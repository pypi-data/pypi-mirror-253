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

from oauthx.lib.exceptions import StopSnooping
from oauthx.client.protocols import IClientAuthorizationState
from .clientstorage import ClientStorage
from .query import STATE


__all__: list[str] = ['ClientAuthorizationState']


async def get(
    storage: ClientStorage,
    state: str | None = STATE
) -> IClientAuthorizationState | None:
    if state is None:
        return None
    obj = await storage.get_state(state)
    if obj is None:
        raise StopSnooping
    return obj


ClientAuthorizationState: TypeAlias = Annotated[
    IClientAuthorizationState | None,
    fastapi.Depends(get)
]