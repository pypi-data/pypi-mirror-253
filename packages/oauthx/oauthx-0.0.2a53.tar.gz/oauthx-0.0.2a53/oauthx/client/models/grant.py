# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import re
from typing import Any
from typing import Union

import pydantic

from oauthx.lib.types import GrantType
from .authorizationcodegrant import AuthorizationCodeGrant
from .clientcredentialsgrant import ClientCredentialsGrant
from .jwtbearergrant import JWTBearerGrant
from .refreshtokengrant import RefreshTokenGrant
from .tokenexchangegrant import TokenExchangeGrant


__all__: list[str] = [
    'Grant'
]


_GrantType = Union[
    AuthorizationCodeGrant,
    ClientCredentialsGrant,
    JWTBearerGrant,
    RefreshTokenGrant,
    TokenExchangeGrant
]


class Grant(pydantic.RootModel[_GrantType]):
    root: _GrantType

    @property
    def grant_type(self) -> GrantType:
        return self.root.grant_type

    @property
    def scope(self) -> set[str]:
        if isinstance(self.root.scope, set):
            return self.root.scope
        return set(filter(bool, re.split(r'\s+', self.root.scope or '')))

    def has_credentials(self) -> bool:
        """Return a boolean indicating if client credentials were
        supplied with the grant.
        """
        return self.root.has_credentials()

    def must_authenticate(self) -> bool:
        """Return a boolean if the client must always authenticate when
        using this grant.
        """
        return self.root.must_authenticate()

    def must_identify(self) -> bool:
        """Return a boolean if the client must identify when
        using this grant.
        """
        return self.root.must_identify()

    async def decrypt(self, keychain: Any):
        pass