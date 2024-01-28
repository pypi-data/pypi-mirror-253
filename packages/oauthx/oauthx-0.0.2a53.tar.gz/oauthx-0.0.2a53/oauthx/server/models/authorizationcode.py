# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import hashlib

import pydantic
from aiopki.types import Base64
from aiopki.utils import b64encode

from oauthx.lib.protocols import IClient
from oauthx.server.protocols import IResourceOwner
from oauthx.server.types import AuthorizationKey
from oauthx.server.types import TokenMAC


class AuthorizationCode(pydantic.BaseModel):
    aut: int
    client_id: str
    mac: Base64
    redirect_uri: str | None = None
    sub: int | str

    @property
    def authorization(self) -> AuthorizationKey:
        return AuthorizationKey(self.aut)

    @property
    def owner(self) -> IResourceOwner.Key:
        return IResourceOwner.Key(self.client_id, str(self.sub))

    def allows_redirect(self, redirect_uri: str | None) -> bool:
        if redirect_uri is not None:
            redirect_uri = b64encode(
                    hashlib.sha3_256(str.encode(redirect_uri or '')).digest(),
                    encoder=bytes.decode
            )
        return any([
            self.redirect_uri is None,
            str(self.redirect_uri) == redirect_uri
        ])

    def is_authorized(self, client_id: str) -> bool:
        return self.client_id == client_id

    def is_revoked(self, client: IClient, owner: IResourceOwner) -> bool:
        mac = TokenMAC()
        mac.add(client)
        mac.add(owner)
        return bytes(mac) == self.mac