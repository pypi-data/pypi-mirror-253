# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os
from typing import Iterable

from oauthx.client.models import Client
from oauthx.lib.params import HTTPClient
from .clientresolver import ClientResolver
from .models import Client


class DefaultClient(ClientResolver):
    __module__: str = 'oauthx.client'
    client: Client | None = None

    def __init__(
        self,
        scope: Iterable[str] | None = None
    ):
        self.scope = scope

    async def get(self, client_id: str) -> Client:
        assert self.client is not None
        return self.client

    async def resolve(self, http: HTTPClient) -> Client: # type: ignore
        if self.client is None:
            self.client = Client.model_validate({
                'provider': os.getenv('OAUTH2_ISSUER'),
                'client_id': os.getenv('OAUTH2_CLIENT_ID'),
                'scope': self.scope
            })
            await self.client.discover(http=http)
        return self.client