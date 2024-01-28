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
import fastapi.params
from canonical.exceptions import ProgrammingError

from oauthx.server.types import StopSnooping
from oauthx.lib.params import Storage
from oauthx.server.models import ClientKey
from oauthx.server.models import ClientType
from oauthx.server.params import ClientAuthorizationState
from oauthx.server.request import Request


__all__: list[str] = [
    'ClientDependency',
    'Client'
]


async def get(
    request: Request,
    state: ClientAuthorizationState,
    storage: Storage
) -> ClientType:
    if state is None:
        raise StopSnooping
    client_id = state.annotation('client-id', decoder=ClientKey)
    if client_id is None:
        raise ProgrammingError(
            "The ClientAuthorizationState instance must be annotated with "
            "the 'client-id' annotation, point to an existing OAuth 2.x/"
            "OpenID Connect client."
        )
    client = await storage.get(client_id)
    if client is None:
        raise StopSnooping
    request.set_client(client.root) # type: ignore
    return client.root # type: ignore


ClientDependency: fastapi.params.Depends = fastapi.Depends(get)
Client: TypeAlias = Annotated[ClientType, ClientDependency]
