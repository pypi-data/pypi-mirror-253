# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Protocol

import fastapi
from aiopki.types import ISigner

from oauthx.lib.types import GrantType
from oauthx.lib.types import ResponseType


class IResponseMode(Protocol):
    __module__: str = 'oauthx.server.types'
    response_type: ResponseType

    def get_token_types(self) -> set[str]: ...
    def grants(self) -> GrantType | None: ...
    def with_signer(self, signer: ISigner) -> 'IResponseMode': ...

    async def deny(self) -> str: ...

    async def error(
        self,
        *,
        error: str,
        error_description: str | None = None,
        error_uri: str | None = None
    ) -> str:
        ...

    async def redirect(self, **kwargs: Any) -> fastapi.responses.RedirectResponse: ...