# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
import secrets
from typing import Any
from typing import Iterable
from typing import TypeVar

import httpx
import pydantic
from aiopki.ext.jose import JWA
from aiopki.lib import JSONWebKeySet
from canonical import PersistedModel

from oauthx.lib import utils
from oauthx.lib.models import ObtainedGrant
from oauthx.lib.types import ClientCredentialType
from oauthx.lib.types import ClientSecret
from oauthx.lib.types import PrompType
from oauthx.lib.types import ResponseModeType
from oauthx.lib.types import ResponseType
from .authorizationresponse import AuthorizationResponse
from .clientauthorizationstate import ClientAuthorizationState
from .error import Error
from .grant import Grant
from .provider import Provider
from .redirectionparameters import RedirectionParameters


T = TypeVar('T', bound=ClientAuthorizationState)


class Client(PersistedModel):
    auth_method: str | None = pydantic.Field(
        default=None
    )

    client_id: str = pydantic.Field(
        default=...
    )

    client_secret: ClientSecret | None = pydantic.Field(
        default=None
    )

    credential: ClientCredentialType | None = pydantic.Field(
        default=None
    )

    port: int | None = pydantic.Field(
        default=None
    )

    provider: Provider = pydantic.Field(
        default=...
    )

    response_mode: ResponseModeType = pydantic.Field(
        default='query'
    )

    response_type: ResponseType = pydantic.Field(
        default='code'
    )

    # RFC 7591
    token_endpoint_auth_method: str = pydantic.Field(
        default=...
    )

    # JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
    authorization_signed_response_alg: JWA = pydantic.Field(
        default=JWA.rs256
    )

    model_config = {
        'arbitrary_types_allowed': True,
    }

    @property
    def pk(self) -> str:
        return self.client_id

    @pydantic.field_validator('provider', mode='before')
    def preprocess_provider(
        cls,
        value: Provider | dict[str, str] | str
    ) -> Provider:
        if isinstance(value, str):
            value = {'issuer': value}
        if isinstance(value, dict):
            if not value.get('issuer'):
                raise ValueError("The `issuer` parameter is required.")
            value = Provider.model_validate({
                'iss': value.get('issuer'),
                **value
            })
        return value

    def can_encrypt(self) -> bool:
        return any([
            isinstance(self.credential, JSONWebKeySet) and self.credential.can_encrypt()
        ])

    def get_local_port(self) -> int:
        return self.port or utils.random_port()

    def is_confidential(self) -> bool:
        return isinstance(self.credential, JSONWebKeySet)

    async def authenticate(self, grant: Grant) -> bool:
        grant.root.client_id = self.client_id
        if isinstance(self.credential, str):
            grant.root.client_secret = self.credential
        if self.client_secret is not None and self.token_endpoint_auth_method == 'client_secret_post':
            grant.root.client_secret = self.client_secret
        return True

    @utils.http
    async def authorize(
        self,
        http: httpx.AsyncClient,
        *,
        redirect_uri: str | None = None,
        scope: Iterable[str] | None = None,
        response_type: ResponseType | None = None,
        state_class: type[T] = ClientAuthorizationState,
        prompt: Iterable[PrompType] = [],
        annotations: dict[str, str] | None = None,
        **params: Any
    ) -> T:
        """Create an authorization request and return the URL to
        which a user-agent must be redirectred.
        """
        await self.provider.discover(http)
        scope = scope or set()
        params = {
            **params,
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'scope': str.join(' ', sorted(scope)),
            'response_type': response_type or self.response_type,
            'response_mode': self.response_mode,
            'state': secrets.token_urlsafe(32)
        }
        if 'openid' in scope:
            params.update({
                'nonce': secrets.token_urlsafe(32),
                'prompt': str.join(' ', set(prompt))
            })
        url = self.provider.authorize(**{k: v for k, v in params.items() if v})
        return state_class.model_validate({
            'authorize_url': url,
            'client_id': self.client_id,
            'params': params,
            'annotations': annotations or {}
        })

    async def authorization_code( # type: ignore
        self,
        params: AuthorizationResponse | Error | RedirectionParameters,
        state: ClientAuthorizationState,
        http: httpx.AsyncClient | None = None,
        resources: str | list[str] | None = None
    ) -> ObtainedGrant:
        """Use the query parameters that the authorization server
        supplied to the client redirection endpoint to obtain
        an access token.
        """
        if isinstance(resources, str):
            resources = [resources]
        if not isinstance(params, (Error, RedirectionParameters)):
            params = await self.on_redirected(state, params)
        params.raise_for_status()
        assert isinstance(params, RedirectionParameters), type(params)
        grant = Grant.model_validate({
            'grant_type': 'authorization_code',
            'code': params.code,
            'redirect_uri': state.redirect_uri,
            'resources': resources
        })
        obtained = await self.grant(grant, http=http)
        if obtained.id_token is not None:
            if obtained.id_token.is_encrypted():
                raise NotImplementedError
            await self.provider.verify_id_token(obtained.id_token)
        return obtained

    async def discover(self, http: httpx.AsyncClient) -> None:
        await self.provider.discover(http)

    async def refresh(
        self,
        refresh_token: str,
        scope: Iterable[str] | None = None,
        http: httpx.AsyncClient | None = None,
        resources: list[str] | None = None,
        resource: str | None = None
    ) -> ObtainedGrant:
        resources = list(resources or [])
        if resource:
            resources.append(resource)
        grant = Grant.model_validate({
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'scope': set(scope) if scope else None,
            'resources': resources
        })
        return await self.grant(grant, http=http)

    @functools.singledispatchmethod
    async def grant(
        self,
        params: AuthorizationResponse,
        *args: Any,
        **kwargs: Any
    ) -> ObtainedGrant:
        raise NotImplementedError(params)

    @grant.register
    async def _(
        self,
        grant: Grant,
        authenticate: bool = True,
        http: httpx.AsyncClient | None = None
    ) -> ObtainedGrant:
        if authenticate:
            await self.authenticate(grant)
        return await self.provider.grant(grant, http=http)

    async def on_redirected(
        self,
        state: ClientAuthorizationState,
        params: dict[str, Any] | AuthorizationResponse | Error | RedirectionParameters
    ) -> Error | RedirectionParameters:
        """Processes the parameters that were supplied by the authorization
        server to the redirection endpoint.
        """
        await self.provider
        if not isinstance(params, (Error, RedirectionParameters)):
            if not isinstance(params, AuthorizationResponse):
                params = AuthorizationResponse.model_validate(params)
            await params.decode(
                issuer=self.provider.issuer,
                client_id=self.client_id,
                verifier=self.provider.signing_keys,
                decrypter=self.credential
            )
            assert isinstance(params.root, (Error, RedirectionParameters))
            params = params.root

        if isinstance(params, RedirectionParameters):
            await self.provider.verify(params)
            await state.verify(params)
        return params

    async def userinfo(self, access_token: str, http: httpx.AsyncClient | None = None):
        return await self.provider.userinfo(access_token, http=http)