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

import fastapi

from oauthx.lib.protocols import IClient
from oauthx.lib.protocols import IStorage


class IAuthorizationRequest(Protocol):
    __module__: str = 'oauthx.server.types'
    
    @property
    def pk(self) -> Any: ...
    
    def add_to_template_context(self, request: fastapi.Request, context: dict[str, Any]) -> None: ...
    async def get_client(self, storage: IStorage) -> IClient: ...
    async def get_context(self, storage: IStorage) -> Any: ...
    async def deny(self, client: IClient, exception: bool = False) -> str: ...
    async def redirect(self, client: IClient, **params: Any) -> fastapi.Response: ...