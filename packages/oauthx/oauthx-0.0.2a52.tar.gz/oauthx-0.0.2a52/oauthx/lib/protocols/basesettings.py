# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import TypeVar

import aiopki
import fastapi
import pydantic


P = TypeVar('P', bound=pydantic.BaseModel)
T = TypeVar('T')


class BaseSettings(pydantic.BaseModel):
    __module__: str = 'oauthx.lib.protocols'

    def inject(self) -> Any:
        def f(request: fastapi.Request):
            setattr(request, 'config', self)
        return fastapi.Depends(f)

    def get_cek(self) -> aiopki.CryptoKeyType:
        raise NotImplementedError

    def get_splash_image_url(self) -> str:
        raise NotImplementedError