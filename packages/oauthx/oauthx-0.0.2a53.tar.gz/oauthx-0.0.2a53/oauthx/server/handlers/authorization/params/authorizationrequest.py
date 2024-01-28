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

from oauthx.lib.params import Logger
from oauthx.server.models import AuthorizationRequest as AuthorizationRequestModel
from oauthx.server.params import ObjectFactory
from .client import Client
from .pushedauthorizationrequest import PushedAuthorizationRequest
from .redirecturi import RedirectURI
from .scope import Scope
from .targetresources import TargetResources


__all__: list[str] = [
    'AuthorizationRequest'
]


async def get(
    factory: ObjectFactory,
    logger: Logger,
    request: fastapi.Request,
    client: Client,
    redirect_uri: RedirectURI,
    resources: TargetResources,
    par: PushedAuthorizationRequest,
    scope: Scope,
) -> AuthorizationRequestModel:
    if par is None:
        par = await factory.request(
            client=client, # type: ignore
            request=request,
            redirect_uri=redirect_uri,
            resources=resources,
            scope=scope
        )
        await par.persist()
        logger.debug(
            "Persisted authorization request parameters (client: %s, urn: %s)",
            client.id, par.request_uri
        )
    return par

AuthorizationRequest: TypeAlias = Annotated[
    AuthorizationRequestModel,
    fastapi.Depends(get)
]