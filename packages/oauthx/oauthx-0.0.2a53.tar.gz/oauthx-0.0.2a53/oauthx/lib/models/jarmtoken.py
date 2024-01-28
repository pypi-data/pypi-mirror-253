# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

import pydantic
from aiopki.ext.jose import CompactSerialized
from aiopki.ext.jose import JWT
from aiopki.lib import JSONWebKeySet
from aiopki.types import IDecrypter

from .error import Error
from .jarmauthorizationresponse import JARMAuthorizationResponse


class JARMToken(pydantic.BaseModel):
    response: CompactSerialized

    def is_valid(self, issuer: str, client_id: str, jwt: JWT) -> bool:
        return all([
            jwt.validate_iss(issuer),
            jwt.validate_aud(client_id),
            jwt.validate_exp(),
            jwt.validate_iat(max_age=300, required=False),
            jwt.validate_nbf(required=False),
        ])

    def raise_for_status(self):
        pass

    async def decrypt(self, decrypter: IDecrypter) -> None:
        if not decrypter.can_decrypt():
            raise TypeError(f'{type(decrypter).__name__} can not decrypt.')
        await self.response.decrypt(decrypter)

    async def decode(
        self,
        issuer: str,
        client_id: str,
        verifier: JSONWebKeySet,
        decrypter: IDecrypter
    ) -> JARMAuthorizationResponse | Error:
        if self.response.is_encrypted():
            await self.decrypt(decrypter)
        if not await self.response.verify(verifier):
            raise TypeError
        jwt = self.response.payload(factory=JWT.model_validate)
        if not self.is_valid(issuer, client_id, jwt):
            raise NotImplementedError
        if jwt.claims.get('error'):
            return Error.model_validate(jwt.model_dump())
        return JARMAuthorizationResponse.model_validate(jwt.model_dump())