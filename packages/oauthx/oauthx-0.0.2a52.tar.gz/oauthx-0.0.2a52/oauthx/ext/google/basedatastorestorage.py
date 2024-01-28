# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import contextlib
import datetime
import functools
import inspect
from typing import cast
from typing import Any
from typing import AsyncIterable
from typing import Callable
from typing import Iterable
from typing import Mapping
from typing import TypeVar

import pydantic
from canonical import PersistedModel
from canonical import ResourceIdentifier

from oauthx.lib import utils
from .datastorecursor import DatastoreCursor
from .params import DatastoreClient
from .types import IDatastoreKey
from .types import IDatastoreEntity
from .types import IDatastoreTransaction


T = TypeVar('T', bound=pydantic.BaseModel)


class BaseDatastoreStorage:
    dump_mode: str = 'json'
    exclude_fields: set[str] = set()
    exclude_none: bool = False

    @utils.class_property
    def __signature__(cls) -> inspect.Signature:
        return utils.merge_signatures([
            inspect.signature(cls.__init__),
            inspect.signature(cls.require)
        ])

    @staticmethod
    async def run_in_executor(
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any
    ) -> Any:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, func, *args, **kwargs)

    def __init__( # type: ignore
        self,
        *,
        client: DatastoreClient, # type: ignore
        **kwargs: Any
    ) -> None:
        self.client = client
        self.require(**kwargs)

    def require(self, **_: Any):
        pass

    async def allocate_identifier(self, cls: type | str) -> int:
        if not isinstance(cls, str):
            cls = cls.__name__
        base = self.entity_key(kind=cls)
        result = await self.run_in_executor(
            functools.partial( # type: ignore
                self.client.allocate_ids, # type: ignore
                incomplete_key=base,
                num_ids=1
            )
        )
        return [x for x in result][0].id

    async def delete(self, obj: Any) -> None:
        key = self.entity_key(type(obj), obj.pk)
        await self.run_in_executor(
            functools.partial(
                self.client.delete, # type: ignore
                key=key
            )
        )

    def dump_model(
        self,
        obj: pydantic.BaseModel,
        exclude_fields: set[str] | dict[str, Any] | None = None,
        exclude_none: bool = False
    ) -> dict[str, Any]:
        return obj.model_dump(
            mode=self.dump_mode,
            exclude=exclude_fields or self.exclude_fields,
            exclude_none=exclude_none or self.exclude_none
        )

    def entity_factory(
        self,
        key: IDatastoreKey,
        obj: pydantic.BaseModel,
        exclude_fields: set[str] | dict[str, Any] | None = None
    ) -> IDatastoreEntity:
        entity = self.client.entity(key) # type: ignore
        attrs = self.dump_model(obj, exclude_fields=exclude_fields)
        if attrs:
            entity.update(attrs) # type: ignore
        return entity # type: ignore

    def entity_key(
        self,
        kind: str | type,
        identifier: int | str | ResourceIdentifier[int | str, Any] | None = None,
        parent: IDatastoreKey | None = None
    ) -> IDatastoreKey:
        if not isinstance(kind, str):
            kind = kind.__name__
        if isinstance(identifier, ResourceIdentifier):
            identifier = identifier.cast() # type: ignore
        args: list[Any] = [kind]
        if identifier is not None:
            args.append(identifier)
        return self.client.key(*args, parent=parent) # type: ignore

    def model_factory(self, entity: Mapping[str, Any], model: type[T]) -> T:
        obj = model.model_validate(dict(entity))
        if isinstance(obj, PersistedModel):
            obj.attach(self) # type: ignore
        return obj

    def query(
        self,
        *,
        model: type[T],
        filters: Iterable[tuple[str, str, int | str | datetime.datetime]] | None = None,
        sort: Iterable[str] | None = None,
        limit: int | None = None,
        kind: str | None = None,
        page_size: int = 10,
        keys: list[IDatastoreKey] | None = None
    ) -> DatastoreCursor[T]:
        return DatastoreCursor(
            kind=kind or model.__name__,
            model=model,
            client=self.client,
            keys=keys,
            filters=filters,
            sort=sort,
            limit=limit,
            page_size=page_size
        )

    async def find(
        self,
        kind: type[T],
        filters: Iterable[tuple[str, str, int | str]],
        sort: Iterable[str] | None = None
    ) -> AsyncIterable[T]:
        q = self.client.query(kind=kind.__name__) # type: ignore
        if sort is not None:
            q.order = sort
        for filter in filters:
            q.add_filter(*filter) # type: ignore
        results = await self.run_in_executor(
            functools.partial(q.fetch) # type: ignore
        )
        for entity in results:
            yield kind.model_validate(dict(entity))

    async def get_entity_by_key(self, key: IDatastoreKey) -> IDatastoreEntity | None:
        return await self.run_in_executor(
            functools.partial(
                self.client.get, # type: ignore
                key=key
            )
        )

    async def get_model_by_key(
        self,
        cls: type[T], pk: int | str | ResourceIdentifier[Any, Any],
        parent: IDatastoreKey | None = None
    ) -> T | None:
        entity = await self.get_entity_by_key(
            key=self.entity_key(cls, pk, parent=parent)
        )
        if entity is None:
            return None
        return self.model_factory(dict(entity), cls)

    async def put(
        self,
        obj: pydantic.BaseModel,
        pk: int | str | ResourceIdentifier[Any, Any],
        parent: IDatastoreKey | None = None,
        exclude_fields: set[str] | dict[str, Any] | None = None,
        transaction: IDatastoreTransaction | None = None
    ) -> IDatastoreKey:
        put = self.client.put if transaction is None else transaction.put # type: ignore
        key = self.entity_key(type(obj), pk, parent=parent)
        entity = self.entity_factory(key, obj, exclude_fields=exclude_fields)
        await self.run_in_executor(put, entity) # type: ignore
        return entity.key # type: ignore

    @contextlib.asynccontextmanager
    async def transaction(self):
        tx = cast(IDatastoreTransaction, await self.run_in_executor(self.client.transaction)) # type: ignore
        try:
            await self.run_in_executor(tx.begin)
            yield tx
            await self.run_in_executor(tx.commit)
        except Exception:
            await self.run_in_executor(tx.rollback)
            raise