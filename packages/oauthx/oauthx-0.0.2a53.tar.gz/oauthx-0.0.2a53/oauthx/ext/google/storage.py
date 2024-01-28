# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import functools
from typing import Any
from typing import AsyncIterable
from typing import Callable
from typing import Iterable
from typing import TypeVar

import pydantic
from canonical import ResourceIdentifier

from oauthx.lib.models import ClientAuthorizationState
from oauthx.lib.models import ClientAuthorizationStateKey
from oauthx.lib.types import MaskedPrincipal
from oauthx.server import types
from oauthx.server import BaseStorage
from oauthx.server.types import AuthorizationKey
from oauthx.server.models import Authorization
from oauthx.server.models import AuthorizationRequest
from oauthx.server.models import BaseModel
from oauthx.server.models import Claim
from oauthx.server.models import ClaimSet
from oauthx.server.models import Client
from oauthx.server.models import Principal
from oauthx.server.models import Receipt
from oauthx.server.models import ResourceOwner
from oauthx.server.models import ResourceOwnerKey
from oauthx.server.models import Subject
from oauthx.server.models import SubjectKey
from oauthx.server.params import ContentEncryptionKey
from .params import DatastoreClient
from .types import IDatastoreKey
from .types import IDatastoreEntity


T = TypeVar('T', bound=pydantic.BaseModel)


class DatastoreStorage(BaseStorage):

    @staticmethod
    async def run_in_executor(
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any
    ) -> Any:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, func, *args, **kwargs)

    def setup( # type: ignore
        self,
        *,
        client: DatastoreClient, # type: ignore
        key: ContentEncryptionKey,
        **kwargs: Any
    ) -> None:
        self.client = client
        self.key = key

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

    def entity_factory(self, key: IDatastoreKey, obj: pydantic.BaseModel) -> IDatastoreEntity:
        entity = self.client.entity(key) # type: ignore
        attrs = obj.model_dump(mode='json')
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

    async def get_model_by_key(self, cls: type[T], pk: int | str | ResourceIdentifier[Any, Any]) -> T | None:
        entity = await self.get_entity_by_key(
            key=self.entity_key(cls, pk)
        )
        if entity is None:
            return None
        obj = cls.model_validate(dict(entity))
        if isinstance(obj, BaseModel):
            obj.attach(self)
        return obj

    async def put(self, obj: pydantic.BaseModel, pk: int | str | ResourceIdentifier[Any, Any]) -> IDatastoreKey:
        key = self.entity_key(type(obj), pk)
        entity = self.entity_factory(key, obj)
        await self.run_in_executor(self.client.put, entity) # type: ignore
        return entity.key # type: ignore

    async def get_authorization(self, key: AuthorizationKey) -> Authorization | None:
        return await self.get_model_by_key(Authorization, int(key))

    async def get_authorization_request(self, key: types.AuthorizationRequestKey) -> types.IAuthorizationRequest | None:
        return await self.get_model_by_key(AuthorizationRequest, int(key)) # type: ignore

    async def get_authorization_state(self, key: ClientAuthorizationStateKey) -> ClientAuthorizationState | None:
        return await self.get_model_by_key(ClientAuthorizationState, key)

    async def get_client(self, key: Client.Key) -> Client | None:
        return None

    async def get_principal(self, masked: MaskedPrincipal) -> Principal | None:
        return await self.get_model_by_key(Principal, str(masked))

    async def get_resource_owner(self, key: ResourceOwnerKey) -> ResourceOwner | None:
        return await self.get_model_by_key(ResourceOwner, str(key))

    async def get_subject_by_pk(self, pk: SubjectKey) -> Subject | None:
        return await self.get_model_by_key(Subject, int(pk))

    async def persist_authorization(self, authorization: Authorization) -> None:
        await self.put(authorization, int(authorization.pk))

    async def persist_authorization_request(self, request: AuthorizationRequest) -> None:
        await self.put(request, request.id)

    async def persist_authorization_state(
            self,
            state: ClientAuthorizationState
    ) -> None:
        await self.put(state, state.pk)

    async def persist_principal(self, principal: Principal) -> None:
        if not principal.is_encrypted():
            raise ValueError("Call Principal.encrypt(subject) prior to persisting.")
        await self.put(principal, str(principal.masked))

    async def persist_receipt(self, receipt: Receipt) -> None:
        claims = await ClaimSet.fromquery(
            provider=receipt.provider,
            query=self.find(
                kind=Claim,
                filters=[
                    ('provider', '=', str(receipt.provider)),
                    ('sub', '=', receipt.sub)
                ]
            )
        )
        for claim in claims.diff(receipt.claims):
            await self.put(claim, claim.pk)

    async def persist_resource_owner(self, owner: ResourceOwner) -> None:
        await self.put(owner, str(owner.pk))

    async def persist_subject(self, subject: Subject) -> None:
        if not subject.is_encrypted():
            raise ValueError("Call Subject.encrypt_keys() prior to persisting.")
        await self.put(subject, int(subject.get_primary_key()))