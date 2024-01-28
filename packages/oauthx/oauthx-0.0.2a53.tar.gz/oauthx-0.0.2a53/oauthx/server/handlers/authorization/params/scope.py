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
from oauthx.lib.types import ScopeType
from oauthx.server.types import InvalidAuthorizationRequest
from .authorizationcontext import AuthorizationContext
from .client import Client
from .pushedauthorizationrequest import PushedAuthorizationRequest
from .query import ACCESS_TYPE
from .query import SCOPE


__all__: list[str] = [
    'Scope'
]


async def get(
    client: Client,
    context: AuthorizationContext,
    params: PushedAuthorizationRequest,
    access_type: str | None = ACCESS_TYPE,
    scope: str | None = SCOPE,
) -> ScopeType | None:
    requested = None
    if scope and params:
        raise InvalidRequest(
            "The scope parameter must not be included if the "
            "request or request_uri parameters are present."
        )
    if scope is not None:
        requested = ScopeType.fromstring(scope)
    if params:
        requested = params.scope
    if requested and not client.allows_scope(requested):
        raise InvalidAuthorizationRequest(
            error="invalid_scope",
            error_description="The client does not allow the requested scope.",
            context=context
        )
    if access_type == 'offline':
        if requested is None:
            requested = ScopeType()
        requested.add('offline_access')
    return requested


Scope: TypeAlias = Annotated[
    ScopeType | None,
    fastapi.Depends(get)
]