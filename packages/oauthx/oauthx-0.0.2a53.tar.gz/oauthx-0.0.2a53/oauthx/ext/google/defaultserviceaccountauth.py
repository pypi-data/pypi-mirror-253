# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import datetime
import logging
from typing import cast
from typing import AsyncGenerator

from aiopki.ext import jose
from aiopki.ext.jose import JWT
import google.oauth2.id_token
import google.auth.transport.requests

import httpx


class DefaultServiceAccountAuth(httpx.Auth):
    audience: str | None = None
    bearer: str | None = None
    logger: logging.Logger = logging.getLogger('uvicorn')
    token: JWT | None = None

    def __init__(self, audience: str | None = None):
        self.audience = audience
        self.loop = asyncio.get_running_loop()

    async def async_auth_flow(
        self,
        request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        now = datetime.datetime.now(datetime.timezone.utc)\
            - datetime.timedelta(seconds=30)
        if self.token is None or not self.token.validate_exp(now=now):
            self.bearer, self.token = await self.get_id_token(request)
        request.headers['Authorization'] = f'Bearer {self.bearer}'
        yield request

    async def get_id_token(self, request: httpx.Request) -> tuple[str, JWT]:
        audience = self.audience or f'{request.url.scheme}://{request.url.netloc.decode()}'
        self.logger.info(
            "Obtaining OIDC ID Token using default credentials"
            " (audience: %s)",
            audience
        )
        result = await self.loop.run_in_executor( # type: ignore
            None,
            google.oauth2.id_token.fetch_id_token, # type: ignore
            google.auth.transport.requests.Request(),
            audience
        )
        jws = jose.parse(result)
        return cast(str, result), jws.payload(JWT.model_validate)