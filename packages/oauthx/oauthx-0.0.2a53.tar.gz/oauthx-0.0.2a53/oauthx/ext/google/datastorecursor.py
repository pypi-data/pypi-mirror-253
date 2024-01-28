# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import datetime
import functools
from typing import cast
from typing import Any
from typing import AsyncIterator
from typing import Generic
from typing import Iterable
from typing import Mapping
from typing import TypeVar

import pydantic
from canonical.exceptions import DoesNotExist
from canonical.exceptions import MultipleObjectsReturned
from google.cloud.datastore import Client
from google.cloud.datastore.query import PropertyFilter
from oauthx.ext.google.types import IDatastoreCursor, IDatastoreEntity
from oauthx.ext.google.types import IDatastoreQuery
from .types import IDatastoreKey
from .types import IDatastoreEntity


T = TypeVar('T', bound=pydantic.BaseModel)


class DatastoreCursor(Generic[T]):
    _client: Client
    _filters: Iterable[tuple[str, str, int | str | datetime.datetime]]
    _keys_only: bool
    _keys: list[IDatastoreKey]
    _kind: str
    _limit: int | None
    _loop: asyncio.AbstractEventLoop
    _model: type[T]
    _sort: list[str]

    def __init__(
        self,
        kind: str,
        model: type[T],
        client: Client,
        keys: list[IDatastoreKey] | None = None,
        filters: Iterable[tuple[str, str, int | str | datetime.datetime]] | None = None,
        sort: Iterable[str] | None = None,
        page_size: int = 1000,
        limit: int | None = None,
        _keys_only: bool = False
    ):
        self._client = client
        self._filters = filters or []
        self._keys_only = _keys_only
        self._keys = keys or []
        self._kind = kind
        self._limit = limit
        self._loop = asyncio.get_running_loop()
        self._model = model
        self._page_size = page_size
        self._sort = list(sort or [])

    def factory(self, entity: IDatastoreEntity) -> T:
        return self._model.model_validate(dict(entity))

    def model_factory(self, entity: Mapping[str, Any] | IDatastoreEntity) -> T:
        return self._model.model_validate(entity)

    def keys(self) -> 'EntityKeyDatastoreCursor':
        return EntityKeyDatastoreCursor(
            kind=self._kind,
            model=self._model, # type: ignore
            client=self._client,
            filters=self._filters,
            sort=self._sort,
            page_size=self._page_size,
            limit=self._limit,
            _keys_only=False
        )

    async def all(self) -> AsyncIterator[T]:
        cursor: bytes | None = None
        while True:
            c = await self.run_query(limit=self._page_size, page=cursor)
            objects = list(c)
            if not objects:
                break
            for entity in objects:
                yield self.factory(entity)
            if self._keys:
                # TODO: It is assumed here that with a keys query, all objects
                # are returned in one call.
                break
            if not c.next_page_token:
                break
            cursor = c.next_page_token

    async def first(self) -> T | None:
        c = await self.run_query(limit=1)
        objects = list(c)
        if not objects:
            return None
        return self.factory(objects[0])

    async def one(self) -> T:
        c = await self.run_query(limit=2)
        objects = list(c)
        if len(objects) > 1:
            raise MultipleObjectsReturned
        if not objects:
            raise DoesNotExist
        return self.factory(objects[0])

    async def run_query(self, limit: int | None = None, page: bytes | None = None) -> IDatastoreCursor:
        if self._keys:
            f = functools.partial(self._client.get_multi, self._keys) # type: ignore
        else:
            q = cast(IDatastoreQuery, self._client.query(kind=self._kind)) # type: ignore
            for filter in self._filters:
                q.add_filter(filter=PropertyFilter(*filter)) # type: ignore
            if self._sort:
                q.order = self._sort
            f = functools.partial(q.fetch, start_cursor=page, limit=limit)
        return await self._loop.run_in_executor(None, f) # type: ignore


class EntityKeyDatastoreCursor(DatastoreCursor[IDatastoreKey]): # type: ignore

    def factory(self, entity: IDatastoreEntity) -> IDatastoreKey:
        return entity.key