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


class IAuthorizationRouter(Protocol):
    __module__: str = 'oauthx.server.types'
    
    def add_plugin(
        self,
        *,
        methods: list[str],
        path: str,
        handler: type,
        method: Callable[..., Any],
        name: str,
        description: str,
        authenticated: bool = True,
        needs_data: bool = False
    ) -> None:
        ...

    def register_template_module(self, qualname: str) -> None:
        ...

    def register_scope(
        self,
       name: str,
       cls: type
    ) -> None:
        ...