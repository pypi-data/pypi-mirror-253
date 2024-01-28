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

from oauthx.lib.exceptions import Error
from oauthx.lib.exceptions import InvalidAuthorizationResponse
from oauthx.lib.exceptions import InvalidTokenResponse
from oauthx.lib.models import Error as ErrorModel
from oauthx.lib.models import ObtainedGrant as ObtainedGrantModel
from .authorizationresponse import AuthorizationResponse
from .client import Client
from .clientauthorizationstate import ClientAuthorizationState
from .clientstorage import ClientStorage


async def get(
    params: AuthorizationResponse,
    provider: Client,
    state: ClientAuthorizationState,
    storage: ClientStorage
) -> ObtainedGrantModel:
    if state is None:
        raise InvalidAuthorizationResponse(error='invalid_response')
    return_url = state.annotation('return-url')
    if params.is_error():
        assert isinstance(params.root, ErrorModel)
        await storage.delete(state)
        raise InvalidAuthorizationResponse(
            error=params.root.error,
            error_description=params.root.error_description,
            context={
                'authorize_url': state.get_authorize_url(),
                'provider': provider,
                'return_url': return_url,
            }
        )
    try:
        grant = await provider.authorization_code(params, state)
    except Error as exception:
        await storage.delete(state)
        raise InvalidTokenResponse(
            error=exception.error,
            error_description=exception.error_description,
            context={'provider': provider}
        )
    await storage.delete(state)
    return grant


AuthorizationCodeGrant: TypeAlias = Annotated[
    ObtainedGrantModel,
    fastapi.Depends(get)
]