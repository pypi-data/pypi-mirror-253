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
from typing import Literal

import pydantic


class IssuedToken(pydantic.BaseModel):
    active: bool
    aud: str | list[str] = []
    client_id: str | None = None
    exp: int
    iat: int
    iss: str
    jti: str
    nbf: int
    scope: set[str] | None = None
    sub: str | None = None
    token_type: Literal['Bearer'] = 'Bearer'

    @classmethod
    def new(cls, ttl: int, **kwargs: Any):
        now = datetime.datetime.now(datetime.timezone.utc)
        params = {
            **kwargs,
            'active': True,
            'exp': int((now + datetime.timedelta(seconds=ttl)).timestamp()),
            'iat': int(now.timestamp()),
            'nbf': int(now.timestamp()),
        }

        return cls.model_validate(params)

    @pydantic.field_serializer('scope')
    def serialize_scope(self, value: set[str], _: Any) -> str | None:
        return str.join(' ', sorted(self.scope)) if self.scope else None