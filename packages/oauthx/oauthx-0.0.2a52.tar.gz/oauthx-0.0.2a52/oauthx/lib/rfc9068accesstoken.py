# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import json

from aiopki.ext import jose
from aiopki.types import ISigner
from canonical import UnixTimestamp

from oauthx.lib.models import ClientKey
from oauthx.lib.types import ScopeType


class RFC9068AccessToken(jose.JWT):
    acr: str | None = None
    amr: str | None = None
    auth_time: UnixTimestamp | None = None
    client_id: ClientKey
    iss: str # type: ignore
    scope: ScopeType = ScopeType()
    sub: str # type: ignore

    async def sign(self, signer: ISigner) -> str:
        claims = json.loads(self.model_dump_json(exclude_defaults=True, exclude_none=True))
        jws = jose.jws(claims)
        await jws.sign(signer.default_algorithm(), signer, {'typ': 'at+jwt'})
        return jws.encode(encoder=bytes.decode)

    def is_client(self) -> bool:
        """Return a boolean indicating if the access token represents
        an OAuth 2.x/OpenID Connect client.
        """
        return self.client_id == self.sub

    def is_openid(self) -> bool:
        """Return a boolean indicating if the access token was issued
        to an OpenID Connect client.
        """
        return 'openid' in self.scope

    def validate_scope(self, scope: set[str]) -> bool:
        return scope <= self.scope