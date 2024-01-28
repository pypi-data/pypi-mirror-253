# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.client.models import Client
from oauthx.client.models import ClientAuthorizationState
from oauthx.client.models import ObtainedCredential
from oauthx.client.protocols import IClientStorage
from oauthx.client import LocalClientRepository

from .basedatastorestorage import BaseDatastoreStorage


class ClientRepository(
    IClientStorage[Client, ClientAuthorizationState, ObtainedCredential],
    BaseDatastoreStorage
):
    local: LocalClientRepository = LocalClientRepository()

    async def get_client(self, client_id: str):
        return await self.local.one(client_id)

    async def get_credential(
        self,
        client_id: str,
        resource: str | None = None
    ) -> ObtainedCredential | None:
        return await self.get_model_by_key(ObtainedCredential, client_id)

    async def get_state(self, state: str) -> ClientAuthorizationState | None:
        return await self.get_model_by_key(ClientAuthorizationState, state)

    async def persist(self, obj: Client | ClientAuthorizationState | ObtainedCredential) -> None:
        await self.put(obj, obj.pk)