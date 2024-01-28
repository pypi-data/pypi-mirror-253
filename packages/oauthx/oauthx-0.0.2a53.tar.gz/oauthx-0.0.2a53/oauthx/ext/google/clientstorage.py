# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
from typing import Any
from typing import TypeVar

from canonical import ResourceIdentifier

from oauthx.lib.models import ClientAuthorizationStateKey
from oauthx.lib.models import ClientAuthorizationState
from oauthx.lib.protocols import IClientStorage
from oauthx.lib.protocols import IClient
from oauthx.lib.types import Masked
from .datastorestorage import DatastoreStorage
from .params import DatastoreClient


T = TypeVar('T')


class ClientStorage(DatastoreStorage, IClientStorage):

    def __init__( # type: ignore
        self,
        *,
        client: DatastoreClient, # type: ignore
    ) -> None:
        self.client = client

    async def get(self, key: ResourceIdentifier[Any, T]) -> T | None:
        return await self._get(key)

    @functools.singledispatchmethod
    async def _get(self, key: Any) -> Any | None:
        raise NotImplementedError

    async def application(self, client_id: str) -> IClient | None:
        raise NotImplementedError

    async def mask(self, obj: Any) -> Masked:
        raise NotImplementedError

    @_get.register
    async def state(self, key: ClientAuthorizationStateKey) -> Any:
        return await self.get_model_by_key(ClientAuthorizationState, key)

    async def persist(self, object: Any) -> None:
        await self.put(object, object.pk)