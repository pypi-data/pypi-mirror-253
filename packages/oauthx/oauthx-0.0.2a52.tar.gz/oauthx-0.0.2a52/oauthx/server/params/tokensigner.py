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

import aiopki
import fastapi

from oauthx.server.request import Request


__all__: list[str] = ['TokenSigner']


async def get(request: Request) -> aiopki.CryptoKeyType:
    return await request.keychain # type: ignore


TokenSigner: TypeAlias =  Annotated[aiopki.CryptoKeyType, fastapi.Depends(get)]