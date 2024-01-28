# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Generic
from typing import TypeAlias
from typing import TypeVar

from .iclient import IClient
from .iclientauthorizationstate import IClientAuthorizationState
from .iobtainedcredential import IObtainedCredential


C = TypeVar('C', bound=IClient)
S = TypeVar('S', bound=IClientAuthorizationState)
T = TypeVar('T', bound=IObtainedCredential)


class IClientStorage(Generic[C, S, T]):
    __module__: str = 'oauthx.client.protocols'

    async def delete(self, obj: C | S| T) -> None: ...
    async def get_client(self, client_id: str) -> C: ...
    async def get_credential(self, client_id: str, resource: str | None = None) -> T | None: ... 
    async def get_state(self, state: str) -> S | None: ...
    async def persist(self, obj: C | S | T) -> None: ...


ClientStorageType: TypeAlias = IClientStorage[
    IClient,
    IClientAuthorizationState,
    IObtainedCredential
]