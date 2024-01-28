# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Iterable
from typing import Protocol
from typing import TypeVar

import httpx

from oauthx.lib.models import ObtainedGrant
from oauthx.lib.types import PrompType
from oauthx.lib.types import ResponseType
from oauthx.lib import utils
from .iclientauthorizationstate import IClientAuthorizationState


T = TypeVar('T')


class IClient(Protocol):
    __module__: str = 'oauthx.client.protocols'

    @property
    def pk(self) -> str:
        ...

    async def authorize(
        self,
        *,
        redirect_uri: str | None = None,
        scope: Iterable[str] | None = None,
        response_type: ResponseType | None = None,
        state_class: type[T] = IClientAuthorizationState,
        prompt: Iterable[PrompType] = [],
        annotations: dict[str, str] | None = None,
        **params: Any
    ) -> T:
        ...

    async def authorization_code(
        self,
        params: Any,
        state: Any,
        http: httpx.AsyncClient | None = None,
        resources: str | list[str] | None = None
    ) -> ObtainedGrant: ...

    @utils.http
    async def refresh(
        self,
        http: httpx.AsyncClient,
        refresh_token: str,
        scope: Iterable[str] | None = None,
        resources: list[str] | None = None,
        resource: str | None = None
    ) -> ObtainedGrant:
        ...