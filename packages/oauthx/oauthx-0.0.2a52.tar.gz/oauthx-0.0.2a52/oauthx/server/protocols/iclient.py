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
from typing import MutableMapping

import httpx
from aiopki.ext.jose import JOSEObject
from canonical import ResourceIdentifier
from fastapi.security import HTTPBasicCredentials

from oauthx.lib.types import GrantType
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import ResponseType
from .irequestsubject import IRequestSubject
from .iresourceowner import IResourceOwner


class IClient(Protocol):
    __module__: str = 'oauthx.types'

    @property
    def id(self) -> str:
        ...

    def allows_response_type(self, response_type: ResponseType) -> bool:
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

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        ...

    def get_default_redirect_uri(self) -> RedirectURI:
        """Return a string containing the default redirect URI for the
        client. Raise :exc:`NotImplementedError` if the client can not
        redirect.
        """
        ...

    def get_display_name(self) -> str:
        """Return a string containing the display name of the client."""
        ...

    def get_logo_url(self) -> str:
        """Return a string containing the logo URL of the client."""
        ...

    def get_sector_identifier(self) -> str: ...

    def is_confidential(self) -> bool:
        """Return a boolean indicating if the client is confidential."""
        ...

    def must_push(self) -> bool:
        """Return a boolean indicating if the client is required to
        push authorization requests.
        """
        ...

    def resource_owner(self, subject: IRequestSubject) -> IResourceOwner.Key:
        """Create a resource owner identifier."""
        ...

    def requires_state(self) -> bool:
        """Return a boolean indicating if the client enforces the use
        of the ``state`` parameter in authorization requests.
        """
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

    class Key(ResourceIdentifier[str, 'IClient']):
        client_id: str
        openapi_example: str = 'client-123'
        openapi_title: str = 'Client ID'

        def __init__(self, client_id: str):
            self.client_id = client_id

        def cast(self) -> str:
            return str(self.client_id)

        def __str__(self) -> str:
            return self.client_id
        
        def __eq__(self, key: object) -> bool:
            return isinstance(key, type(self)) and key.client_id == self.client_id