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
from canonical import PythonSymbol

from oauthx.server.models import Scope


class ScopeSpecification(pydantic.BaseModel):
    name: str
    claims: list[str]
    impl: PythonSymbol[type[Scope]] = pydantic.Field(
        default_factory=lambda: PythonSymbol.fromqualname('oauthx.server.models.Scope') # type: ignore
    )
    
    @property
    def scope(self) -> Any:
        return self.impl.value(**self.model_dump(exclude={'impl'}))