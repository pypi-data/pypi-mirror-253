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
from typing import MutableMapping
from typing import TypeAlias
from typing import Union
from typing_extensions import Literal

import pydantic
from aiopki.types import EncryptionResult
from aiopki.types import ISigner

from oauthx.server.protocols import ISubject
from .birthdate import BirthdateClaim
from .email import EmailClaim
from .gender import GenderClaim
from .name import NameClaim
from .phonenumber import PhonenumberClaim
from .stringclaim import StringClaim


__all__: list[str] = ['Claim']


ClaimType: TypeAlias = Union[
    BirthdateClaim,
    EmailClaim,
    GenderClaim,
    NameClaim,
    PhonenumberClaim,
    StringClaim,
]


class Claim(pydantic.RootModel[ClaimType]):

    @classmethod
    def new(
        cls,
        *,
        receipt_id: int,
        id: int,
        kind: Literal['email', 'gender', 'name'],
        provider: str,
        issuer: str,
        sub: int,
        value: Any,
        now: datetime.datetime | None = None,
        ial: int = 0
    ):
        """Create a new :class:`Claim` instance using an
        Open ID Connect ID Token.
        """
        return cls.model_validate({
            'ial': ial,
            'id': id,
            'issuer': issuer,
            'kind': kind,
            'obtained': now or datetime.datetime.now(datetime.timezone.utc),
            'provider': provider,
            'receipt_id': receipt_id,
            'sub': sub,
            'value': value,
        })

    @property
    def pk(self) -> int:
        return self.root.id

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        self.root.contribute_to_userinfo(userinfo)

    def is_encrypted(self) -> bool:
        """Return a boolean indicating if the claim is encrypted."""
        return isinstance(self.root.value, EncryptionResult)

    def is_masked(self) -> bool:
        """Return a boolean indicating if the claim is masked."""
        return self.root.is_masked()

    async def decrypt(self, subject: ISubject) -> None:
        """Decrypt the claim using the owners' private key."""
        return await self.root.decrypt(subject)

    async def encrypt(self, subject: ISubject) -> None:
        """Encrypt the claim using the owners' private key."""
        await self.root.encrypt(subject)

    async def mask(self, key: ISigner) -> None:
        """Use `key` to create a masked and set the :class:`BaseClaim.masked`
        attribute.
        """
        await self.root.mask(key)