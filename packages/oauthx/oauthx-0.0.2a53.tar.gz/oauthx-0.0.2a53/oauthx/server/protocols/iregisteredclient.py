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
from typing import ClassVar
from typing import MutableMapping
from typing import Protocol

import httpx
from aiopki.ext.jose import JOSEObject
from aiopki.ext.jose import OIDCToken
from fastapi.security import HTTPBasicCredentials

from oauthx.lib.types import GrantType
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import ResponseType
from .iclient import IClient


class IRegisteredClient(Protocol):
    __module__: str = 'oauthx.lib.protocols'
    Key: ClassVar[type[IClient.Key]] = IClient.Key

    @property
    def id(self) -> str:
        ...

    def allows_delegation_to(self, userinfo: OIDCToken) -> bool:
        """Return a boolean indicating if the client allows delegation to
        the given identity.
        """
        ...

    def allows_response_type(self, response_type: ResponseType | None) -> bool:
        """Return a boolean indicating if the client allows the given
        response type.
        """
        ...

    def allows_scope(self, scope: set[str]) -> bool:
        """Return a boolean indicating if the client allows the
        given scope.
        """
        ...

    def can_redirect(self, redirect_uri: RedirectURI | None) -> bool:
        """Return a boolean indicating if the client allows
        redirection to the given `redirect_uri`.
        """
        ...

    def can_grant(self, grant_type: GrantType | None) -> bool:
        """Return a boolean indicating if the client allows the given
        `grant_type`.
        """
        ...

    def contribute_to_event(self, data: MutableMapping[str, Any]) -> None:
        """Adds properties to an event that involves the client."""
        ...

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        """Adds properties to a :class:`UserInfo` instance."""
        ...

    def get_default_redirect_uri(self) -> RedirectURI:
        """Return a string containing the default redirect URI for the client,
        if any.
        """
        ...

    def get_display_name(self) -> str:
        """Return a string containing the display name of the client as
        shown in the user interface.
        """
        ...

    def get_logo_url(self) -> str:
        """Return a string containing the logo URL of the client."""
        ...

    def get_sector_identifier(self) -> str:
        """Return a string containing the :term:`Sector Identifier` of the
        client.
        """
        ...

    def has_redirection_endpoints(self) -> bool:
        """Return a boolean indicating if the client has configured any
        redirection endpoints.
        """
        ...

    def is_confidential(self) -> bool:
        """Return a boolean indicating if the client is confidential."""
        ...

    def must_push(self) -> bool:
        """Return a boolean indicating if the client is required to
        push authorization requests.
        """
        ...

    def requires_state(self) -> bool:
        """Return a boolean indicating if the client enforces the use
        of the ``state`` parameter in authorization requests.
        """
        ...

    def resource_owner(self, subject: Any) -> Any:
        """Create a resource owner identifier."""
        ...

    def update_key(self, update: Callable[[bytes], None]):
        """Update the clients' key that is used to secure its
        security credentials, such as authorization codes and
        refresh tokens. Updating the key effectively revokes
        all security credentials for the client.
        """
        ...

    async def authenticate(self, credential: HTTPBasicCredentials | JOSEObject | str | None) -> None:
        """Authenticate the client using the given credential.
        """
        ...

    async def userinfo(self, access_token: str, http: httpx.AsyncClient | None = None) -> None:
        """Query the providers' UserInfo endpoint to obtain information
        about the resource owner.
        """
        ...