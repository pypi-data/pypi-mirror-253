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

from oauthx.client.protocols import IClient
from .clientstorage import ClientStorage


__all__: list[str] = ['Client']


async def get(
    request: fastapi.Request,
    storage: ClientStorage
) -> IClient:
    return await storage.get_client(getattr(request.state, 'oauth_active_client'))


Client: TypeAlias  = Annotated[IClient, fastapi.Depends(get)]