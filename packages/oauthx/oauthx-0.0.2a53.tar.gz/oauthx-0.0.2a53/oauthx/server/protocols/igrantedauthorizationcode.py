# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Protocol

from oauthx.lib.types import RedirectURI
from .iresourceowner import IResourceOwner


class IGrantedAuthorizationCode(Protocol):
    __module__: str = 'oauthx.types'
    value: str

    @property
    def owner(self) -> IResourceOwner.Key: ...

    def allows_redirect(self, redirect_uri: RedirectURI | None) -> bool: ...
    def consume(self) -> None: ...
    def is_authorized(self, client_id: str) -> bool: ...
    def is_consumed(self) -> bool: ...
    def has_consent(self, owner: IResourceOwner) -> bool: ...