# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pydantic

from oauthx.lib.types import ResponseType
from oauthx.server.types import InvalidResponseType
from .confidentialclient import ConfidentialClient
from .responsemode import ResponseMode
from .publicclient import PublicClient


class AuthorizationContext(pydantic.BaseModel):
    client: ConfidentialClient | PublicClient
    response_mode: ResponseMode

    @property
    def response_type(self) -> ResponseType:
        return self.response_mode.response_type

    def can_redirect(self) -> bool:
        return self.response_mode.can_redirect()

    def model_post_init(self, __context: Any) -> None:
        if not self.client.allows_response_type(self.response_type):
            raise InvalidResponseType

    async def get_template_context(self) -> dict[str, Any]:
        return {
            'client_name': self.client.client_name,
            'deny_url': await self.deny()
        }
    async def deny(self) -> str:
        return await self.response_mode.error(error='access_denied')

    async def error(self, **params: Any) -> str:
        return await self.response_mode.error(**params)