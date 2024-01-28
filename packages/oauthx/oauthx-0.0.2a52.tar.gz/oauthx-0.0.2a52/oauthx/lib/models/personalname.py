# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pydantic
from aiopki.ext.jose import OIDCToken


class PersonalName(pydantic.BaseModel):
    name: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    middle_name: str | None = None
    nickname: str | None = None

    @classmethod
    def from_oidc_token(cls, token: OIDCToken):
        return cls.model_validate(token.model_dump())

    def model_post_init(self, _: Any) -> None:
        if not self.is_provided():
            raise ValueError("None of the name elements are provided.")

    def is_provided(self):
        return any([
            self.name,
            self.given_name,
            self.family_name,
            self.middle_name,
            self.nickname
        ])