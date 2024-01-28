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

from oauthx.lib.exceptions import InvalidAuthorizationResponse
from oauthx.lib.models import AuthorizationResponse as AuthorizationResponseModel


async def get(
    error: str | None = fastapi.Query(
        default=None,
        description=(
            "Error code returned by the authorization "
            "server."
        )
    ),
    error_description: str | None = fastapi.Query(
        default=None,
        title="Error description"
    ),
    code: str | None = fastapi.Query(
        default=None,
        title="Authorization code",
        description=(
            "The authorization code supplied by the server."
        )
    ),
    state: str | None = fastapi.Query(
        default=None,
        title="State",
        description=(
            "The `state` parameter that was included with the authorization "
            "request."
        )
    ),
    iss: str | None = fastapi.Query(
        default=None,
        title="Issuer identifier",
        description=(
            "The issuer identifier that clients must use to verify the "
            "response of the authorization endpoint."
        )
    )
) -> AuthorizationResponseModel:
    try:
        return AuthorizationResponseModel.model_validate({
            'code': code,
            'error': error,
            'error_description': error_description,
            'state': state,
            'iss': iss
        })
    except pydantic.ValidationError:
        raise InvalidAuthorizationResponse(error='invalid_response')


AuthorizationResponse: TypeAlias = Annotated[
    AuthorizationResponseModel,
    fastapi.Depends(get)
]