# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Protocol

from oauthx.lib.protocols import IStorage


class IAuthorization(Protocol):
    __module__: str = 'oauthx.server.types'

    @property
    def pk(self) -> Any:
        ...

    async def consume(self, storage: IStorage) -> None:
        """Consume the :class:`IAuthorization` and mark its
        authorization code as used.
        """
        ...

    def is_consumed(self) -> bool:
        """Return a boolean indicating if the :class:`IAuthorization`
        is consumed i.e. it's authorization code was exchanged.
        """
        ...