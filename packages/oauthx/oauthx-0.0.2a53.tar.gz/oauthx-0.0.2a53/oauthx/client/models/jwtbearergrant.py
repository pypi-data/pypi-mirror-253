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
from aiopki.ext.jose import CompactSerialized

from oauthx.lib.types import ScopeType
from .basegrant import BaseGrant


class JWTBearerGrant(BaseGrant):
    grant_type: Literal['urn:ietf:params:oauth:grant-type:jwt-bearer'] = pydantic.Field(
        default=...,
        description=(
            "This value **must** be `urn:ietf:params:"
            "oauth:grant-type:jwt-bearer`."
        )
    )
    
    assertion: CompactSerialized = pydantic.Field(
        default=...,
        description=(
            "A compact-encoded JSON Web Token (JWT) that is signed, "
            "containing the claims specified in RFC 7523."
        )
    )

    scope: ScopeType = pydantic.Field(
        default_factory=ScopeType,
        description=(
            "The space-delimited scope of the access request."
        )
    )
    
    def must_authenticate(self) -> bool:
        return False

    def must_identify(self) -> bool:
        return False