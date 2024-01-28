# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

from canonical.protocols import ICache


__all__: list[str] = ['ApplicationCache']


def ApplicationCache(cls: type[ICache]):
    async def get(
        request: fastapi.Request,
        cache: ICache = fastapi.Depends(cls)
    ) -> None:
        setattr(request, 'cache', cache)
    return fastapi.Depends(get)