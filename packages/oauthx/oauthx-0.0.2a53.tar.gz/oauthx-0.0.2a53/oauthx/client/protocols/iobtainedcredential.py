# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Protocol

import httpx

from .iclient import IClient


class IObtainedCredential(Protocol):
    __module__: str = 'oauthx.client.protocols'

    @property
    def pk(self) -> str:
        ...

    def add_to_request(self, request: httpx.Request) -> None:
        ...

    async def destroy(self) -> None:
        ...

    async def refresh(self, client: IClient):
        ...