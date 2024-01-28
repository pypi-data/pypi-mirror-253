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

from oauthx.server.models import Authorization as AuthorizationModel
from oauthx.server.models import SubjectKey
from oauthx.server.params import ObjectFactory
from oauthx.server.params import RequestSession
from oauthx.server.params import Storage
from .authorizationrequest import AuthorizationRequest
from .client import Client
from .responsemode import ResponseMode
from .userinfo import UserInfo


__all__: list[str] = [
    'Authorization'
]


async def get(
    factory: ObjectFactory,
    storage: Storage,
    session: RequestSession,
    client: Client,
    params: AuthorizationRequest,
    response_mode: ResponseMode,
    userinfo: UserInfo
) -> AuthorizationModel:
    authorization = await factory.authorization(
        request=params,
        client_id=client.id,
        lifecycle='GRANTED',
        scope=params.scope,
        sub=SubjectKey(userinfo.sub),
        token_types=response_mode.get_token_types(),
        contributors=[params, session]
    )
    await authorization.persist()
    await storage.delete(params)
    return authorization

Authorization: TypeAlias = Annotated[AuthorizationModel, fastapi.Depends(get)]