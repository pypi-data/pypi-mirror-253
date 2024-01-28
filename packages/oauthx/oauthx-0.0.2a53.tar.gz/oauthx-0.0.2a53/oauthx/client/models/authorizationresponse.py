# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pydantic

from .clientauthorizationstate import ClientAuthorizationState
from .error import Error
from .jarmtoken import JARMToken
from .jarmauthorizationresponse import JARMAuthorizationResponse
from .provider import Provider
from .redirectionparameters import RedirectionParameters


class AuthorizationResponse(pydantic.RootModel[Error | JARMToken | JARMAuthorizationResponse | RedirectionParameters]):

    @property
    def code(self):
        assert isinstance(self.root, RedirectionParameters)
        return self.root.code

    @property
    def iss(self) -> str | None:
        if not isinstance(self.root, RedirectionParameters):
            return None
        return self.root.iss

    def can_retry(self) -> bool:
        return isinstance(self.root, Error) and self.root.error in {
            'access_denied'
        }

    def is_error(self) -> bool:
        return isinstance(self.root, Error)

    def is_jarm(self) -> bool:
        return isinstance(self.root, JARMToken)

    def raise_for_status(self):
        return self.root.raise_for_status()

    async def decode(self, issuer: str, client_id: str, verifier: Any, decrypter: Any):
        if isinstance(self.root, JARMToken):
            self.root = await self.root.decode(issuer, client_id, verifier, decrypter)

    async def verify(self, provider: Provider, state: ClientAuthorizationState):
        self.root.raise_for_status()
        assert isinstance(self.root, RedirectionParameters)
        await state.verify(self.root)
        await provider.verify(self.root)