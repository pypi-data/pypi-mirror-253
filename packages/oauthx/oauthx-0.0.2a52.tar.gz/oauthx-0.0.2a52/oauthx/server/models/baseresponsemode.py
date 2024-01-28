# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import aiopki
import fastapi
import pydantic

from oauthx.lib.types import GrantType
from oauthx.lib.types import RedirectURI
from .confidentialclient import ConfidentialClient
from .publicclient import PublicClient


RESPONSE_TOKEN_TYPES: dict[str, str] = {
    'code'      : 'urn:ietf:params:oauth:token-type:access_token',
    'token'     : 'urn:ietf:params:oauth:token-type:access_token',
    'id_token'  : 'urn:ietf:params:oauth:token-type:id_token'
}


class BaseResponseMode(pydantic.BaseModel):
    client: ConfidentialClient | PublicClient
    redirect_uri: RedirectURI | None = None
    state: str | None = None
    iss: str

    @property
    def grant_type(self) -> GrantType | None:
        raise NotImplementedError

    def get_params(self) -> dict[str, str]:
        return self.model_dump(include={'state'}, exclude_none=True)

    def get_redirect_uri(self) -> RedirectURI:
        return self.redirect_uri or self.client.get_default_redirect_uri()

    def get_responses(self) -> set[str]:
        raise NotImplementedError

    def get_token_types(self) -> set[str]:
        return set(filter(bool, [RESPONSE_TOKEN_TYPES.get(x, '') for x in self.get_responses()]))

    async def deny(self) -> str:
        raise NotImplementedError

    async def error(
        self,
        *,
        error: str,
        error_description: str | None = None,
        error_uri: str | None = None
    ) -> str:
        raise NotImplementedError

    async def redirect(self, signer: aiopki.CryptoKeyType, **kwargs: Any) -> fastapi.responses.RedirectResponse:
        raise NotImplementedError