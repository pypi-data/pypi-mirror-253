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

from oauthx.lib.protocols import IStorage
from oauthx.server.request import Request


__all__: list[str] = ['Storage']


def get(request: Request) -> IStorage:
    return getattr(request, 'storage')


Storage: TypeAlias = Annotated[IStorage, fastapi.Depends(get)]