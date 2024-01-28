# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Callable
from typing import Protocol
from typing import TypeVar


T = TypeVar('T')


class IClientAuthorizationState(Protocol):
    __module__: str = 'oauthx.client.protocols'

    @property
    def pk(self) -> str:
        ...

    def annotation(self, name: str, decoder: Callable[[Any], T] = lambda x: x) -> T | None: ...
    def get_authorize_url(self) -> str: ...
    def redirect(self, request_factory: Callable[..., T]) -> T: ...