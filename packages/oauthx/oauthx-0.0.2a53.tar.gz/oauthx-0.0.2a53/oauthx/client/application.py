# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import inspect
import logging
from typing import Any
from typing import Callable
from typing import Iterable
from typing import TypeVar

import fastapi
import starlette.routing
from canonical.exceptions import ProgrammingError
from fastapi.types import DecoratedCallable

from oauthx.lib import utils
from oauthx.lib.exceptions import StopSnooping
from oauthx.lib.templates import TemplateService
from oauthx.lib.params import AuthorizationResponse
from oauthx.lib.params import ClientAuthorizationState
from oauthx.lib.params import Storage
from oauthx.lib.protocols import IClientStorage
from oauthx.lib.protocols import BaseSettings
from .clientapiroute import ClientAPIRoute
from .clientresolver import ClientResolver
from .params import ApplicationClient


T = TypeVar('T', bound=fastapi.FastAPI)


class ClientApplication(fastapi.FastAPI):
    __module__: str = 'oauthx.client'
    on_error_handler: Callable[..., Any] | None = None
    oauth: fastapi.APIRouter
    logger: logging.Logger = logging.getLogger('uvicorn')
    authorize_params: dict[str, Any]
    clients: ClientResolver
    scope: set[str]
    welcome_name: str
    welcome_path: str

    @classmethod
    def create_application(
        cls,
        *,
        settings: BaseSettings,
        client: ClientResolver,
        storage_class: type[IClientStorage],
        scope: Iterable[str] | None = None,
        login_path: str = '/login',
        login_name: str = 'oauth2.login',
        callback_path: str = '/oauth/v2/callback',
        callback_name: str = 'oauth2.callback',
        dependencies: list[Any] = [],
        auto_login: bool = False,
        redirect_root: bool = False,
        templates: TemplateService | None = None,
        template_dirs: list[str] | None = None,
        template_packages: list[str] | None = None,
        welcome_path: str = '/welcome',
        welcome_name: str = 'welcome',
        **kwargs: Any
    ):
        if templates is None:
            templates = TemplateService()
        app = cls(
            dependencies=[
                settings.inject(),
                templates.inject(
                    template_dirs=template_dirs,
                    packages=template_packages,
                ),
                storage_class.inject(),
                fastapi.Depends(client),
                *dependencies
            ],
            **kwargs
        )
        app.authorize_params = {}
        app.clients = client
        app.scope = set(scope or [])
        app.welcome_name = welcome_name
        app.welcome_path = welcome_path
        router = app.oauth = fastapi.APIRouter(route_class=ClientAPIRoute)
        router.add_api_route(
            methods=['GET'],
            path=callback_path,
            endpoint=app.callback,
            name=callback_name,
            dependencies=[
                client.as_provider(),
                *dependencies
            ],
            include_in_schema=False,
        )

        if auto_login:
            @app.get(login_path, include_in_schema=False)
            async def _(
                request: fastapi.Request,
            ) -> fastapi.Response:
                return fastapi.responses.RedirectResponse(
                    status_code=302,
                    url=request.url_for(login_name, preset='_')
                )

            @router.get(f'{login_path}/{{preset}}', name=login_name, include_in_schema=False)
            async def _(
                request: fastapi.Request,
                client: ApplicationClient,
                storage: Storage,
                preset: str = fastapi.Path(...),
            ) -> fastapi.Response:
                if preset not in app.authorize_params and preset != '_':
                    app.logger.warning("Authorization preset %s does not exist", preset[:32])
                    raise StopSnooping
                params = app.authorize_params.get(preset, {})
                state = await client.authorize(
                    redirect_uri=str(request.url_for(callback_name)),
                    **params
                )
                state.annotate('return-url', '/welcome')
                await storage.persist(state)
                return fastapi.responses.RedirectResponse(
                    status_code=302,
                    url=state.get_authorize_url()
                )

        if redirect_root:
            @router.get('/', include_in_schema=False)
            def _(request: fastapi.Request) -> fastapi.Response:
                try:
                    return fastapi.responses.RedirectResponse(
                        status_code=303,
                        url=request.url_for(login_name, preset='_')
                    )
                except starlette.routing.NoMatchFound:
                    raise ProgrammingError(
                        "No login endpoint is defined for this application. "
                        f"Use the {type(app).__name__}.on_login() decorator "
                        "to implement the login endpoint."
                    )

        app.include_router(router=router)
        return app

    async def callback(
        self,
        request: fastapi.Request,
        client: ApplicationClient,
        state: ClientAuthorizationState,
        response: AuthorizationResponse
    ) -> fastapi.Response:
        params = await client.on_redirected(state, response) # type: ignore
        name = 'oauth2.success'
        if params.is_error():
            name = 'oauth2.error'
        try:
            return fastapi.responses.RedirectResponse(
                status_code=302,
                url=request.url_for(name)\
                    .include_query_params(**request.query_params)
            )
        except starlette.routing.NoMatchFound:
            if params.is_error():
                return fastapi.responses.PlainTextResponse(
                    status_code=400,
                    content=f"{params.error}: {params.error_description}"
                )
            raise 

    def has_preset(self, name: str) -> bool:
        return name in self.authorize_params

    def login(self, preset: str, scope: Iterable[str] | None = None, **kwargs: Any) -> None:
        if preset == '_':
            raise ProgrammingError(
                "The _ preset is used for the default login endpoint "
                "if not preset is defined. It used the default settings "
                "specified for the client."
            )
        self.authorize_params[preset] = {
            **kwargs,
            'scope': set(scope or []) | self.scope
        }

    def on_authorized(
        self,
        preset: str,
        *,
        path_prefix: str = '/oauth/v2/success',
        name: str = 'oauth2.success'
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        """Registers a function to handle a successful authorization."""
        if str.endswith(path_prefix, '/') or not str.startswith(path_prefix, '/'):
            raise ProgrammingError(
                "The path_prefix parameter must begin with a slash and not end "
                "with a slash."
            )
        if preset not in self.authorize_params:
            raise ProgrammingError(
                f"The preset '{preset}' has not been declared. "
                f"Call {type(self).__name__}.login() to declare "
                "a preset."
            )
        def decorator(func: DecoratedCallable) -> DecoratedCallable:
            async def f(request: fastapi.Request, **kwargs: Any) -> fastapi.Response:
                response = utils.merged_call(func, {
                    **kwargs,
                    'request': request
                })
                if inspect.isawaitable(response):
                    response = await response
                params = {'channel': preset}
                if response is None:
                    response = fastapi.responses.RedirectResponse(
                        status_code=302,
                        url=request.url_for(self.welcome_name)\
                            .include_query_params(**params)
                    )
                return response

            f.__signature__ = utils.merge_signatures([ # type: ignore
                inspect.signature(f),
                inspect.signature(func)
            ])
            self.add_api_route(
                methods=['GET'],
                path=f'{path_prefix}/{preset}',
                endpoint=f,
                name=name,
                dependencies=[self.clients.as_provider()],
                include_in_schema=False
            )
            return func
        return decorator

    def welcome(self, func: DecoratedCallable) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return self.get(self.welcome_path, name=self.welcome_name)(func)


create_application = ClientApplication.create_application