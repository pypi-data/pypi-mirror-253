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

from oauthx.lib.params import Logger
from oauthx.server.types import AuthorizationRequestKey
from oauthx.server.types import IAuthorizationRequest
from oauthx.server.types import StopSnooping
from .storage import Storage


__all__: list[str] = ['PendingAuthorizationRequest']


async def get(
    logger: Logger,
    storage: Storage,
    pk: AuthorizationRequestKey = fastapi.Path(...)
) -> IAuthorizationRequest:
    request = await storage.get(pk)
    if request is None:
        logger.debug("Authorization request does not exist (id: %s)", int(pk))
        raise StopSnooping
    return request
    

PendingAuthorizationRequest: TypeAlias =  Annotated[IAuthorizationRequest, fastapi.Depends(get)]