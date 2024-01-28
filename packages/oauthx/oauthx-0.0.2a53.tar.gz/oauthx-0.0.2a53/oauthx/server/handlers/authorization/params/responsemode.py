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
import pydantic

from oauthx.lib.exceptions import InvalidRequest
from oauthx.lib.params import Logger
from oauthx.server.request import Request
from oauthx.server.params import IssuerIdentifier
from oauthx.server.params import ObjectFactory
from oauthx.server.params import TokenSigner
from oauthx.server.types import InvalidAuthorizationRequest
from oauthx.server.types import InvalidResponseType
from oauthx.server.types import IResponseMode
from oauthx.server.types import UnauthorizedClient
from .client import Client
from .query import RESPONSE_MODE
from .redirecturi import RedirectURI
from .responsetype import ResponseType
from .state import State


__all__: list[str] = [
    'ResponseMode'
]


async def get(
    factory: ObjectFactory,
    signer: TokenSigner,
    logger: Logger,
    iss: IssuerIdentifier,
    request: Request,
    client: Client,
    response_type: ResponseType,
    redirect_uri: RedirectURI,
    state: State,
    response_mode: str | None = RESPONSE_MODE,
) -> IResponseMode:
    try:
        obj = await factory.response_mode(
            iss=iss,
            client=client, # type: ignore
            response_type=response_type,
            response_mode=response_mode,
            redirect_uri=redirect_uri,
            state=state
        )
        request.response_mode = obj.with_signer(signer) # type: ignore
    except pydantic.ValidationError:
        raise InvalidAuthorizationRequest(
            error='invalid_request',
            allow_redirect=True,
            redirect_uri=redirect_uri,
            context={'client_name': client.get_display_name()}
        )
    if not client.allows_response_type(obj.response_type):
        raise InvalidResponseType
    if not client.can_grant(obj.grants()):
        logger.debug(
            "Client does not allow the requested grant (client: %s)",
            client.id
        )
        raise UnauthorizedClient
    if client.requires_state() and not state:
        raise InvalidRequest("The client requires the use of the state parameter.")
    return obj.with_signer(signer)

ResponseMode: TypeAlias = Annotated[
    IResponseMode,
    fastapi.Depends(get)
]