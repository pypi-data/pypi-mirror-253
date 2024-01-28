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
from oauthx.lib.types import RedirectURI as RedirectURIType
from oauthx.server.request import Request
from oauthx.server.types import InvalidRedirectURI
from .pushedauthorizationrequest import PushedAuthorizationRequest
from .client import Client
from .query import REDIRECT_URI


__all__: list[str] = [
    'RedirectURI'
]


async def get(
    request: Request,
    client: Client,
    params: PushedAuthorizationRequest,
    redirect_uri: str | None = REDIRECT_URI,
) -> RedirectURIType | None:
    if params and redirect_uri:
        raise InvalidRequest(
            "The redirect_uri parameter must not be used in combination "
            "with request or request_uri"
        )
    if params is not None:
        redirect_uri = params.redirect_uri
    if redirect_uri is not None:
        try:
            redirect_uri = RedirectURIType(redirect_uri)

            # If there are parameters, the request was signed by the
            # client so we can trust the redirect URI.
            if not params and not client.can_redirect(redirect_uri):
                raise InvalidRedirectURI
        except ValueError:
            raise InvalidRedirectURI
    return redirect_uri


RedirectURI: TypeAlias = Annotated[
    RedirectURIType | None,
    fastapi.Depends(get)
]