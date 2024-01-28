# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Union

import pydantic
from aiopki.types import EncryptionResult
from aiopki.types import SubjectID
from canonical import EmailAddress
from canonical import Phonenumber

from oauthx.lib.types import MaskedPrincipal
from oauthx.server.protocols import ISubject
from .emailprincipal import EmailPrincipal
from .phonenumberprincipal import PhonenumberPrincipal
from .subjectkey import SubjectKey
from .subjectidentifierprincipal import SubjectIdentifierPrincipal


__all__: list[str] = [
    'PrincipalType',
    'PrincipalValueType',
    'Principal'
]


PrincipalType = Union[
    EmailPrincipal,
    PhonenumberPrincipal,
    SubjectIdentifierPrincipal
]


PrincipalValueType = Union[
    EmailAddress,
    Phonenumber,
    SubjectID
]


class Principal(pydantic.RootModel[PrincipalType]):

    @property
    def kind(self) -> str:
        return self.root.kind

    @property
    def masked(self) -> MaskedPrincipal:
        return self.root.masked

    @property
    def owner(self) -> SubjectKey:
        return SubjectKey(str(self.root.owner))

    @property
    def value(self) -> PrincipalValueType:
        assert not isinstance(self.root.value, EncryptionResult)
        return self.root.value

    def is_encrypted(self) -> bool:
        return isinstance(self.root.value, EncryptionResult)

    def is_owned_by(self, sub: SubjectKey) -> bool:
        """Return a boolean indicating if the subject identified by the
        key owns this principal.
        """
        return sub == self.owner

    def is_verified(self) -> bool:
        return self.root.verified

    async def encrypt(self, subject: ISubject) -> None:
        await self.root.encrypt(subject)