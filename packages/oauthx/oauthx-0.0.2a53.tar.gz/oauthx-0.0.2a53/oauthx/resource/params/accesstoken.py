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

from oauthx.resource.models import Request
from oauthx.lib import RFC9068AccessToken
from oauthx.lib.exceptions import InvalidRequest


__all__: list[str] = ['AccessToken']


async def get(request: Request) -> RFC9068AccessToken | None:
    at = getattr(request, 'access_token', None)
    if at is None:
        raise InvalidRequest("The Authorization header is required.")
    return at


AccessToken: TypeAlias = Annotated[
    RFC9068AccessToken,
    fastapi.Depends(get)
]