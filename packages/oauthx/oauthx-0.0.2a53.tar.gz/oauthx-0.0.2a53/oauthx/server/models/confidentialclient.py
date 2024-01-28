# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
import secrets
from typing import Any

import pydantic
from aiopki.ext.jose import JWA
from aiopki.ext.jose import JOSEObject
from aiopki.lib import JSONWebKeySet
from canonical import ResourceName
from fastapi.security import HTTPBasicCredentials

from oauthx.lib.models.assertion import Assertion
from .baseclient import BaseClient


class ConfidentialClient(BaseClient):
    credential: JSONWebKeySet | ResourceName | str = pydantic.Field(
        default=...,
        alias='client_secret'
    )
    
    # JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
    authorization_encrypted_response_alg: JWA | None = pydantic.Field(
        default=None
    )
    
    authorization_encrypted_response_enc: JWA | None = pydantic.Field(
        default=None
    )

    model_config = {
        'populate_by_name': True
    }

    def can_encrypt(self) -> bool:
        return isinstance(self.credential, JSONWebKeySet)

    def model_post_init(self, _: Any) -> None:
        if self.authorization_encrypted_response_enc\
        and not self.authorization_encrypted_response_alg:
            raise ValueError(
                "the authorization_encrypted_response_alg parameter "
                "is required."
            )
        if self.authorization_encrypted_response_alg\
        and not self.authorization_encrypted_response_enc:
            self.authorization_encrypted_response_enc = JWA.a128cbc_hs256

        # If the client wants to encrypt, then the credential must be
        # a JSONWebKeySet instance.
        if self.wants_encryption() and not isinstance(self.credential, JSONWebKeySet):
            raise ValueError(f"{type(self.credential)} can not encrypt.")

    def wants_encryption(self) -> bool:
        """Return a boolean indicating if the client implements encryption."""
        return any([
            self.authorization_encrypted_response_alg
        ])

    @functools.singledispatchmethod
    async def authenticate(
        self,
        _: Assertion | JOSEObject | HTTPBasicCredentials | str | None
    ) -> bool:
        return False

    @authenticate.register
    async def _(self, jws: JOSEObject) -> bool:
        return isinstance(self.credential, JSONWebKeySet) and await jws.verify(self.credential)

    @authenticate.register
    async def _(self, credential: str) -> bool:
        assert isinstance(self.credential, str)
        return secrets.compare_digest(credential, self.credential)