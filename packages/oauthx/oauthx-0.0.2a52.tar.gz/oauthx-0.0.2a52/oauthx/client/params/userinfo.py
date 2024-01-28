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

from oauthx.lib.params import HTTPClient
from oauthx.lib.responses import UserInfoResponse
from .bearertoken import BearerToken
from .provider import Provider


__all__: list[str] = ['UserInfo']


async def get(provider: Provider, token: BearerToken, http: HTTPClient) -> UserInfoResponse:
    return await provider.userinfo(token, http)


UserInfo: TypeAlias  = Annotated[UserInfoResponse, fastapi.Depends(get)]