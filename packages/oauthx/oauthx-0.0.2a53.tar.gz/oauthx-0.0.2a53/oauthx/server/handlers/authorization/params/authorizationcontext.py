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

from oauthx.server import models
from oauthx.server.params import Storage
from oauthx.server.request import Request
from .client import Client
from .redirecturi import RedirectURI
from .responsemode import ResponseMode


__all__: list[str] = [
    'AuthorizationContext'
]


async def get(
    request: Request,
    storage: Storage,
    client: Client,
    redirect_uri: RedirectURI,
    response_mode: ResponseMode
) -> models.AuthorizationContext:
    ctx = models.AuthorizationContext.model_validate({
        'client': client,
        'redirect_uri': redirect_uri,
        'response_mode': response_mode,
    })
    request.set_context(ctx)
    return ctx


AuthorizationContext: TypeAlias = Annotated[
    models.AuthorizationContext,
    fastapi.Depends(get)
]