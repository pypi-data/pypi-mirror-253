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

from oauthx.lib.types import GrantType as GrantType_
from oauthx.server.types import UnauthorizedClient
from .client import Client
from .query import GRANT_TYPE


__all__: list[str] = [
    'GrantType'
]


async def get(
    client: Client,
    grant_type: GrantType_ = GRANT_TYPE
) -> GrantType_:
    if client is not None and not client.can_grant(grant_type):
        raise UnauthorizedClient
    return grant_type


GrantType: TypeAlias = Annotated[
    GrantType_,
    fastapi.Depends(get)
]