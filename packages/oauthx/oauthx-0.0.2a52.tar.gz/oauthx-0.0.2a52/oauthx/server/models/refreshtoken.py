# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic
from aiopki.ext import jose
from aiopki.ext.jose import JWT
from aiopki.types import ISigner

from oauthx.server.types import AuthorizationKey
from .clientkey import ClientKey
from .resourceownerkey import ResourceOwnerKey


class RefreshToken(JWT):
    aut: int = pydantic.Field(
        default=...
    )

    client_id: ClientKey = pydantic.Field(
        default=...
    )

    @property
    def authorization(self) -> AuthorizationKey:
        return AuthorizationKey(self.aut)

    @property
    def owner(self) -> ResourceOwnerKey:
        assert self.sub is not None
        return ResourceOwnerKey(str(self.client_id), self.sub)

    async def sign(self, signer: ISigner) -> str:
        jws = jose.jws(self.model_dump(exclude_none=True))
        await jws.sign(
            algorithm=signer.default_algorithm(),
            signer=signer,
            protected={'typ': 'jwt+refresh-token'}
        )
        return jws.encode(compact=True, encoder=bytes.decode)