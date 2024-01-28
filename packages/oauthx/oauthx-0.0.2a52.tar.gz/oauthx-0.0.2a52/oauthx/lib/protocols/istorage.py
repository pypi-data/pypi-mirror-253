# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import contextlib
from typing import Any
from typing import AsyncGenerator
from typing import AsyncIterable
from typing import Iterable
from typing import Protocol
from typing import TypeAlias
from typing import TypeVar

from canonical import ResourceIdentifier
import pydantic

from oauthx.lib.types import Masked


P = TypeVar('P', bound=pydantic.BaseModel)
T = TypeVar('T')


class IStorage(Protocol):
    __module__: str = 'oauthx.lib.protocols'
    Findable: TypeAlias = type[P]

    def find(
        self,
        kind: type[P],
        filters: Iterable[tuple[str, str, Any]],
        sort: Iterable[str] | None = None
    ) -> AsyncIterable[P]:
        """Find objects by the given filters."""
        ...

    async def allocate_identifier(self, cls: str | type) -> Any: ...
    async def delete(self, obj: Any) -> None: ...
    async def get(self, key: ResourceIdentifier[Any, T]) -> T | None: ...
    async def mask(self, obj: Any) -> Masked: ...
    async def persist(self, object: Any) -> None: ...

    @contextlib.asynccontextmanager
    async def atomic(self, key: ResourceIdentifier[Any, T]) -> AsyncGenerator[T | None, None]:
        obj = await self.get(key)
        try:
            yield obj
            await self.persist(obj)
        except Exception:
            pass