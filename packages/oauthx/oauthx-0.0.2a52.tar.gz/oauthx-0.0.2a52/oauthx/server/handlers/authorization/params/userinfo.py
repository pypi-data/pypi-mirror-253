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
from aiopki.ext.jose import OIDCToken

from oauthx.lib.params import Logger
from oauthx.server.params import ContentEncryptionKey
from oauthx.server.params import CurrentSubject
from oauthx.server.params import ObjectFactory
from oauthx.server.params import RequestSession
from oauthx.server.types import LoginRequired
from oauthx.server.types import UnauthorizedAccount
from .authorizationrequest import AuthorizationRequest
from .client import Client
from .responsemode import ResponseMode


__all__: list[str] = [
    'UserInfo'
]


async def get(
    factory: ObjectFactory,
    logger: Logger,
    key: ContentEncryptionKey,
    request: fastapi.Request,
    session: RequestSession,
    client: Client,
    subject: CurrentSubject,
    response_mode: ResponseMode,
    par: AuthorizationRequest
) -> OIDCToken:
    if subject is None:
        logger.debug(
            "Request is not authenticated (client: %s, request: %s)",
            client.id, par.request_uri
        )
        raise LoginRequired(
            client=client,
            next_url=par.get_authorize_url(request),
            deny_url=await response_mode.deny(),
            a=par.id
        )
    await subject.decrypt_keys(key)
    userinfo = await factory.userinfo(
        subject=subject,
        contributors=[session, client]
    )
    if not client.allows_delegation_to(userinfo):
        raise UnauthorizedAccount({
            'client_name': client.get_display_name(),
            'client_logo': client.get_logo_url(),
            'logout_url': request.url_for('user.logout')\
                .include_query_params(n=par.get_authorize_url(request)),
            'deny_url': await response_mode.deny()
        })
    return userinfo

UserInfo: TypeAlias = Annotated[
    OIDCToken,
    fastapi.Depends(get)
]