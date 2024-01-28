# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import dataclasses
from typing import Annotated
from typing import TypeAlias

import fastapi
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials

from oauthx.lib.exceptions import InvalidRequest
from oauthx.server.models import ClientKey
from oauthx.server.models import ClientType
from .query import CLIENT_ID
from .query import CLIENT_SECRET


__all__: list[str] = ['ClientCredentials']


@dataclasses.dataclass
class ClientSecret:
    client_id: ClientKey
    client_secret: str | None

    async def authenticate(self, client: ClientType) -> bool:
        return all([
            client.id == str(self.client_id),
            await client.authenticate(self.client_secret)
        ])


async def get(
    credentials: HTTPBasicCredentials | None = fastapi.Depends(HTTPBasic(auto_error=False)),
    client_id: str | None = CLIENT_ID,
    client_secret: str | None = CLIENT_SECRET,
) -> ClientSecret | None:
    if credentials and (client_id or client_secret):
        raise InvalidRequest(
            "Multiple mechanisms for client authentication "
            "provided."
        )
    if not credentials and not client_id:
        return None
    if credentials:
        client_id = credentials.username
        client_secret = credentials.password
    assert client_id
    return ClientSecret(ClientKey(client_id), client_secret)


ClientCredentials: TypeAlias = Annotated[
    ClientSecret | None,
    fastapi.Depends(get)
]