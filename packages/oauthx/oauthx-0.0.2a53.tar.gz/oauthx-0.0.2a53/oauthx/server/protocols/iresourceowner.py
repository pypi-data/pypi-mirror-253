# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import AsyncContextManager
from typing import Callable
from typing import Protocol

from canonical import ResourceIdentifier


class IResourceOwner(Protocol):
    sub: str

    class Key(ResourceIdentifier[str, 'IResourceOwner']):
        client_id: str
        openapi_example: str = 'clients/client-123/resourceOwners/123'
        openapi_title: str = 'Resource Owner ID'

        def __init__(self, client_id: str, sub: str):
            self.client_id = client_id
            self.sub = sub
        
        def __eq__(self, key: object) -> bool:
            return isinstance(key, type(self)) and all([
                self.client_id == key.client_id,
                self.sub == key.sub
            ])

        def __str__(self) -> str:
            return f'{self.client_id}/{self.sub}'
        
        def __hash__(self) -> int:
            return hash((self.client_id, self.sub))
        
    @property
    def pk(self) -> Key: ...

    def atomic(self) -> AsyncContextManager[None]: ...
    def consent(self, scope: set[str]) -> None: ...
    def grants_consent(self, scope: set[str]) -> bool: ...
    def update_key(self, update: Callable[[bytes], None]): ...