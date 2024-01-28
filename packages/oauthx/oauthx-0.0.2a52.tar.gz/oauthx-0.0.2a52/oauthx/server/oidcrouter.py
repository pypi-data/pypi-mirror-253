# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import json
from typing import Any
from typing import Callable

import fastapi
import fastapi.params
import httpx
import yaml
from aiopki.ext.jose import JWA
from aiopki.ext.jose import JWKS
from aiopki import CryptoKeyType
from aiopki.types import ISigner
from jinja2 import Environment
from jinja2 import BaseLoader
from jinja2 import PackageLoader
from jinja2 import ChoiceLoader
from jinja2 import FileSystemLoader

from oauthx.lib.models import ServerMetadata
from oauthx.lib.params import ApplicationStorage
from oauthx.lib.params import NextURL
from oauthx.lib.templates import TemplateService
from oauthx.lib.utils import set_signature_defaults
from .authorizationserver import AuthorizationServer
from .config import Config
from .handlers import AuthorizationRequestHandler
from .handlers import TokenEndpointHandler
from .handlers import UpstreamBeginHandler
from .handlers import UpstreamCallbackHandler
from .handlers import UserInfoEndpointHandler
from .clientroutehandler import ClientRouteHandler
from .oidcroutehandler import OIDCRouteHandler
from .params import PendingAuthorizationClient
from .params import PendingAuthorizationRequest
from .params import RequestSession
from .params import Storage
from .params import RequestUserInfo
from .pluginendpoint import PluginEndpoint
from .request import Request
from .subjectlogger import SubjectLogger


