# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import AsyncGenerator
from typing import Annotated
from typing import TypeAlias

import fastapi
import httpx


__all__: list[str] = ['HTTPClientDependency']


async def get(request: fastapi.Request) -> AsyncGenerator[httpx.AsyncClient, None]:
    if getattr(request, 'http', None) is not None:
        yield getattr(request, 'http')
    else:
        client = httpx.AsyncClient()
        try:
            await client.__aenter__()
            yield client
        finally:
            await client.__aexit__(None, None, None)



HTTPClientDependency: httpx.AsyncClient = fastapi.Depends(get)
HTTPClient: TypeAlias = Annotated[httpx.AsyncClient, HTTPClientDependency]