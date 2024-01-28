# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import functools
from typing import Any
from typing import Callable
from typing import Literal
from typing import MutableMapping
from typing import TypeVar

import pydantic
from aiopki.types import EncryptionResult
from aiopki.types import ISigner
from aiopki.utils import b64encode

from oauthx.lib.types import Masked
from oauthx.lib.types import Unmasked
from oauthx.lib.types import OIDCIssuerIdentifier
from oauthx.server.protocols import ISubject


R = TypeVar('R')
T = TypeVar('T', bound='BaseClaim')


class BaseClaim(pydantic.BaseModel):
    """The base class for all claim implementations. A :term:`Claim`
    is an assertion about a :term:`Subject`; it represents an attribute
    of the identified user.
    """
    id: int = pydantic.Field(
        default=...
    )

    ial: int = pydantic.Field(
        default=0
    )

    issuer: Literal['self'] | OIDCIssuerIdentifier = pydantic.Field(
        default='self'
    )

    kind: Any = pydantic.Field(
        default=...
    )

    masked: Masked = pydantic.Field(
        default_factory=Unmasked
    )

    obtained: datetime.datetime = pydantic.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    provider: Literal['self'] | OIDCIssuerIdentifier = pydantic.Field(
        default=...
    )

    sub: int = pydantic.Field(
        default=...
    )

    receipt_id: int = pydantic.Field(
        default=...
    )

    value: Any

    @property
    def key(self) -> tuple[str, str, str]:
        return (
            str(self.issuer),
            str(self.provider),
            str(self.kind)
        )

    @staticmethod
    def requires_decryption(func: Callable[..., R]) -> Callable[..., R]:
        @functools.wraps(func)
        def f(self: 'BaseClaim', *args: Any, **kwargs: Any) -> Any:
            if self.is_encrypted():
                raise TypeError(
                    f"{type(self).__name__} must be decrypted prior to calling "
                    f"{func.__name__}()."
                )
            return func(self, *args, **kwargs)
        return f

    @pydantic.field_serializer('value', mode='plain', when_used='always')
    def dump_model(self, value: EncryptionResult, _: Any) -> dict[str, Any]:
        return value.root.model_dump(mode='json')

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        userinfo[self.kind] = self.get_value()

    def decode_plaintext(self, pt: bytes) -> Any:
        obj = self.model_validate({
            **self.model_dump(exclude={'value'}),
            'value': bytes.decode(pt, 'utf-8')
        })
        return obj.value

    def get_encryption_input(self) -> bytes:
        raise NotImplementedError

    def get_masking_input(self) -> bytes:
        raise NotImplementedError

    @requires_decryption
    def get_value(self) -> Any:
        return self.value

    def is_encrypted(self) -> bool:
        return isinstance(self.value, EncryptionResult)

    def is_masked(self):
        return not isinstance(self.masked, Unmasked)

    def set_mask(self, masked: bytes):
        self.masked = Masked(b64encode(masked, encoder=bytes.decode))

    async def decrypt(self, subject: ISubject) -> None:
        if isinstance(self.value, EncryptionResult):
            pt = await subject.decrypt(self.value)
            self.value = self.decode_plaintext(bytes(pt))

    async def encrypt(self, subject: ISubject) -> None:
        """Encrypt the claim using the owners' private key."""
        if not isinstance(self.value, EncryptionResult):
            self.value = await subject.encrypt(self.get_encryption_input())

    @requires_decryption
    async def mask(self, key: ISigner) -> None:
        self.set_mask(await key.sign(self.get_masking_input()))