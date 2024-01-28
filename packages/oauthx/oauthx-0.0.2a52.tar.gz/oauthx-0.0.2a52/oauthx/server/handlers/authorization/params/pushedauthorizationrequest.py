# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import cast
from typing import Annotated
from typing import TypeAlias

import fastapi

from oauthx.lib.exceptions import InvalidRequest
from oauthx.lib.params import Logger
from oauthx.lib.types import RequestURI
from oauthx.server import models
from oauthx.server.params import Storage
from oauthx.server.types import AuthorizationRequestKey
from oauthx.server.types import StopSnooping
from .client import Client
from .query import REQUEST
from .query import REQUEST_URI


__all__: list[str] = [
    'PushedAuthorizationRequest'
]


async def get(
    client: Client,
    logger: Logger,
    storage: Storage,
    request: str | None = REQUEST,
    request_uri: RequestURI | None = REQUEST_URI,
) -> models.AuthorizationRequest | None:
    params = None
    if client.must_push() and not request_uri:
        raise InvalidRequest(
            "The client is configured to accept only pushed authorization "
            "requests."
        )
    if request and request_uri:
        raise InvalidRequest(
            "The request and request_uri parameters are mutually"
            "exclusive."
        )
    if request:
        raise NotImplementedError
    elif request_uri:
        assert request_uri.id is not None
        params = await storage.get(AuthorizationRequestKey.fromuri(request_uri))
        if params is None:
            raise StopSnooping
        logger.debug(
            "Retrieving existing authorization request (request: %s)",
            params.request_uri # type: ignore
        )

    return cast(models.AuthorizationRequest, params)


PushedAuthorizationRequest: TypeAlias = Annotated[
    models.AuthorizationRequest | None,
    fastapi.Depends(get)
]