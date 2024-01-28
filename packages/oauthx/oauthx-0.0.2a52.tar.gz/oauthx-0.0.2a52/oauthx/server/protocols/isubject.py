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
from typing import Protocol

from aiopki.types import EncryptionResult
from aiopki.types import IDecrypter
from aiopki.types import IEncrypter
from aiopki.types import ISigner
from aiopki.types import Plaintext
from aiopki.ext.jose import OIDCToken
from canonical import ResourceIdentifier


class ISubject(Protocol):
    """Specifies the interface of a model that represents a
    :term:`Subject`
    """
    __module__: str = 'oauthx.types'

    def is_authenticated(self) -> bool:
        ...

    def is_encrypted(self) -> bool:
        ...

    async def decrypt_keys(self, key: IDecrypter) -> None:
        """Decrypt the subjects' encryption keys using the
        storage encryption key.
        """
        ...

    async def encrypt_keys(self, key: IEncrypter) -> None:
        """Encrypt the subjects' encryption keys using the
        storage encryption key.
        """
        ...

    async def decrypt(self, value: EncryptionResult) -> Plaintext:
        ...

    async def encrypt(self, value: bytes) -> EncryptionResult:
        ...

    async def mask(self, value: bytes) -> str:
        ...

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        ...

    def get_primary_key(self) -> ResourceIdentifier[int | str, 'ISubject']:
        """Return the primary key of the :class:`ISubject`."""
        ...

    def get_masking_key(self) -> ISigner:
        ...

    def update_from_oidc(self, token: OIDCToken) -> None:
        ...