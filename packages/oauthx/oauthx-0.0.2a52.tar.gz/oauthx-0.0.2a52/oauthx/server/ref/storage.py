# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import operator
import secrets
from typing import Any
from typing import AsyncIterable
from typing import Callable
from typing import Iterable

import pydantic

from oauthx.lib.models import ClientAuthorizationState
from oauthx.lib.models import ClientAuthorizationStateKey
from oauthx.lib.types import MaskedPrincipal
from oauthx.server.models import Authorization
from oauthx.server.models import AuthorizationRequest
from oauthx.server.models import Client
from oauthx.server.models import Principal
from oauthx.server.models import ResourceOwner
from oauthx.server.models import Subject
from oauthx.server.models import SubjectKey
from oauthx.server.params import ContentEncryptionKey
from oauthx.server.protocols import IResourceOwner
from oauthx.server.protocols import ISubject
from oauthx.server.types import AuthorizationKey
from ..basestorage import BaseStorage


class Storage(BaseStorage):
    __module__: str = 'oauthx.server.ref'
    objects: dict[Any, Any] = {}
    operators: dict[str, Callable[..., bool]] = {
        '=': operator.eq
    }
    key: ContentEncryptionKey

    def setup(
        self,
        *,
        key: ContentEncryptionKey,
        **kwargs: Any) -> None:
        self.key = key
        self.objects = Storage.objects

    async def allocate_identifier(self, cls: str | type) -> int:
        return secrets.choice(range(10000000, 99999999))

    async def delete(self, obj: Any) -> None:
        self.objects.pop(obj.pk, None)

    async def find(
        self,
        kind: type[pydantic.BaseModel],
        filters: Iterable[tuple[str, str, str]],
        sort: Iterable[str] | None = None
    ) -> AsyncIterable[pydantic.BaseModel]:
        for obj in self.objects.values():
            if not isinstance(obj, kind):
                continue
            raise NotImplementedError
            yield obj
        return

    async def get_authorization(self, key: AuthorizationKey) -> Authorization | None:
        return self.objects[key]

    async def get_authorization_state(self, key: ClientAuthorizationStateKey) -> Any:
        return self.objects[key]

    async def get_client(self, key: Client.Key) -> Client | None:
        return Client.model_validate(self.objects[f'clients/{key.client_id}'])

    async def get_principal(self, masked: MaskedPrincipal) -> Principal | None:
        return self.objects[masked]

    async def get_resource_owner(self, key: IResourceOwner.Key) -> ResourceOwner | None:
        return self.objects[key]

    async def get_subject_by_pk(self, pk: SubjectKey) -> ISubject | None:
        subject = self.objects.get(pk)
        if subject is not None:
            await subject.decrypt_keys(self.key)
        return subject

    async def get_subject_by_principal(self, masked: MaskedPrincipal) -> ISubject | None:
        principal = self.objects.get(masked)
        if principal is None:
            return None
        subject = self.objects[SubjectKey(str(principal.owner))]
        if subject is not None:
            await subject.decrypt_keys(self.key)
        return subject

    async def persist_authorization(self, authorization: Authorization) -> None:
        self.objects[authorization.pk] = authorization

    async def persist_authorization_request(self, request: AuthorizationRequest) -> None:
        self.objects[request.pk] = request

    async def persist_authorization_state(self, state: ClientAuthorizationState) -> None:
        self.objects[state.pk] = state

    async def persist_client(self, client: Client) -> None:
        self.objects[f'clients/{client.root.client_id}'] = client

    async def persist_principal(self, principal: Principal) -> None:
        self.objects[principal.masked] = principal

    async def persist_resource_owner(self, owner: ResourceOwner) -> None:
        self.objects[owner.pk] = owner

    async def persist_subject(self, subject: Subject) -> None:
        await subject.encrypt_keys(self.key)
        self.objects[subject.get_primary_key()] = subject