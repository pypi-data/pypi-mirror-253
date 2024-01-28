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

from canonical import ResourceIdentifier


T = TypeVar('T')


class IClientAuthorizationState(Protocol):
    __module__: str = 'oauthx.types'
    client_id: str

    class Key(ResourceIdentifier[str, 'IClientAuthorizationState']):
        state: str
        openapi_example: str = 'EwzP5eWNArizDvJdO95fuyoKuLDpoYmOx2ZGuqudqWTZy7QlSxxkXyx2fNwhjjI8'
        openapi_title: str = 'State'

        def __init__(self, state: str):
            self.state = state

        def cast(self) -> str:
            return str(self.state)

        def __str__(self) -> str:
            return self.state
        
        def __eq__(self, key: object) -> bool:
            return isinstance(key, type(self)) and key.state == self.state

        def __hash__(self) -> int:
            return hash(self.state)

    @property
    def key(self) -> Key:
        ...

    @property
    def pk(self) -> Key:
        return self.Key(self.client_id)

    def annotate(self, key: str, value: Any) -> None: ...
    def annotation(self, key: str, decoder: Callable[[Any], T] = lambda x: x) -> T | None: ...
    def get_authorize_url(self) -> str: ...