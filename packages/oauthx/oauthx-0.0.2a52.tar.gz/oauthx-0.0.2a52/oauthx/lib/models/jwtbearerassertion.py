# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Literal

from aiopki.types import ISigner
from aiopki.ext import jose
from aiopki.ext.jose import CompactSerialized
from aiopki.ext.jose import JWT

from .baseassertion import BaseAssertion


class JWTBearerAssertion(BaseAssertion):
    grant_type: Literal['urn:ietf:params:oauth:grant-type:jwt-bearer']
    assertion: CompactSerialized

    @classmethod
    async def new(
        cls,
        signer: ISigner,
        iss: str,
        sub: str,
        token_endpoint: str,
        ttl: int = 15,
        **claims: Any
    ) -> 'JWTBearerAssertion':
        jwt = JWT.new(
            ttl=ttl,
            aud=token_endpoint,
            iss=iss,
            sub=sub,
            **claims
        )
        jws = jose.jws(jwt.model_dump())
        await jws.sign(signer.default_algorithm(), signer)
        return cls.model_validate({
            'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
            'assertion': jws
        })

    def must_authenticate(self) -> bool:
        return False

    def must_identify(self) -> bool:
        return False