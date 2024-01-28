# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

from oauthx.lib.protocols import IStorage


__all__: list[str] = ['ApplicationStorage']


def ApplicationStorage(cls: type[IStorage]):
    async def get(
        request: fastapi.Request,
        storage: IStorage = fastapi.Depends(cls)
    ) -> None:
        setattr(request, 'storage', storage)
    return fastapi.Depends(get)