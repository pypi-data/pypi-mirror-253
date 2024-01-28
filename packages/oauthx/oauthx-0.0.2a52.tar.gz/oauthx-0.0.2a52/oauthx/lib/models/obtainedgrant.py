# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Literal

import pydantic
from aiopki.ext.jose import CompactSerialized

from oauthx.lib.types import AccessToken
from oauthx.lib.types import ScopeType


class ObtainedGrant(pydantic.BaseModel):
    obtained: datetime.datetime = pydantic.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    token_type: Literal['Bearer', 'bearer']
    expires_in: int
    access_token: AccessToken
    refresh_token: str | None = None
    id_token: CompactSerialized | None = None
    scope: ScopeType | None = None

    def is_expired(self) -> bool:
        """Return a boolean indicating if the grant is expired."""
        now = datetime.datetime.now(datetime.timezone.utc)
        return abs(int((now - self.obtained).total_seconds())) > self.expires_in