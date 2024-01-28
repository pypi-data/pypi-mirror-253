# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Annotated
from typing import TypeAlias

import fastapi

from oauthx.server.models import ClientType
from oauthx.server.models import ClientKey
from oauthx.server.params import Storage
from oauthx.server.request import Request
from .query import CLIENT_ID


__all__: list[str] = ['Client']


async def get(
    request: Request,
    storage: Storage,
    client_id: str | None = CLIENT_ID
) -> ClientType | None:
    if client_id is None:
        return None
    client = await storage.get(ClientKey(client_id))
    if client is None:
        return None
    request.set_client(client)
    return client.root # type: ignore


Client: TypeAlias = Annotated[
    ClientType | None,
    fastapi.Depends(get)
]