class OIDCRouter(fastapi.APIRouter):
    __module__: str = 'oauthx.server'
    config: Config
    http: httpx.AsyncClient | None = None
    jwks: JWKS
    signer: ISigner | None = None

    @classmethod
    def create_server(
        cls,
        config: str | Config,
        dependencies: list[Any] = [],
        asgi_class: type[fastapi.FastAPI] = fastapi.FastAPI,
        http: httpx.AsyncClient | None = None,
        **kwargs: Any
    ):
        if not isinstance(config, Config):
            config = Config.load(config)
        app = asgi_class(dependencies=dependencies, **kwargs)
        router = cls(
            app=app,
            config=config,
            http=http,
        )
        app.include_router(
            router=router
        )
        return app

    @classmethod
    def from_config(cls, app: fastapi.FastAPI, config: str | Config, **kwargs: Any):
        if not isinstance(config, Config):
            config = Config.model_validate({
                **yaml.safe_load(open(config).read()) # type: ignore
            })
        return cls(
            app=app,
            config=config,
            **kwargs
        )

    def __init__(
        self,
        *,
        app: fastapi.FastAPI,
        config: Config,
        template_service: type[TemplateService] = TemplateService,
        authorize_handler: type[AuthorizationRequestHandler] = AuthorizationRequestHandler,
        token_endpoint_handler: type[TokenEndpointHandler] = TokenEndpointHandler,
        login_endpoint: str = 'oauth2.login',
        login_path: str = '/login',
        prefix: str = '/oauth/v2',
        http: httpx.AsyncClient | None = None
    ):
        super().__init__(
            dependencies=[
                fastapi.Depends(SubjectLogger),
                self._wrap_depends('config', self.get_config),
                self._wrap_depends('templates', lambda: template_service(self.templates)),
                ApplicationStorage(config.storage.impl.value),
                self._wrap_depends('http', lambda: self.http),
                self._wrap_depends('keychain', self.get_keychain),
                self._wrap_depends('plugins', lambda: self.plugins),
                self._wrap_depends('signer', self.get_signer),
                self._wrap_depends('token_signer', lambda: self.signing_key),
                self._wrap_depends('oauth', AuthorizationServer),
            ],
            route_class=type('OIDCRouteHandler', (OIDCRouteHandler,), {
                'config': config,
                'login_endpoint': login_endpoint
            }),
        )
        self.app = app
        self.config = config
        self.http = http
        self.plugins = [plugin.value for plugin in config.plugins]
        self.signing_key = config.issuer.signing_key
        self.subject_class = config.authentication.impl.value
        self.template_loaders: list[BaseLoader] = [
            FileSystemLoader('templates/oauthx'),
            PackageLoader('oauthx.lib')
        ]

        # RFC 8414 OAuth 2.0 Authorization Server Metadata
        @app.get('/.well-known/openid-configuration')
        def _(request: Request) -> fastapi.Response:
            return fastapi.responses.RedirectResponse(
                status_code=301,
                url=request.url_for('oauth2.metadata')
            )

        app.add_api_route(
            methods=['GET'],
            path=f'/.well-known/oauth-authorization-server',
            endpoint=self.metadata,
            name='oauth2.metadata',
            summary='Metadata Endpoint',
            response_model=ServerMetadata,
            tags=['OAuth 2.x/OpenID Connect']
        )

        app.add_api_route(
            methods=['GET'],
            path='/.well-known/jwks.json',
            endpoint=self.keys,
            name='oauth2.jwks',
            summary='JSON Web Key Set (JWKS)',
            response_model=JWKS,
            tags=['OAuth 2.x/OpenID Connect']
        )

        # Add the login handler to the fastapi.FastAPI instance instead
        # of the router, as the implementer possibly does not want to
        # expose the login endpoint under /oauth/v2.
        for handler in config.authentication.handlers:
            handler.impl.value.add_to_router(
                router=self,
                name=handler.name,
                path=handler.path,
                dependencies=[
                    self._wrap_depends('subject', self.subject_class.resolve)
                ],
            )

        # If there are upstream identity providers trusted by the
        # authorization server, then add UpstreamLoginRequestHandler
        # so that frontend clients can initate the login flow. This
        # endpoint is added to the router as it is an OAuth-specific
        # concern.
        self.add_api_route(
            methods=['POST'],
            path=f'{prefix}/token',
            endpoint=set_signature_defaults(self.token, {
                'handler': fastapi.Depends(token_endpoint_handler)
            }),
            name='oauth2.token',
            summary="Token Endpoint",
            tags=['OAuth 2.x/OpenID Connect'],
            route_class_override=type('ClientRouteHandler', (ClientRouteHandler,), {
                'config': config,
                'login_endpoint': login_endpoint
            }),
        )

        if config.has_authorize_endpoint():
            authorize_handler.add_to_router(
                router=self,
                dependencies=[
                    self._wrap_depends('subject', self.subject_class.resolve)
                ],
                prefix=prefix
            )

        if self.config.providers:
            UpstreamBeginHandler.add_to_router(
                router=self,
                dependencies=[
                    self._wrap_depends('subject', self.subject_class.resolve)
                ],
                prefix=prefix
            )
            UpstreamCallbackHandler.add_to_router(
                router=self,
                dependencies=[
                    self._wrap_depends('subject', self.subject_class.resolve)
                ],
                prefix=prefix
            )

        UserInfoEndpointHandler.add_to_router(self, prefix=prefix)

        # User interface endpoints
        self.add_api_route(
            methods=['GET'],
            path='/a/{pk}/deny',
            endpoint=self.deny,
            status_code=302,
            name='oauth2.deny',
            summary="Deny authorization request",
            include_in_schema=False
        )
        
        self.add_api_route(
            methods=['POST'],
            path='/logout',
            name='user.logout',
            endpoint=self.logout,
            include_in_schema=False,
        )
        
        self.add_api_route(
            methods=['GET'],
            path='/welcome',
            name='user.welcome',
            endpoint=self.welcome,
            include_in_schema=False,
            dependencies=[
                self._wrap_depends('subject', self.subject_class.resolve)
            ]
        )

        # Load plugins. This should run before initializing the template
        # loaders because plugins are allowed to add them using the
        # OIDCRouter.register_template_module() method.
        for plugin in self.plugins:
            plugin.__register__(self)

        # Initialize templates
        self.templates = Environment(
            extensions=[
                'jinja2.ext.i18n',
                'jinja_markdown.MarkdownExtension'
            ],
            loader=ChoiceLoader(self.template_loaders)
        )
        self.templates.install_null_translations(True) # type: ignore

    def add_plugin(
        self,
        *,
        methods: list[str],
        path: str,
        handler: type,
        method: Callable[..., Any],
        name: str,
        description: str,
        authenticated: bool = True,
        needs_data: bool = False
    ) -> None:
        if str.startswith(path, '/'):
            raise ValueError(f"Path must not start with a slash: {path}")
        path = f'/a/{{pk}}/{path}'
        dependencies: list[fastapi.params.Depends] = [
            self._wrap_depends('subject', self.subject_class.resolve)
        ]

        self.add_api_route(
            methods=methods,
            endpoint=PluginEndpoint(
                'authorize',
                handler,
                method,
                authenticated=authenticated,
                needs_data=needs_data
            ),
            path=path,
            name=name,
            description=description,
            dependencies=dependencies,
            include_in_schema=False
        )

    def register_template_module(self, qualname: str) -> None:
        self.template_loaders.append(PackageLoader(qualname))

    async def authorize(
        self,
        response: Any = NotImplemented,
    ) -> fastapi.Response:
        """The **Authorization Endpoint** provides an interface for Resource Owners
        to interact with the Authorization Server in order to authenticate and
        authorize client requests.
        """
        assert response != NotImplemented
        return response

    async def deny(
        self,
        storage: Storage,
        request: PendingAuthorizationRequest,
        client: PendingAuthorizationClient
    ) -> fastapi.responses.RedirectResponse:
        """Deny an authorization request."""
        await storage.delete(request)
        return fastapi.responses.RedirectResponse(
            status_code=302,
            url=await request.deny(client)
        )

    async def keys(self) -> fastapi.responses.PlainTextResponse:
        await self.config.issuer.encryption_key
        await self.config.issuer.signing_key
        jwks = self.config.issuer.encryption_key | self.config.issuer.signing_key
        return fastapi.responses.PlainTextResponse(
            media_type='application/json;indent=2',
            headers={
                'Cache-Control': (
                    'max-age=43200, '
                    'stale-while-revalidate=43200, '
                    'stale-if-error=43200'
                )
            },
            content=json.dumps(
                jwks.model_dump(exclude_none=True),
                indent=2,
                sort_keys=True
            )
        )

    async def logout(
        self,
        next_url: NextURL,
        session: RequestSession
    ) -> fastapi.Response:
        if next_url is None:
            raise NotImplementedError
        session.logout()
        return fastapi.responses.RedirectResponse(
            status_code=302,
            url=next_url
        )

    async def metadata(
        self,
        request: fastapi.Request
    ) -> fastapi.responses.PlainTextResponse:
        await asyncio.gather(
            asyncio.ensure_future(self.config.issuer.signing_key),
            asyncio.ensure_future(self.config.issuer.encryption_key),
        )
        enc_alg = self.config.issuer.encryption_key.get_encryption_algorithms()
        sig_alg = self.config.issuer.signing_key.get_signing_algorithms()
        cek_alg = [JWA.a128gcm, JWA.a192gcm, JWA.a256gcm]

        obj = ServerMetadata.model_validate({
            'issuer': self.config.issuer.id,
            'authorization_signing_alg_values_supported': sig_alg,
            'authorization_encryption_alg_values_supported': enc_alg,
            'authorization_encryption_enc_values_supported': cek_alg,
            'authorization_response_iss_parameter_supported': True,
            'jwks_uri': str(request.url_for('oauth2.jwks')),
            'id_token_signing_alg_values_supported': sig_alg,
            'id_token_encryption_alg_values_supported': enc_alg,
            'introspection_signing_alg_values_supported': sig_alg,
            'introspection_encryption_alg_values_supported': enc_alg,
            'nfv_token_signing_alg_values_supported': sig_alg,
            'nfv_token_encryption_alg_values_supported': enc_alg,
            'nfv_token_encryption_enc_values_supported': cek_alg,
            'request_object_signing_alg_values_supported': sig_alg,
            'request_object_encryption_alg_values_supported': enc_alg,
            'request_object_encryption_enc_values_supported': cek_alg,
            'token_endpoint_auth_signing_alg_values_supported': sig_alg,
            'userinfo_signing_alg_values_supported': sig_alg,
            'userinfo_encryption_alg_values_supported': enc_alg,
            'userinfo_encryption_enc_values_supported': cek_alg,
            'subject_types_supported': ['public', 'pairwise'],
            'token_endpoint': str(request.url_for('oauth2.token')),
            'userinfo_endpoint': str(request.url_for('oidc.userinfo'))
        })
        if self.config.has_authorize_endpoint():
            obj.authorization_endpoint = str(request.url_for('oauth2.authorize'))
        return fastapi.responses.PlainTextResponse(
            media_type='application/json',
            content=obj.model_dump_json(
                exclude_defaults=True,
                exclude_none=True,
                indent=2
            )
        )

    async def token(
        self,
        request: Request,
        handler: TokenEndpointHandler = NotImplemented,
    ) -> fastapi.Response:
        async with handler.transaction(request):
            return await handler.handle(request)

    async def userinfo(self, response: Any = NotImplemented) -> fastapi.Response:
        assert response != NotImplemented
        return response

    async def welcome(
        self,
        request: Request,
        userinfo: RequestUserInfo,
    ) -> fastapi.Response:
        authorize_url = request.url_for('oauth2.authorize')\
            .include_query_params(
                client_id='self',
                response_type='none',
                scope='openid profile email'
            )
        return await request.render_to_response(
            'oauthx/welcome.html.j2',
            context={
                'login_url': authorize_url,
                'logout_url': request.url_for('user.logout')\
                    .include_query_params(n=authorize_url),
                'userinfo': userinfo
            }
        )

    async def get_config(self) -> Config:
        return self.config

    async def get_keychain(self) -> CryptoKeyType:
        return self.signing_key

    async def get_signer(self) -> ISigner:
        if self.signer is None:
            self.signer = await self.config.ui.session_key # type: ignore
        return self.signer # type: ignore

    def _wrap_depends(
        self,
        name: str,
        dependency: Callable[..., Any]
    ) -> fastapi.params.Depends:
        """Set an attribute on the request object that has an instance of the
        given callable.
        """
        async def f(request: Request, dep: Any = fastapi.Depends(dependency)) -> None:
            setattr(request, name, dep)

        return fastapi.Depends(f)