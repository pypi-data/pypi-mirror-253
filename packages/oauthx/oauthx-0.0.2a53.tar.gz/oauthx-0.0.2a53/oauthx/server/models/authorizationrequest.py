# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import MutableMapping

import fastapi
import pydantic
from aiopki.utils import b64encode_int
from canonical.exceptions import ProgrammingError

from oauthx.lib.protocols import IClient
from oauthx.lib.protocols import IStorage
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import ResponseType
from oauthx.lib.types import ScopeType
from oauthx.lib.types import TargetResource
from oauthx.server.types import AuthorizationRequestKey
from .authorizationcontext import AuthorizationContext
from .basemodel import BaseModel
from .clientkey import ClientKey
from .responsemode import ResponseMode


class AuthorizationRequest(BaseModel):
    id: int
    client_name: str
    iss: str
    
    # https://datatracker.ietf.org/doc/html/rfc6749
    client_id: ClientKey = pydantic.Field(
        default=...
    )

    redirect_uri: RedirectURI | None = pydantic.Field(
        default=None
    )

    response_type: ResponseType = pydantic.Field(
        default=...
    )

    scope: ScopeType = pydantic.Field(
        default_factory=ScopeType
    )

    state: str | None = pydantic.Field(
        default=None
    )
    
    # https://datatracker.ietf.org/doc/html/rfc8707
    resources: set[TargetResource] = pydantic.Field(
        default_factory=set
    )
    
    # https://openid.net/specs/openid-connect-core-1_0.html
    nonce: str | None = pydantic.Field(
        default=None
    )

    # https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html
    response_mode: str | None = pydantic.Field(
        default=None
    )

    @property
    def request_uri(self) -> str:
        return f'urn:ietf:params:oauth:request_uri:{b64encode_int(self.id, encoder=bytes.decode)}'

    @property
    def pk(self) -> AuthorizationRequestKey:
        return AuthorizationRequestKey(self.id)

    def add_to_template_context(self, request: fastapi.Request, context: dict[str, Any]):
        context.update({
            'authorize_url': request.url_for('oauth2.authorize').include_query_params(
                client_id=self.client_id,
                request_uri=self.request_uri
            ),
            'client_name': self.client_name,
            'deny_url': request.url_for('oauth2.deny', pk=self.id),
        })

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        if self.nonce is not None:
            userinfo['nonce'] = self.nonce

    def get_authorize_url(self, request: fastapi.Request) -> str:
        url = request.url_for('oauth2.authorize')\
            .include_query_params(
                client_id=self.client_id,
                request_uri=self.request_uri
            )
        return str(url)

    def get_response_mode(self, client: IClient) -> ResponseMode:
        return ResponseMode.model_validate({
            'iss': self.iss,
            'client': client,
            'redirect_uri': self.redirect_uri,
            'state': self.state,
            'response_type': self.response_type,
            'response_mode': self.response_mode
        })

    async def deny(self, client: IClient, exception: bool = False) -> str:
        response_mode = self.get_response_mode(client)
        return await response_mode.deny()

    async def get_client(self, storage: IStorage) -> IClient:
        client = await storage.get(self.client_id)
        if client is None:
            raise ProgrammingError(
                "The authorization request references a client that does "
                "not exist."
            )
        return client

    async def get_context(self, storage: IStorage) -> AuthorizationContext:
        client = await self.get_client(storage)
        return AuthorizationContext.model_validate({
            'client': client.root, # type: ignore
            'response_mode': self.get_response_mode(client.root) # type: ignore
        })