# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import logging
from typing import Any
from typing import AsyncGenerator

import httpx

from oauthx.client.exceptions import AuthorizationRequired
from oauthx.client.protocols import IClient
from oauthx.client.protocols import IClientAuthorizationState
from oauthx.client.protocols import IClientStorage
from oauthx.client.protocols import IObtainedCredential


class AuthorizationCodeCredential(httpx.Auth):
    client: IClient | None
    credential: IObtainedCredential | None
    lock: asyncio.Lock = asyncio.Lock()
    logger: logging.Logger = logging.getLogger('uvicorn')
    name: str
    storage: IClientStorage[IClient, IClientAuthorizationState, IObtainedCredential]

    def __init__(self, storage: Any, name: str):
        self.storage = storage
        self.client = None
        self.credential = None
        self.name = name

    def get_credential_name(self) -> str:
        return self.name

    async def async_auth_flow(self, request: httpx.Request) -> AsyncGenerator[
        httpx.Request,
        httpx.Response,
    ]:
        if self.client is None:
            self.logger.info("Retrieving OAuth 2.x/OpenID Connect client (client: %s)", self.name)
            self.client = await self.storage.get_client(self.name)
        async with self.lock:
            if self.credential is None:
                self.logger.info("Retrieving credential (client: %s)", self.name)
                credential = await self.get_credential()
                if credential is None:
                    raise AuthorizationRequired
                self.credential = credential
        self.credential.add_to_request(request)
        response = yield request
        if response.status_code == 401:
            await self.refresh()
            self.credential.add_to_request(request)
            response = yield request
            if response.status_code == 401:
                await self.credential.destroy()
                self.credential = None
                self.logger.critical("Authorization required (client: %s)", self.name)
                raise AuthorizationRequired

    async def get_credential(self) -> IObtainedCredential | None:
        return  await self.storage.get_credential(self.get_credential_name())

    async def refresh(self) -> None:
        assert self.client is not None
        assert self.credential is not None
        async with self.lock:
            self.logger.info("Refreshing access token (client: %s)", self.name)
            await self.credential.refresh(self.client)
            await self.storage.persist(self.credential)