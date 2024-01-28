# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Any
from typing import Literal

import pydantic

from oauthx.server.protocols import ISubject
from oauthx.lib.types import MaskedPrincipal
from oauthx.lib.types import OIDCIssuerIdentifier


class BasePrincipal(pydantic.BaseModel):
    active: bool = pydantic.Field(
        default=True
    )

    allow_login: bool = pydantic.Field(
        default=True
    )

    blocked: bool = pydantic.Field(
        default=False
    )

    issuer: Literal['self'] | OIDCIssuerIdentifier = pydantic.Field(
        default=...
    )

    kind: Any = pydantic.Field(
        default=...
    )

    masked: MaskedPrincipal = pydantic.Field(
        default=...
    )

    registered: datetime.datetime = pydantic.Field(
        default=...
    )
    
    owner: int | str = pydantic.Field(
        default=...
    )
    
    verified: bool = pydantic.Field(
        default=False
    )

    value: Any

    def to_bytes(self) -> bytes:
        raise NotImplementedError

    async def encrypt(self, subject: ISubject) -> None:
        self.value = await subject.encrypt(bytes(self))

    def __bytes__(self) -> bytes:
        return self.to_bytes()