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
from oauthx.lib.types import TargetResource
from .pushedauthorizationrequest import PushedAuthorizationRequest
from .query import RESOURCES


__all__: list[str] = [
    'TargetResources'
]


async def get(
    params: PushedAuthorizationRequest,
    resources: set[TargetResource] | None = RESOURCES,
) -> set[TargetResource]:
    if params and resources:
        raise InvalidRequest(
            "The resource parameter must not be included if the "
            "request or request_uri parameters are present."
        )
    if params:
        resources = params.resources
    return resources or set()


TargetResources: TypeAlias = Annotated[
    set[str],
    fastapi.Depends(get)
]