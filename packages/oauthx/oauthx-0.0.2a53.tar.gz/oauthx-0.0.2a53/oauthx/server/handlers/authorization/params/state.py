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

from oauthx.lib.exceptions import InvalidRequest
from .client import Client
from .pushedauthorizationrequest import PushedAuthorizationRequest
from .query import STATE


__all__: list[str] = [
    'State'
]


async def get_state(
    client: Client,
    params: PushedAuthorizationRequest,
    state: str | None = STATE,
) -> str | None:
    if params and state:
        raise InvalidRequest(
            "The state parameter must not be included if the "
            "request or request_uri parameters are present."
        )
    if params:
        state = params.state
    return state


StateDependency: str | None = fastapi.Depends(get_state)
State: TypeAlias = Annotated[str | None, StateDependency]