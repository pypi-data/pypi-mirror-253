# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
from typing import Any
from typing import Callable
from typing import Literal
from typing import MutableMapping
from typing import TypeVar

import pydantic
from aiopki.ext.jose import OIDCToken
from aiopki.lib import JSONWebKey
from aiopki.types import IDecrypter
from aiopki.types import IEncrypter
from aiopki.types import EncryptionResult
from aiopki.types import Plaintext
from aiopki.utils import b64encode

from .subjectkey import SubjectKey


R = TypeVar('R')


class Subject(pydantic.BaseModel):
    active: bool = pydantic.Field(
        default=True
    )    

    dek: EncryptionResult | JSONWebKey = pydantic.Field(
        default=...
    )

    dmk: EncryptionResult | JSONWebKey = pydantic.Field(
        default=...
    )

    kind: Literal['User'] = pydantic.Field(
        default=...
    )

    locale: str = pydantic.Field(
        default='nl-NL'
    )

    sub: int = pydantic.Field(
        default=...
    )

    use: Literal['personal', 'institutional'] = pydantic.Field(
        default=...
    )

    zoneinfo: str = pydantic.Field(
        default='Europe/Amsterdam'
    )

    @staticmethod
    def requires_decryption(func: Callable[..., R]) -> Callable[..., R]:
        @functools.wraps(func)
        def f(self: 'Subject', *args: Any, **kwargs: Any) -> Any:
            if self.is_encrypted():
                raise TypeError(
                    f"{type(self).__name__} must be decrypted prior to calling "
                    f"{func.__name__}()."
                )
            return func(self, *args, **kwargs)
        return f

    @requires_decryption
    def get_masking_key(self) -> JSONWebKey:
        assert isinstance(self.dmk, JSONWebKey)
        return self.dmk

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        userinfo['locale'] = self.locale
        userinfo['zoneinfo'] = self.zoneinfo

    def get_primary_key(self) -> SubjectKey:
        return SubjectKey(str(self.sub))

    def is_authenticated(self) -> bool:
        return True

    def is_encrypted(self) -> bool:
        return any([
            isinstance(self.dek, EncryptionResult),
            isinstance(self.dmk, EncryptionResult),
        ])

    def update_from_oidc(self, token: OIDCToken) -> None:
        if token.locale:
            self.locale = token.locale
        if token.zoneinfo:
            self.zoneinfo = token.zoneinfo

    @requires_decryption
    async def decrypt(self, ct: EncryptionResult) -> Plaintext:
        assert not isinstance(self.dek, EncryptionResult)
        return await self.dek.decrypt(ct)

    @requires_decryption
    async def encrypt(self, value: bytes) -> EncryptionResult:
        assert not isinstance(self.dek, EncryptionResult)
        return await self.dek.encrypt(value)

    async def decrypt_keys(self, key: IDecrypter) -> None:
        """Decrypt the subjects' encryption keys using the
        storage encryption key.
        """
        if not isinstance(self.dek, JSONWebKey):
            assert isinstance(self.dek, EncryptionResult)
            assert isinstance(self.dmk, EncryptionResult)
            self.dek = JSONWebKey.model_validate_json(
                bytes.decode(bytes(await key.decrypt(self.dek)))
            )
            self.dmk = JSONWebKey.model_validate_json(
                bytes.decode(bytes(await self.dek.decrypt(self.dmk)))
            )

    async def encrypt_keys(self, key: IEncrypter) -> None:
        """Encrypt the subjects' encryption keys using the
        storage encryption key.
        """
        if isinstance(self.dek, JSONWebKey):
            assert not isinstance(self.dek, EncryptionResult)
            assert not isinstance(self.dmk, EncryptionResult)
            self.dmk = await self.dek.encrypt(
                str.encode(self.dmk.model_dump_json(exclude_none=True))
            )
            self.dek = await key.encrypt(
                str.encode(self.dek.model_dump_json(exclude_none=True))
            )

    @requires_decryption
    async def mask(self, value: bytes) -> str:
        assert isinstance(self.dmk, JSONWebKey)
        return b64encode(await self.dmk.sign(value), encoder=bytes.decode)