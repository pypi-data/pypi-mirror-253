# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import secrets
from typing import Any
from typing import Literal

import aiopki
import fastapi
import pydantic
from aiopki.ext import jose
from aiopki.lib import JSONWebKeySet

from oauthx.lib.types import GrantType
from .baseresponsemode import BaseResponseMode


class QueryResponseMode(BaseResponseMode):
    response_mode: Literal['query', 'jwt', 'query.jwt']
    response_type: Literal['code', 'code id_token', 'none']

    @property
    def grant_type(self) -> GrantType | None:
        return 'authorization_code' if self.response_type != 'none' else None

    @pydantic.field_validator('response_mode', mode='before')
    def preprocess_response_mode(cls, value: str | None) -> str:
        if value is None:
            value = 'query'
        return value

    def get_responses(self) -> set[str]:
        return {x for x in str.split(self.response_type, ' ')}

    async def deny(self) -> str:
        return self.get_redirect_uri().redirect(
            mode='query',
            error='access_denied',
            state=self.state,
            iss=self.iss
        )

    async def error(
        self,
        *,
        error: str,
        error_description: str | None = None,
        error_uri: str | None = None
    ) -> str:
        redirect_uri = self.get_redirect_uri()
        return redirect_uri.redirect(
            False,
            mode='query',
            error=error,
            error_description=error_description,
            error_uri=error_uri,
            state=self.state,
            iss=self.iss
        )

    async def redirect(self, signer: aiopki.CryptoKeyType, **kwargs: Any) -> fastapi.responses.RedirectResponse:
        if self.response_type == 'none':
            kwargs = {}
        kwargs.update({
            'iss': self.iss,
            'state': self.state
        })
        if self.response_mode in {'query.jwt', 'jwt'}:
            kwargs = {
                'response': await self.sign(signer, **kwargs)
            }
        return fastapi.responses.RedirectResponse(
            status_code=302,
            url=self.get_redirect_uri().redirect(False, mode='query', **kwargs)
        )

    async def sign(
        self,
        signer: aiopki.CryptoKeyType,
        **claims: Any
    ) -> str:
        now = datetime.datetime.now(datetime.timezone.utc)
        jws = jose.jws({
            **claims,
            'jti': secrets.token_urlsafe(32),
            'aud': self.client.id,
            'exp': now + datetime.timedelta(seconds=60),
            'nbf': now,
            'iat': now,
        })
        await jws.sign(signer.default_algorithm(), signer)
        if self.client.wants_encryption():
            assert isinstance(self.client.credential, JSONWebKeySet)
            assert self.client.credential.can_encrypt()
            await jws.encrypt(
                encrypter=self.client.credential
            )
        return jws.encode(encoder=bytes.decode, compact=True)