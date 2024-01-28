# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

import pydantic

from oauthx.lib.types import RedirectURI
from .basegrant import BaseGrant


class AuthorizationCodeGrant(BaseGrant):
    grant_type: Literal['authorization_code'] = pydantic.Field(
        default=...,
        description="This value **must** be `authorization_code`."
    )

    code: str = pydantic.Field(
        default=...,
        description="The authorization code received from the authorization server"
    )

    redirect_uri: RedirectURI | None = pydantic.Field(
        default=None,
        description=(
            "This parameter is **required** if the `redirect_uri` parameter was "
            "included in the authorization request and their values **must** be identical."
        )
    )

    @property
    def scope(self) -> set[str]:
        return set()

    def requires_offline_access(self) -> bool:
        return False