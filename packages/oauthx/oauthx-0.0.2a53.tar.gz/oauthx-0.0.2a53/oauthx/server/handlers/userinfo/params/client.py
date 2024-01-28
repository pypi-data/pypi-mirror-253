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

from oauthx.lib.exceptions import InvalidToken
from oauthx.resource import AccessToken
from oauthx.server.params import Storage
from oauthx.server.protocols import IRegisteredClient


async def get(at: AccessToken, storage: Storage) -> IRegisteredClient:
    client = await storage.get(at.client_id)
    if client is None:
        raise InvalidToken("The client is disabled.")
    return client


Client: TypeAlias = Annotated[IRegisteredClient, fastapi.Depends(get)]

