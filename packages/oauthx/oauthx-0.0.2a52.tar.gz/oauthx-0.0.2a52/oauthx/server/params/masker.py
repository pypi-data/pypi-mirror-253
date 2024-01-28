# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import base64
import functools
from typing import Annotated
from typing import Any
from typing import Callable
from typing import TypeAlias
from typing import TypeVar

import fastapi
from aiopki.types import SubjectID
from canonical import EmailAddress
from canonical import Phonenumber

from oauthx.lib.types import MaskedPrincipal
from oauthx.server.models import PrincipalValueType
from .datamaskingkey import DataMaskingKey


T = TypeVar('T')


class _Masker:
    __module__: str = 'oauthx.types'
    
    def __init__(self, key: DataMaskingKey):
        self.key = key

    @functools.singledispatchmethod
    async def mask(
        self,
        value: PrincipalValueType | bytes | str,
        factory: Callable[[str], T] = MaskedPrincipal
    ) -> T:
        if isinstance(value, (bytes, str)):
            if isinstance(value, str):
                value = str.encode(value)
            sig = await self.key.sign(value)
            return factory(bytes.decode(base64.urlsafe_b64encode(sig)))
        raise NotImplementedError(type(value).__name__)

    @mask.register
    async def _(self, value: EmailAddress, factory: Any = MaskedPrincipal) -> Any:
        return await self.mask(f'email:{str(str.lower(value))}', factory=factory)

    @mask.register
    async def _(self, value: Phonenumber, factory: Any = MaskedPrincipal) -> Any:
        return await self.mask(f'phone:{str(str.lower(value))}', factory=factory)

    @mask.register
    async def _(self, value: SubjectID, factory: Any = MaskedPrincipal) -> Any:
        return await self.mask(f'sub:{value.iss}/{value.sub}', factory=factory)


Masker: TypeAlias = Annotated[_Masker, fastapi.Depends(_Masker)]