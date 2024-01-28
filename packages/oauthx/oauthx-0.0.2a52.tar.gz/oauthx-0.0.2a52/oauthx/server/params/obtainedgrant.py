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
from oauthx.lib.params import ClientAuthorizationState
from oauthx.lib.models import Error as ErrorModel
from oauthx.lib.models import ObtainedGrant as ObtainedGrantModel
from oauthx.lib.params import AuthorizationResponse
from .storage import Storage
from .upstreamprovider import UpstreamProvider


async def get(
    params: AuthorizationResponse,
    provider: UpstreamProvider,
    state: ClientAuthorizationState,
    storage: Storage
) -> ObtainedGrantModel:
    if state is None:
        raise InvalidAuthorizationResponse(error='invalid_response')
    return_url = state.annotation('return-url')
    if return_url is None:
        await storage.delete(state)
        raise InvalidAuthorizationResponse(error='invalid_response')
    if params.is_error():
        assert isinstance(params.root, ErrorModel)
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
        return await provider.authorization_code(params, state) # type: ignore
    except Error as exception:
        await storage.delete(state)
        raise InvalidTokenResponse(
            error=exception.error,
            error_description=exception.error_description,
            context={'provider': provider}
        )


ObtainedGrant: TypeAlias = Annotated[
    ObtainedGrantModel,
    fastapi.Depends(get)
]