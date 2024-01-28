# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Iterable
from typing import MutableMapping
from typing import TypeVar

import httpx
import pydantic
from aiopki.ext.jose import JWKS
from aiopki.ext.jose import OIDCToken
from canonical.exceptions import ProgrammingError

from oauthx.lib.models import AuthorizationResponse
from oauthx.lib.models import ClientAuthorizationState
from oauthx.lib.models import Grant
from oauthx.lib.models import JWTBearerAssertion
from oauthx.lib.models import ObtainedGrant
from oauthx.lib.models import Provider
from oauthx.lib.protocols import IStorage
from oauthx.lib.types import GrantType
from oauthx.lib.types import PrompType
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import ResponseType
from oauthx.server.protocols import IRequestSubject
from oauthx.server.protocols import IResourceOwner
from .clientkey import ClientKey
from .confidentialclient import ConfidentialClient
from .publicclient import PublicClient


T = TypeVar('T')


class Client(pydantic.RootModel[ConfidentialClient | PublicClient]):
    Key: ClassVar[type[ClientKey]] = ClientKey

    @property
    def id(self) -> ClientKey:
        return ClientKey(self.root.client_id)

    @property
    def pk(self) -> ClientKey:
        return ClientKey(self.root.client_id)

    @property
    def provider(self) -> Provider:
        return self.root.provider

    def allows_delegation_to(self, userinfo: OIDCToken) -> bool:
        return self.root.allows_delegation_to(userinfo)

    def allows_response_type(self, response_type: ResponseType) -> bool:
        return self.root.allows_response_type(response_type)

    def allows_scope(self, scope: set[str]) -> bool:
        return self.root.allows_scope(scope)

    def can_encrypt(self) -> bool:
        return self.root.can_encrypt()

    def can_grant(self, grant_type: GrantType | None) -> bool:
        """Return a boolean indicating if the client allows the given
        `grant_type`.
        """
        return self.root.can_grant(grant_type)

    def can_redirect(self, redirect_uri: RedirectURI | None) -> bool:
        return self.root.can_redirect(redirect_uri)

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        return self.root.contribute_to_userinfo(userinfo)

    def get_audience(self) -> str | None:
        return self.root.audience

    def get_default_redirect_uri(self) -> RedirectURI:
        return self.root.get_default_redirect_uri()

    def get_display_name(self) -> str:
        return self.root.get_display_name()

    def get_logo_url(self) -> str | None:
        return self.root.get_logo_url()

    def get_providers(self):
        return self.root.get_providers()

    def get_sector_identifier(self) -> str:
        return self.root.sector_identifier

    def get_splash_image_url(self) -> str:
        return self.root.get_splash_image_url()

    def has_redirection_endpoints(self) -> bool:
        return self.root.has_redirection_endpoints()

    def is_confidential(self) -> bool:
        return self.root.is_confidential()

    def is_public(self) -> bool:
        return isinstance(self.root, PublicClient)

    def must_push(self) -> bool:
        return False

    def resource_owner(self, subject: IRequestSubject) -> IResourceOwner.Key:
        return IResourceOwner.Key(str(self.id), str(subject.id)) # type: ignore

    def requires_state(self) -> bool:
        return False

    def update_key(self, update: Callable[[bytes], None]):
        return self.root.update_key(update)

    @functools.singledispatchmethod
    async def authenticate(self, *args: Any, **kwargs: Any) -> bool:
        """Authenticates the grant using the method specified by the
        client.
        """
        return await self.root.authenticate(*args, **kwargs)

    @functools.singledispatchmethod
    async def grant(
        self,
        params: AuthorizationResponse,
        *args: Any,
        **kwargs: Any
    ) -> ObtainedGrant:
        raise NotImplementedError(params)

    @grant.register
    async def authorization_code( # type: ignore
        self,
        params: AuthorizationResponse,
        state: ClientAuthorizationState,
        http: httpx.AsyncClient | None = None,
    ) -> ObtainedGrant:
        """Use the query parameters that the authorization server
        supplied to the client redirection endpoint to obtain
        an access token.
        """
        if isinstance(params, dict):
            params = AuthorizationResponse.model_validate(params)
        params.raise_for_status()
        await params.verify(self.provider, state)

        grant = Grant.model_validate({
            'grant_type': 'authorization_code',
            'code': params.code,
            'redirect_uri': state.redirect_uri
        })
        return await self.grant(grant, http=http)

    async def authorize(
        self,
        *,
        redirect_uri: str | None = None,
        scope: Iterable[str] | None = None,
        response_type: ResponseType | None = None,
        state_class: type[T] = ClientAuthorizationState,
        prompt: Iterable[PrompType] | None = None
    ) -> T:
        """Create an authorization request and return the URL to
        which a user-agent must be redirectred.
        """
        return await self.root.authorize( # type: ignore
            redirect_uri=redirect_uri,
            scope=scope,
            response_type=response_type,
            state_class=state_class,
            prompt=list(prompt or [])
        )

    async def client_credentials(
        self,
        scope: Iterable[str],
        http: httpx.AsyncClient | None = None,
    ) -> ObtainedGrant:
        grant = Grant.model_validate({
            'grant_type': 'client_credentials',
            'scope': scope
        })
        return await self.grant(grant, http=http)

    async def jwt(
        self,
        sub: str,
        authenticate: bool = False,
        http: httpx.AsyncClient | None = None,
        **claims: Any
    ):
        """Obtain an access token using a JWT bearer token."""
        if not self.is_confidential():
            raise ProgrammingError(
                "Only confidential clients can use the urn:ietf:para"
                "ms:oauth:grant-type:jwt-bearer grant. This client "
                f"uses: {type(self.root.credential).__name__}."
            )
        assert isinstance(self.root.credential, JWKS)
        assertion = await JWTBearerAssertion.new(
            signer=self.root.credential,
            iss=self.root.client_id,
            sub=sub,
            token_endpoint=str(self.provider.token_endpoint)
        )
        return await self.grant(assertion, authenticate=authenticate, http=http)

    async def persist(self, storage: IStorage) -> None:
        await storage.persist(self)

    @functools.singledispatchmethod
    async def refresh(
        self,
        obj: ObtainedGrant | str,
        *args: Any,
        **kwargs: Any
    ) -> ObtainedGrant:
        raise NotImplementedError
    
    @refresh.register
    async def _refresh_grant(
        self,
        grant: ObtainedGrant,
        *args: Any,
        **kwargs: Any
    ) -> ObtainedGrant:
        return await self.refresh(grant.refresh_token)

    @refresh.register
    async def _refresh_token(
        self,
        token: str,
        scope: Iterable[str] | None = None
    ) -> ObtainedGrant:
        grant = Grant.model_validate({
            'grant_type': 'refresh_token',
            'refresh_token': token,
            'scope': str.join(' ', list(sorted(filter(bool, set(scope))))) if scope else None
        })
        return await self.grant(grant)

    @grant.register
    async def _grant(
        self,
        grant: Grant,
        authenticate: bool = True,
        http: httpx.AsyncClient | None = None
    ) -> ObtainedGrant:
        if authenticate:
            await self.authenticate(grant)
        return await self.provider.grant(grant, http=http)

    @grant.register
    async def _(
        self,
        assertion: JWTBearerAssertion,
        authenticate: bool = True,
        http: httpx.AsyncClient | None = None
    ) -> ObtainedGrant:
        return await self.grant(
            assertion.model_dump(mode='json'),
            authenticate=authenticate,
            http=http
        )

    @grant.register
    async def _(
        self,
        params: dict, # type: ignore
        authenticate: bool = True,
        http: httpx.AsyncClient | None = None
    ) -> ObtainedGrant:
        return await self.grant(
            Grant.model_validate(params),
            authenticate=authenticate,
            http=http
        )