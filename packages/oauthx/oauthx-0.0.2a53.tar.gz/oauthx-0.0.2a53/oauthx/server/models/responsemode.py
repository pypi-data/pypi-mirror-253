# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Union
from typing import TypeAlias

import aiopki
import fastapi
import pydantic

from oauthx.lib.types import GrantType
from oauthx.lib.types import NullRedirectURI
from oauthx.lib.types import ResponseType
from .fragmentresponsemode import FragmentResponseMode
from .queryresponsemode import QueryResponseMode


__all__: list[str] = ['ResponseMode']


ResponseModeType: TypeAlias = Union[
    FragmentResponseMode,
    QueryResponseMode
]


class ResponseMode(pydantic.RootModel[ResponseModeType]):
    _signer: aiopki.CryptoKeyType

    @property
    def grant_type(self) -> GrantType | None:
        return self.root.grant_type

    @property
    def response_type(self) -> ResponseType:
        return self.root.response_type # type: ignore

    def can_redirect(self) -> bool:
        return not isinstance(self.root.redirect_uri, NullRedirectURI)

    def grants(self) -> GrantType | None:
        return self.grant_type

    def get_token_types(self) -> set[str]:
        return self.root.get_token_types()

    def with_signer(self, signer: aiopki.CryptoKeyType):
        self._signer = signer
        return self

    async def deny(self) -> str:
        return await self.root.deny()

    async def error(
        self,
        *,
        error: str,
        error_description: str | None = None,
        error_uri: str | None = None
    ) -> str:
        return await self.root.error(
            error=error,
            error_description=error_description,
            error_uri=error_uri,
        )

    async def redirect(self, **kwargs: Any) -> fastapi.responses.RedirectResponse:
        return await self.root.redirect(self._signer, **kwargs)

    def __str__(self) -> str:
        return self.root.response_mode