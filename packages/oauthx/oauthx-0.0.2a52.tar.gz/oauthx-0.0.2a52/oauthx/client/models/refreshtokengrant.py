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

from oauthx.lib.types import ScopeType
from .basegrant import BaseGrant


class RefreshTokenGrant(BaseGrant):
    grant_type: Literal['refresh_token'] = pydantic.Field(
        default=...,
        description="This value **must** be `refresh_token`."
    )

    refresh_token: str = pydantic.Field(
        default=...,
        description="The refresh token that was issued to the client."
    )

    scope: ScopeType | None = pydantic.Field(
        default=None,
        description=(
            "The space-delimited scope of the access request. The requested "
            "scope **must not** include any scope not originally granted by "
            "the resource owner, and if omitted is treated as equal to the "
            "scope originally granted by the resource owner."
        )
    )