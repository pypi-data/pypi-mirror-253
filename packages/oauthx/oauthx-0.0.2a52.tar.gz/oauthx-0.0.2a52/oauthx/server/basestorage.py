# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import contextlib
import functools
import inspect
from typing import Any
from typing import AsyncIterable
from typing import Iterable
from typing import TypeVar

import fastapi
import pydantic
from canonical import ResourceIdentifier

from oauthx.lib import utils
from oauthx.lib.models import ClientAuthorizationStateKey
from oauthx.lib.models import ClientAuthorizationState
from oauthx.lib.protocols import IStorage
from oauthx.lib.types import MaskedPrincipal
from oauthx.server import types
from oauthx.server.models import Authorization
from oauthx.server.models import AuthorizationRequest
from oauthx.server.models import Client
from oauthx.server.models import Principal
from oauthx.server.models import Receipt
from oauthx.server.models import ResourceOwner
from oauthx.server.models import Subject
from oauthx.server.models import SubjectKey
from oauthx.server.types import AuthorizationKey
from oauthx.server.types import AuthorizationRequestKey
from oauthx.server.protocols import IResourceOwner
from oauthx.server.protocols import ISubject
from .config import Config
from .localclientstorage import LocalClientStorage
from .params import CurrentConfig


T = TypeVar('T')


class BaseStorage(IStorage):
    __module__: str = 'oauthx.server.ref'
    _client: Client | None
    clients: LocalClientStorage
    config: Config

    @utils.class_property
    def __signature__(cls) -> inspect.Signature:
        return utils.merge_signatures([
            inspect.signature(cls.__init__),
            inspect.signature(cls.setup)
        ])

    def __init__(
        self,
        request: fastapi.Request,
        config: Config = CurrentConfig,
        **kwargs: Any
    ) -> None:
        self._client = config.client
        self.config = config
        self.clients = LocalClientStorage()
        self.request = request
        self.setup(**kwargs)

    def setup(self, **kwargs: Any) -> None:
        pass

    def find(
        self,
        kind: type[pydantic.BaseModel],
        filters: Iterable[tuple[str, str, str]],
        sort: Iterable[str] | None = None
    ) -> AsyncIterable[pydantic.BaseModel]:
        raise NotImplementedError

    @contextlib.asynccontextmanager
    async def atomic(self, key: Any):
        obj = await self.get(key)
        try:
            yield obj
            await self.persist(obj)
        except Exception:
            raise

    async def allocate_identifier(self, cls: str | type) -> Any:
        raise NotImplementedError

    async def delete(self, obj: Any) -> None:
        raise NotImplementedError

    @functools.singledispatchmethod
    async def _get(self, key: Any) -> Any:
        if key is None:
            return None
        raise NotImplementedError(type(key).__name__)

    @_get.register
    async def _(self, key: AuthorizationKey) -> Authorization | None:
        return await self.get_authorization(key)

    @_get.register
    async def _(self, key: AuthorizationRequestKey) -> types.IAuthorizationRequest | None:
        return await self.get_authorization_request(key)

    @_get.register
    async def _(self, key: Client.Key) -> Client | None:
        if str(key) == 'self':
            return Client.model_validate({
                'client_id': 'self',
                'client_name': 'WebIAM Checkpoint',
                'redirect_uris': [str(self.request.url_for('user.welcome'))],
                'response_types': ['none'],
                'scope': ['openid', 'email', 'profile']
            })
        if self._client and self._client.id == key:
            return self._client
        return await self.clients.get(str(key)) or await self.get_client(key)

    @_get.register
    async def _(self, key: ClientAuthorizationStateKey) -> ClientAuthorizationState | None:
        return await self.get_authorization_state(key)

    @_get.register
    async def _(self, masked: MaskedPrincipal) -> Principal | None:
        return await self.get_principal(masked)

    @_get.register
    async def _(self, key: ResourceOwner.Key) -> IResourceOwner | None:
        return await self.get_resource_owner(key)

    @_get.register
    async def _(self, pk: SubjectKey) -> ISubject | None:
        return await self.get_subject_by_pk(pk)

    async def get(self, key: ResourceIdentifier[Any, T]) -> T | None:
        try:
            return await self._get(key)
        except LookupError:
            return None

    async def get_authorization(self, key: AuthorizationKey) -> Authorization | None:
        raise NotImplementedError

    async def get_authorization_request(self, key: AuthorizationRequestKey) -> types.IAuthorizationRequest | None:
        raise NotImplementedError

    async def get_authorization_state(self, key: ClientAuthorizationStateKey) -> Any:
        raise NotImplementedError

    async def get_client(self, key: Client.Key) -> Client | None:
        raise NotImplementedError

    async def get_principal(self, masked: MaskedPrincipal) -> Principal | None:
        raise NotImplementedError

    async def get_resource_owner(self, key: ResourceOwner.Key) -> IResourceOwner | None:
        raise NotImplementedError

    async def get_subject_by_pk(self, pk: SubjectKey) -> ISubject | None:
        raise NotImplementedError

    async def get_subject_by_principal(self, masked: MaskedPrincipal) -> ISubject | None:
        raise NotImplementedError

    async def mask(self, obj: Any) -> Any:
        raise NotImplementedError

    async def persist(self, object: Any) -> None:
        return await self._persist(object)

    async def persist_authorization(self, authorization: Authorization) -> None:
        raise NotImplementedError

    async def persist_authorization_request(self, request: AuthorizationRequest) -> None:
        raise NotImplementedError

    async def persist_authorization_state(
            self,
            state: ClientAuthorizationState
    ) -> None:
        raise NotImplementedError

    async def persist_client(self, client: Client) -> None:
        raise NotImplementedError

    async def persist_receipt(self, receipt: Receipt) -> None:
        raise NotImplementedError

    async def persist_resource_owner(self, owner: ResourceOwner) -> None:
        raise NotImplementedError

    async def persist_principal(self, principal: Principal) -> None:
        raise NotImplementedError

    async def persist_subject(self, subject: Subject) -> None:
        raise NotImplementedError

    @functools.singledispatchmethod
    async def _persist(self, object: Any) -> None:
        raise NotImplementedError

    @_persist.register
    async def _(self, authorization: Authorization) -> None:
        return await self.persist_authorization(authorization)

    @_persist.register
    async def _(self, request: AuthorizationRequest) -> None:
        return await self.persist_authorization_request(request)

    @_persist.register
    async def _(self, client: Client) -> None:
        return await self.persist_client(client)

    @_persist.register
    async def _(self, state: ClientAuthorizationState) -> None:
        return await self.persist_authorization_state(state)

    @_persist.register
    async def _(self, principal: Principal) -> None:
        return await self.persist_principal(principal)

    @_persist.register
    async def _(self, receipt: Receipt) -> None:
        return await self.persist_receipt(receipt)

    @_persist.register
    async def _(self, owner: ResourceOwner) -> None:
        return await self.persist_resource_owner(owner)

    @_persist.register
    async def _(self, subject: Subject) -> None:
        return await self.persist_subject(subject)