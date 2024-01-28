# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import contextlib

import pydantic

from oauthx.lib.protocols import IStorage


class BaseModel(pydantic.BaseModel):
    _storage: IStorage = pydantic.PrivateAttr()

    def attach(self, storage: IStorage):
        self._storage = storage
        return self

    @contextlib.asynccontextmanager
    async def atomic(self):
        try:
            yield
            await self.persist()
        except Exception:
            raise

    @contextlib.asynccontextmanager
    async def consume(self):
        try:
            yield
            await self.delete()
        except Exception:
            raise

    async def delete(self) -> None:
        await self._storage.delete(self)

    async def persist(self) -> None:
        await self._storage.persist(self)