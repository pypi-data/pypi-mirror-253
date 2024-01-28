# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
from typing import Any
from typing import Iterable

from oauthx.lib.types import MaskedPrincipal
from .models import PrincipalValueType
from .models import Principal
from .params import Masker
from .params import Storage


class SubjectResolver:
    """Provides an interface to resolve :class:`~oauthx.types.ISubject`
    instances.
    """
    __module__: str = 'oauthx.server'
    storage: Storage

    def __init__(
        self,
        storage: Storage,
        masker: Masker
    ):
        self.masker = masker
        self.storage = storage

    async def mask(self, value: PrincipalValueType | None) -> MaskedPrincipal | None:
        if value is None:
            return None
        return await self.masker.mask(value)

    async def resolve_principal(self, principal: Any) -> Principal | None:
        masked = await self.mask(principal)
        if masked is None:
            return None
        return await self.storage.get(masked)

    async def resolve_principals(
        self,
        principals: Iterable[Any]
    ) -> tuple[Principal | None, ...]:
        """Resolve the given iterable `principals` to :class:`Principal`
        instances.
        """
        principals = await asyncio.gather(*map(self.mask, principals))
        return tuple(await asyncio.gather(*map(self.storage.get, principals)))