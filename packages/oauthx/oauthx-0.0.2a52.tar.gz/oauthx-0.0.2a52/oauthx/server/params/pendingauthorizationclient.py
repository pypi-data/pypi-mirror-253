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

from oauthx.lib.protocols import IClient
from .pendingauthorizationrequest import PendingAuthorizationRequest
from .storage import Storage


__all__: list[str] = ['PendingAuthorizationClient']


async def get(
    request: PendingAuthorizationRequest,
    storage: Storage
) -> IClient:

    return (await request.get_client(storage)).root # type: ignore
    

PendingAuthorizationClient: TypeAlias =  Annotated[IClient, fastapi.Depends(get)]