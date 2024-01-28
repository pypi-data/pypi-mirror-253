# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import inspect
from typing import Literal

import aiopki
import pydantic
from aiopki.ext.jose import JWKS
from aiopki.ext.jose import OIDCToken
from canonical.security import DomainACL

from oauthx.client.models import Client as ConsumingClient
from oauthx.lib.models import AuthorizationResponse
from oauthx.lib.models import ClientAuthorizationState
from oauthx.lib.models import ObtainedGrant
from oauthx.lib.types import ClientSecret
from oauthx.server.models import ClientType
from oauthx.server.types import UnusableAccount


class ProviderConfig(pydantic.BaseModel):
    audience: Literal['personal', 'institutional']
    client_id: str
    client: ConsumingClient | None = None
    credential: aiopki.CryptoKeyType | aiopki.StringSecret | ClientSecret
    display_name: str
    domains: DomainACL = pydantic.Field(
        default_factory=DomainACL.null
    )
    issuer: str
    logo_url: str
    name: str
    params: dict[str, str] = {}
    protocol: Literal['oidc']
    scope: list[str] = []
    trust_email: bool = False
    trust_phonenumber: bool = False

    def process_oidc_token(self, client: ClientType, state: ClientAuthorizationState, token: OIDCToken) -> OIDCToken:
        if not token.email:
            raise NotImplementedError
        token.email_verified = self.trust_email
        token.phone_number_verified = self.trust_phonenumber
        if not self.domains.allows(token.email.domain):
            raise UnusableAccount({
                'authorize_url': state.authorize_url,
                'allowed_domains': self.domains,
                'account_email': token.email,
                'account_email_domain': token.email.domain,
                'client_name': client.client_name,
                'provider': self,
                'reason': 'UNUSABLE_PROVIDER',
                'return_url': state.annotation('return-url'),
                'token': token
            })
        return token

    async def identify(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        return_url: str,
        state_class: type[ClientAuthorizationState] = ClientAuthorizationState
    ) -> ClientAuthorizationState:
        await self
        assert self.client is not None
        return await self.client.authorize(
            redirect_uri=redirect_uri,
            scope=set(self.scope),
            response_type='code',
            state_class=state_class,
            prompt={'consent'},
            annotations={
                'client-id': client_id,
                'return-url': return_url,
                'provider': self.name
            },
            **self.params
        )

    async def discover(self):
        if self.client is None:
            if inspect.isawaitable(self.credential):
                self.credential = await self.credential
            if not isinstance(self.credential, (JWKS, str)):
                raise RuntimeError(
                    f"Unable to discover {type(self).__name__}.credential by "
                    f"awaiting, got {type(self.credential).__name__}"
                )
            self.client = ConsumingClient.model_validate({
                'provider': self.issuer,
                'client_id': self.client_id,
                'credential': self.credential
            })
            
    async def authorization_code(
        self,
        params: AuthorizationResponse,
        state: ClientAuthorizationState
    ) -> ObtainedGrant:
        await self
        assert self.client is not None
        obtained = await self.client.authorization_code(params, state)
        if obtained.id_token is None:
            raise NotImplementedError
        return obtained

    def __await__(self):
        return self.discover().__await__()