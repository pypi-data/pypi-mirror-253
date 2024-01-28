# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Any

import pydantic

from oauthx.lib.types import AccessTokenHash


class TokenSubject(pydantic.BaseModel):
    """Maintains details about a :term:`Subject` as retrieved from the UserInfo
    endpoint of an authorization server.
    """
    at_hash: AccessTokenHash = pydantic.Field(
        default=...,
        title="Hash",
        description=(
            "The SHA3-256 hash of the access token that was used to "
            "authenticate the subject."
        )
    )
    
    exp: datetime.datetime = pydantic.Field(
        default_factory=lambda: (
            datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=3600)
        ),
        title="Expires",
        description=(
            "Indicates the date and time at which the maintained "
            "user information expires."
        )
    )

    sub: str = pydantic.Field(
        default=...,
        title="Subject ID",
        description=(
            "The subject identifier, as provided by the authorization "
            "server."
        )
    )
    
    claims: dict[str, Any] = pydantic.Field(
        default_factory=dict,
        title="Claims",
        description=(
            "The claims that the access token could obtain for the "
            "subject."
        )
    )
    
    @property
    def pk(self) -> str:
        return self.at_hash