# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import secrets
from typing import Any
from typing import ClassVar
from typing import Callable

import pydantic
from aiopki.types import Base64

from oauthx.server.protocols import IResourceOwner
from .basemodel import BaseModel
from .subjectkey import SubjectKey


class ResourceOwner(BaseModel):
    Key: ClassVar = IResourceOwner.Key

    blocked: bool = pydantic.Field(
        default=False
    )

    client_id: str  = pydantic.Field(
        default=...
    )

    key: Base64 = pydantic.Field(
        default_factory=lambda: secrets.token_bytes(32)
    )

    sector_identifier: str = pydantic.Field(
        default=...
    )
    
    scope: set[str] = pydantic.Field(
        default_factory=set
    )

    sub: SubjectKey = pydantic.Field(
        default=...
    )

    onboarded: datetime.datetime = pydantic.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    @property
    def pk(self) -> Key:
        return self.Key(self.client_id, str(self.sub))

    def consent(self, scope: set[str]) -> None:
        self.scope |= scope

    def grants_consent(self, scope: set[str]) -> bool:
        return True

    def model_dump_json(self, **kwargs: Any) -> str:
        exclude = kwargs.setdefault('exclude', set())
        exclude.update({
            'claims',
            'principals'
        })
        return super().model_dump_json(**kwargs)

    def update_key(self, update: Callable[[bytes], None]):
        update(self.key)