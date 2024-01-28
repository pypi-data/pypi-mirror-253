# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Annotated
from typing import TypeAlias

import fastapi

from ..config import Config


__all__: list[str] = ['ServerConfig']


def get(request: fastapi.Request) -> Config:
    return request.config # type: ignore



ServerConfig: TypeAlias = Annotated[Config, fastapi.Depends(get)]