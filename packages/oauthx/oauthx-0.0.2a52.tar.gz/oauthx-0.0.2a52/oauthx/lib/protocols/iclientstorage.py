# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Protocol
from typing import TypeVar

import fastapi
import pydantic

from .iclient import IClient
from .iclientauthorizationstate import IClientAuthorizationState
from .istorage import IStorage


P = TypeVar('P', bound=pydantic.BaseModel)
T = TypeVar('T')


class IClientStorage(IStorage, Protocol):
    __module__: str = 'oauthx.lib.protocols'

    @classmethod
    def inject(cls) -> Any:
        def f(request: fastapi.Request, storage: cls = fastapi.Depends(cls)):
            setattr(request, 'storage', storage)
        return fastapi.Depends(f)

    async def application(self, client_id: str) -> IClient | None: ...
    async def state(self, state: str) -> IClientAuthorizationState | None: ...