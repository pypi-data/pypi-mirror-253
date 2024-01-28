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

from oauthx.server import models
from oauthx.server.params import Storage
from oauthx.server.types import AuthorizationRequestKey
from oauthx.server.types import StopSnooping


__all__: list[str] = [
    'AuthorizationRequest'
]


async def get(
    storage: Storage,
    request_id: AuthorizationRequestKey = fastapi.Query(
        default=...,
        alias='a'
    )
) -> models.AuthorizationRequest | None:
    params = await storage.get(request_id)
    if params is None:
        raise StopSnooping
    return cast(models.AuthorizationRequest, params)


AuthorizationRequest: TypeAlias = Annotated[
    models.AuthorizationRequest | None,
    fastapi.Depends(get)
]