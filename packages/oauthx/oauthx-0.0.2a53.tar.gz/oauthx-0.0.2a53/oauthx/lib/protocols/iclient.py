# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Callable
from typing import Protocol

import httpx
from aiopki.ext.jose import JOSEObject
from fastapi.security import HTTPBasicCredentials


class IClient(Protocol):
    __module__: str = 'oauthx.lib.protocols'

    @property
    def id(self) -> str:
        ...

    def is_confidential(self) -> bool:
        """Return a boolean indicating if the client is confidential."""
        ...

    def update_key(self, update: Callable[[bytes], None]):
        """Update the clients' key that is used to secure its
        security credentials, such as authorization codes and
        refresh tokens. Updating the key effectively revokes
        all security credentials for the client.
        """
        ...

    async def authenticate(self, credential: HTTPBasicCredentials | JOSEObject | str | None) -> None:
        """Authenticate the client using the given credential.
        """
        ...

    async def userinfo(self, access_token: str, http: httpx.AsyncClient | None = None) -> None:
        """Query the providers' UserInfo endpoint to obtain information
        about the resource owner.
        """
        ...