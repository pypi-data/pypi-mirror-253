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

from canonical import ResourceIdentifier


class IRequestSession(Protocol):
    __module__: str = 'oauthx.types'

    class Key(ResourceIdentifier[str, 'IRequestSession']):
        session_id: str
        openapi_example: str = 'client-123'
        openapi_title: str = 'Session ID'

        def __init__(self, session_id: str):
            self.session_id = session_id

        def __str__(self) -> str:
            return self.session_id
        
        def __eq__(self, key: object) -> bool:
            return isinstance(key, type(self)) and key.session_id == self.session_id

    def authenticate(self, sub: str, email: str | None) -> None:
        """Authenticates the session as the given subject."""
        ...

    def claims(self) -> dict[str, Any]:
        """Return a dictionary holding the claims in the session."""
        ...

    def is_dirty(self) -> bool:
        """Return a boolean indicating if the session is dirty."""
        ...

    def logout(self) -> None:
        """Logout the session, if it is authenticated."""
        ...

    def set(self, key: str, value: Any) -> None:
        """Set a key to the session with the given value, and mark the
        session as dirty.
        """
        ...