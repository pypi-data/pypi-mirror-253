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
from aiopki import CryptoKeyType

from oauthx.server.config import Config
from .currentconfig import CurrentConfig


__all__: list[str] = ['ContentEncryptionKey']


async def get(config: Config = CurrentConfig) -> CryptoKeyType:
    cek = config.get_cek()
    await cek
    return cek


ContentEncryptionKey: TypeAlias = Annotated[CryptoKeyType, fastapi.Depends(get)]