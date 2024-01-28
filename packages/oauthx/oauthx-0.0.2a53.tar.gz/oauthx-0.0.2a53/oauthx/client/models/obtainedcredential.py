# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import httpx
import pydantic
from canonical import PersistedModel

from oauthx.client.exceptions import AuthorizationRequired
from oauthx.client.protocols import IClient
from oauthx.lib.exceptions import Error


class ObtainedCredential(PersistedModel):
    client_id: str = pydantic.Field(
        default=...
    )

    name: str = pydantic.Field(
        default=...
    )
    
    access_token: str = pydantic.Field(
        default=...
    )
    
    refresh_token: str | None = pydantic.Field(
        default=None
    )

    @property
    def pk(self) -> str:
        return self.name

    def add_to_request(self, request: httpx.Request) -> None:
        request.headers['Authorization'] = f'Bearer {self.access_token}'

    async def destroy(self) -> None:
        await self.delete()

    async def refresh(self, client: IClient) -> None:
        if self.refresh_token is None:
            raise AuthorizationRequired
        try:
            grant = await client.refresh(self.refresh_token)
        except Error:
            raise AuthorizationRequired
        if grant.refresh_token is None:
            raise AuthorizationRequired
        self.access_token = str(grant.access_token)
        self.refresh_token = grant.refresh_token