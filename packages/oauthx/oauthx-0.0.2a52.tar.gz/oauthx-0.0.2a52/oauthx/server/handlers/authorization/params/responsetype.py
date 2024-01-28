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
from oauthx.lib.types import ResponseType as ResponseType_
from .pushedauthorizationrequest import PushedAuthorizationRequest
from .query import RESPONSE_TYPE


__all__: list[str] = [
    'ResponseType'
]


async def get(
    params: PushedAuthorizationRequest,
    response_type: ResponseType_ | None = RESPONSE_TYPE,
) -> ResponseType_ | None:
    if params and response_type:
        raise InvalidRequest(
            "The response_type parameter must not be included if the "
            "request or request_uri parameters are present."
        )
    if params:
        response_type = params.response_type
    return response_type


ResponseType: TypeAlias = Annotated[
    ResponseType_ | None,
    fastapi.Depends(get)
]