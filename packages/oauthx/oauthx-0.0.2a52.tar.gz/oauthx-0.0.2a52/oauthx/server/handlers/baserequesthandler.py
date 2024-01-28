# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import contextlib
import inspect
import logging
import uuid
from typing import Any
from typing import Sequence
from typing import TypeVar

import fastapi
import fastapi.params

from oauthx.lib import utils
from oauthx.server.models import ClientKey
from oauthx.server.request import Request
from ..config import Config
from ..params import AuthorizationServer
from ..params import CurrentConfig
from ..params import ObjectFactory
from ..params import Storage
from ..params import TokenSigner


T = TypeVar('T', bound='BaseRequestHandler')


class BaseRequestHandler:
    """Handles a request to the authorization server."""
    __module__: str = 'oauthx.server.handlers'
    dependencies: list[fastapi.params.Depends] = []
    include_in_schema: bool = True
    methods: list[str] = ['GET']
    name: str
    logger: logging.Logger = logging.getLogger('uvicorn')
    path: str
    responses: dict[int | str, Any] = {}
    response_class: type[fastapi.Response] = fastapi.responses.Response
    response_description: str
    route_class: type[fastapi.routing.APIRoute] | None = None
    storage: Storage
    status_code: int = 200
    summary: str
    tags: Sequence[str] = ['OAuth 2.x/OpenID Connect']

    @utils.class_property
    def __signature__(cls) -> inspect.Signature:
        return utils.merge_signatures([
            inspect.signature(cls.__init__),
            inspect.signature(cls.setup)
        ])

    @classmethod
    def inject(cls: type[T]) -> fastapi.Response:
        async def f(request: Request, handler: T = fastapi.Depends(cls)):
            async with handler.transaction(request):
                response = await handler.prepare(request) or await handler.handle(request)
                return await handler.process_response(request, response)
        return fastapi.Depends(f)

    @classmethod
    def add_to_router(
        cls,
        router: fastapi.APIRouter | fastapi.FastAPI,
        name: str | None = None,
        dependencies: Sequence[fastapi.params.Depends] = [],
        route_class: type[fastapi.routing.APIRoute] | None = None,
        path: str | None = None,
        prefix: str = '',
        **kwargs: Any,
    ) -> None:
        async def f(response: Any = cls.inject()):
            return response
        f.__doc__ = cls.__doc__

        if isinstance(router, fastapi.APIRouter):
            route_class = route_class or cls.route_class
            if route_class is not None:
                kwargs['route_class_override'] = route_class
        router.add_api_route(
            methods=cls.methods,
            path=path or f'{prefix}{cls.path}',
            endpoint=f,
            include_in_schema=cls.include_in_schema,
            name=name or cls.name,
            summary=cls.summary,
            description=cls.__doc__,
            status_code=cls.status_code,
            dependencies=[*list(dependencies), *cls.dependencies],
            response_class=cls.response_class,
            response_description=cls.response_description,
            response_model=None,
            responses=dict(cls.responses),
            tags=list(cls.tags),
            **kwargs
        )


    def __init__(
        self,
        server: AuthorizationServer,
        request: Request,
        storage: Storage,
        factory: ObjectFactory,
        signer: TokenSigner,
        config: Config = CurrentConfig,
        **kwargs: Any
    ):
        self.config = config
        self.factory = factory
        self.request = request
        self.server = server
        self.signer = signer
        self.storage = storage
        self.setup(**kwargs)

    def redirect(self, url: str, status_code: int = 302) -> fastapi.Response:
        return fastapi.responses.RedirectResponse(
            status_code=status_code,
            url=url
        )

    def setup(self, **_: Any):
        pass

    async def handle(self, request: Request) -> fastapi.Response:
        raise NotImplementedError

    async def incident(self, request: Request) -> fastapi.Response:
        return await request.render_to_response(
            'oauthx/security/incident.html.j2',
            context={
            'incident_id': uuid.uuid4(),
            },
            status_code=403
        )

    @contextlib.asynccontextmanager
    async def transaction(self, request: Request):
        await self.begin(request)
        try:
            yield self
        except Exception as e:
            await self.on_exception(e)
            raise
        else:
            await self.commit(request)

    async def begin(self, request: Request) -> None:
        pass

    async def prepare(self, request: Request) -> fastapi.Response | None:
        pass

    async def process_response(
        self,
        request: Request,
        response: fastapi.Response
    ) -> fastapi.Response:
        return response

    async def commit(self, request: Request) -> None:
        pass

    async def get_client_id(self) -> ClientKey:
        raise NotImplementedError

    async def on_exception(self, exception: Exception) -> None:
        pass