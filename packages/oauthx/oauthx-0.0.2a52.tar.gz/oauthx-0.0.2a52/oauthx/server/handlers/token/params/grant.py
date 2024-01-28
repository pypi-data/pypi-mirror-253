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
from aiopki.ext.jose import CompactSerialized

from oauthx.lib.exceptions import InvalidScope
from oauthx.lib.models import Grant as GrantModel
from oauthx.lib.types import GrantType
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import TargetResource
from .granttype import GrantType
from .resourceowner import ResourceOwner
from .query import ASSERTION
from .query import CODE
from .query import REDIRECT_URI
from .query import REFRESH_TOKEN
from .query import RESOURCE
from .query import SCOPE


__all__: list[str] = [
    'Grant'
]


async def get(
    grant_type: GrantType,
    owner: ResourceOwner,
    assertion: CompactSerialized | None = ASSERTION,
    code: CompactSerialized = CODE,
    client_id: str | None = fastapi.Form(
        default=None,
        title="Client ID",
        description=(
            "Required if the client is not authenticating with "
            "the authorization server"
        )
    ),
    client_secret: str | None = fastapi.Form(
        default=None,
        title="Client secret",
        description=(
            "This parameter is **required** if the client is authenticating using "
            "the `client_secret_post` method, otherwise is **must** be "
            "omitted."
        )
    ),
    redirect_uri: RedirectURI | None = REDIRECT_URI,
    refresh_token: str | None = REFRESH_TOKEN,
    resources: set[TargetResource] = RESOURCE,
    scope: str | None = SCOPE
) -> GrantModel:
    grant = GrantModel.model_validate({
        'grant_type': grant_type,
        'assertion': assertion,
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code.encode() if code else None,
        'redirect_uri': redirect_uri,
        'refresh_token': refresh_token,
        'resource': resources,
        'scope': scope
    })
    await grant.decrypt(NotImplemented)
    if owner is not None and not owner.grants_consent(grant.scope):
        raise InvalidScope(
            "The resource owner has revoked consent "
            "for the requested scope."
        )

    return grant


Grant: TypeAlias = Annotated[
    GrantModel,
    fastapi.Depends(get)
]