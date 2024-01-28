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
from aiopki.ext import jose

from oauthx.lib.params import Logger
from oauthx.server.request import Request
from ..models import Session
from .sessionsigner import SessionSigner


__all__: list[str] = ['SessionSigner']


SESSION_COOKIE_NAME: str = 'sessionid'


async def get(
    logger: Logger,
    request: Request,
    signer: SessionSigner,
    encoded: str | None = fastapi.Cookie(
        default=None,
        alias=SESSION_COOKIE_NAME
    ),
) -> Session:
    request.session_cookie = SESSION_COOKIE_NAME
    session = Session.new()
    if encoded:
        try:
            jws = jose.parse(encoded)
            if await jws.verify(signer): # type: ignore
                session = jws.payload(Session.model_validate_json)
        except Exception:
            session = Session.new()
            logger.critical(
                "Session signature verification failed, established new (id: %s)",
                session.id
            )
    else:
        logger.debug("Established session (id: %s)", session.id)
    request.set_session(session)
    return session


RequestSession: TypeAlias =  Annotated[Session, fastapi.Depends(get)]