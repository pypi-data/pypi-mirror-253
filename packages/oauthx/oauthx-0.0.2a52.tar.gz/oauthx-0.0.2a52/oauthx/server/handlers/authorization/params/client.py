# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import cast
from typing import Annotated
from typing import TypeAlias

import fastapi

from oauthx.lib.exceptions import UnknownClient
from oauthx.server.params import Storage
from oauthx.server.models import ClientKey
from oauthx.server.protocols import IRegisteredClient
from oauthx.server.request import Request
from oauthx.server.types import MissingRedirectURI
from .query import CLIENT_ID


__all__: list[str] = ['Client']


async def get(
    request: Request,
    storage: Storage,
    client_id: str = CLIENT_ID,
) -> IRegisteredClient:
    client = cast(IRegisteredClient | None, await storage.get(ClientKey(client_id)))
    if client is None:
        raise UnknownClient("The client_id parameter specifies an invalid client.")
    if not client.has_redirection_endpoints():
        raise MissingRedirectURI
    request.set_client(client.root) # type: ignore
    return client.root # type: ignore


Client: TypeAlias = Annotated[
    IRegisteredClient,
    fastapi.Depends(get)
]