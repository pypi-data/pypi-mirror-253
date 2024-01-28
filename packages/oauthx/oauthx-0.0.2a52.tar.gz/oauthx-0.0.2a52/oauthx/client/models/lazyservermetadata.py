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

from oauthx.lib import utils
from .servermetadata import ServerMetadata


class LazyServerMetadata(pydantic.BaseModel):
    iss: str
    metadata_url: str | None = None


    @utils.http
    async def discover(self, http: httpx.AsyncClient):
        metadata = None
        urls: list[str] = [
            f'{self.iss}/.well-known/oauth-authorization-server',
            f'{self.iss}/.well-known/openid-configuration'
        ]
        for url in urls:
            response = await http.get(url)
            if response.status_code == 404:
                continue
            response.raise_for_status()
            metadata = ServerMetadata.model_validate(response.json())
            await metadata.discover(http=http)
            break
        if metadata is None:
            raise NotImplementedError
        return metadata
    
    async def _discover(self):
        return await self.discover()

    def __await__(self):
        return self._discover().__await__()