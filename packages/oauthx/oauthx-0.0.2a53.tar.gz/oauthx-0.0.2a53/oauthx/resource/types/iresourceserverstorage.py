# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Protocol

from oauthx.lib.types import AccessTokenHash
from ..models import TokenSubject


class IResourceServerStorage(Protocol):
    __module__: str = 'oauthx.resource'


    async def get_token_subject(self, at_hash: AccessTokenHash) -> TokenSubject | None:
        ...