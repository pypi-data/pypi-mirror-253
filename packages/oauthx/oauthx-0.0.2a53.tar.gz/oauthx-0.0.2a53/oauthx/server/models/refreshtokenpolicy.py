# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import secrets
from typing import Literal

import pydantic


class RefreshTokenPolicy(pydantic.BaseModel):
    current: str = pydantic.Field(
        default_factory=lambda: secrets.token_urlsafe(48)
    )
    
    use: Literal['once', 'rolling', 'fixed'] = pydantic.Field(
        default=...
    )

    def rotate(self) -> None:
        if self.use in {'once'}:
            self.current = secrets.token_urlsafe(48)