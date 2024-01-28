# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import json
from typing import Any
from typing import Callable

import pydantic
from canonical import EmailAddress


class UserInfoResponse(pydantic.BaseModel):
    claims: dict[str, Any] = pydantic.Field(default={}, alias='__claims__')
    email: EmailAddress | None = None
    email_verified: bool | None = None
    family_name: str | None = None
    given_name: str | None = None
    middle_name: str | None = None
    name: str | None = None
    sub: str

    @pydantic.model_validator(mode='before')
    def preprocess(cls, values: bytes | str | dict[str, Any]) -> dict[str, Any]:
        if isinstance(values, (bytes, str)):
            values = json.loads(values)
        assert isinstance(values, dict)
        return {
            **values,
            '__claims__': {
                k: v
                for k, v in values.items()
                if k not in cls.model_fields
            }
        }

    @pydantic.model_serializer(mode='wrap', when_used='always')
    def serialize_model(
        self,
        info: Callable[['UserInfoResponse'], dict[str, Any]]
    ):
        values = info(self)
        if 'claims' in values:
            values = {**values.pop('claims'), **values}
        return values

    def get(self, claim: str) -> Any:
        return self.claims.get(claim)