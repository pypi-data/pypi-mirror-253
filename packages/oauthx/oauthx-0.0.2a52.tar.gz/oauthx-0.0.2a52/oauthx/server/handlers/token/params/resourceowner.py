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
from aiopki.ext.jose import CompactSerialized

from oauthx.lib.exceptions import InvalidGrant
from oauthx.lib.exceptions import InvalidRequest
from oauthx.lib.types import GrantType
from oauthx.server.models import AuthorizationCode
from oauthx.server.params import Storage
from oauthx.server.protocols import IResourceOwner
from .refreshtoken import RefreshToken
from .query import CODE
from .query import GRANT_TYPE


__all__: list[str] = [
    'ResourceOwner'
]


def requires_owner(grant_type: str):
    return grant_type not in {
        'authorization_code',
        'client_credentials',
        'refresh_token',
        'urn:ietf:params:oauth:grant-type:jwt-bearer'
    }


async def get(
    storage: Storage,
    refresh_token: RefreshToken,
    code: CompactSerialized | None = CODE,
    grant_type: GrantType = GRANT_TYPE
) -> IResourceOwner | None:
    owner: IResourceOwner | None
    match grant_type:
        case 'authorization_code':
            if code is None:
                raise InvalidRequest(
                    "The authorization_code parameter is required."
                )
            try:
                jwt = code.payload(AuthorizationCode.model_validate_json)
            except pydantic.ValidationError:
                # The code was signed by us but its structure did not validate.
                raise InvalidGrant(
                    "The provided authorization code is not valid."
                )
            owner = await storage.get(jwt.owner)
        case 'client_credentials':
            owner = None
        case 'refresh_token':
            assert refresh_token is not None
            owner = await storage.get(refresh_token.owner)
        case 'urn:ietf:params:oauth:grant-type:jwt-bearer':
            # The primary key of a resource owner is (client_id, subject_id)
            # but for this grant the client might not identify itself. If
            # there is a resource owner will be determined after validating
            # the assertion.
            owner = None
        case _:
            raise NotImplementedError

    if requires_owner(grant_type) and owner is None:
        raise InvalidGrant(
            "The resource owner identified by the grant parameters "
            "does not exist."
        )
    return owner

ResourceOwner: TypeAlias = Annotated[
    IResourceOwner | None,
    fastapi.Depends(get)
]