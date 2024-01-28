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

from oauthx.lib.params import DefaultCache
from oauthx.resource.models import Request
from oauthx.resource.models import TokenSubject
from .accesstoken import AccessToken
from .requestcredentials import RequestCredentials


async def get(
    request: Request,
    at: AccessToken,
    cache: DefaultCache,
    credentials: RequestCredentials
) -> TokenSubject:
    subject = await cache.get(request.at_hash, decoder=TokenSubject.model_validate_json)
    if subject is None:
        userinfo = await request.issuer.userinfo(credentials)
        subject = TokenSubject.model_validate({
            'claims': userinfo.model_dump(
                exclude={'aud', 'iss', 'exp', 'iat', 'nbf', 'sub'},
                exclude_none=True
            ),
            'sub': at.sub,
            'at_hash': request.at_hash
        })
        await cache.set(request.at_hash, subject.model_dump_json(), encoder=str.encode)
    return subject


RequestSubject: TypeAlias = Annotated[TokenSubject, fastapi.Depends(get)]