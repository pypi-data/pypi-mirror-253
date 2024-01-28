# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Callable
from typing import TypeVar

from canonical.protocols import ICache


T = TypeVar('T')


class MemoryCache(ICache):
    __module__: str = 'oauthx.lib'
    objects: dict[str, Any] = {}
    
    def __init__(self) -> None:
        self.objects = MemoryCache.objects

    async def get(
        self,
        key: str,
        decoder: Callable[[bytes], T] = bytes
    ) -> T | None:
        value = self.objects.get(key)
        if value is not None:
            return decoder(value)

    async def set(
        self,
        key: str,
        value: Any,
        encoder: Callable[..., bytes] = bytes,
        encrypt: bool = False
    ) -> None:
        self.objects[key] = encoder(value)