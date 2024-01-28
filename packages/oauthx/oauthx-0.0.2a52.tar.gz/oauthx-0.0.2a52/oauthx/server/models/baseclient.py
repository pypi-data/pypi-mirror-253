# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
import secrets
import urllib.parse
from typing import Any
from typing import Callable
from typing import Literal
from typing import MutableMapping

import pydantic
from aiopki.types import Base64
from aiopki.ext.jose import JOSEObject
from aiopki.ext.jose import JWA
from aiopki.ext.jose import OIDCToken
from canonical.security import DomainACL
from fastapi.security import HTTPBasicCredentials

from oauthx.lib.types import GrantType
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import ResponseType
from oauthx.lib.types import SectorIdentifierURI
from oauthx.server.protocols import IRequestSubject
from oauthx.server.protocols import IResourceOwner
from oauthx.server.types import MissingRedirectURI
from oauthx.lib  import ClientAuthorizationState
from oauthx.lib  import Provider
from .clientacl import ClientACL
from .clientprovider import ClientProvider


class BaseClient(pydantic.BaseModel):
    client_id: str
    client_name: str
    grant_types: list[str] = []
    key: Base64 = pydantic.Field(default_factory=lambda: secrets.token_bytes(32))
    redirect_uris: list[RedirectURI] = []
    response_types: list[ResponseType] = []
    scope: set[str] = set()
    require_pushed_authorization_requests: bool = False
    token_endpoint_auth_method: Any = None

    # RFC 7591 OAuth 2.0 Dynamic Client Registration Protocol
    logo_url: str | None = pydantic.Field(
        default=None
    )

    # OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
    sector_identifier_uri: SectorIdentifierURI | None = None
    subject_type: Literal['public', 'pairwise'] = 'pairwise'
    
    # JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
    authorization_signed_response_alg: JWA = pydantic.Field(
        default=JWA.rs256
    )

    # Custom properties not specified by OAuth 2.x/OpenID Connect standards.
    acl: ClientACL = pydantic.Field(
        default_factory=ClientACL.null
    )

    audience: Literal['personal', 'institutional'] | None = pydantic.Field(
        default=None
    )

    domains: DomainACL = pydantic.Field(
        default_factory=DomainACL.null
    )
    
    providers: list[ClientProvider] = pydantic.Field(
        default_factory=list
    )
    
    splash_image_url: str = pydantic.Field(
        default='https://static.webiam.id/shared/splash.jpg'
    )

    @property
    def id(self) -> str:
        return self.client_id

    @property
    def provider(self) -> Provider:
        raise NotImplementedError

    @property
    def sector_identifier(self) -> str:
        hostnames = {p.hostname or '' for p in map(urllib.parse.urlparse, self.redirect_uris)}
        if (not hostnames or len(hostnames) > 1) and not self.sector_identifier_uri:
            raise NotImplementedError
        if self.sector_identifier_uri:
            return self.sector_identifier_uri.sector
        else:
            return hostnames.pop()

    def allows_delegation_to(self, userinfo: OIDCToken) -> bool:
        return self.acl.has_access(userinfo)

    def allows_response_type(self, response_type: ResponseType) -> bool:
        return response_type in self.response_types

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        userinfo['azp'] = str(self.id)
        userinfo['aud'] = str(self.id)

    def model_post_init(self, _: Any) -> None:
        if ('authorization_code' in self.grant_types) and not self.redirect_uris:
            raise ValueError("At least one redirect URI must be specified.")

    @functools.singledispatchmethod
    async def authenticate(self, credential: JOSEObject | HTTPBasicCredentials | str | None) -> bool:
        return False

    async def authorize(self, **kwargs: Any) -> ClientAuthorizationState:
        raise NotImplementedError

    async def authorization_code(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def allows_scope(self, scope: set[str]) -> bool:
        return scope <= self.scope

    def can_grant(self, grant_type: GrantType | None) -> bool:
        """Return a boolean indicating if the client allows the given
        `grant_type`.
        """
        return any([
            grant_type is None,
            grant_type in self.grant_types
        ])

    def can_redirect(self, redirect_uri: RedirectURI | None) -> bool:
        return redirect_uri is None or any([x.can_redirect(redirect_uri) for x in self.redirect_uris])

    def is_confidential(self) -> bool:
        return True

    def get_audience(self) -> str | None:
        return self.audience

    def get_default_redirect_uri(self) -> RedirectURI:
        if not self.redirect_uris:
            raise MissingRedirectURI
        return self.redirect_uris[0]

    def get_display_name(self) -> str:
        return self.client_name

    def get_logo_url(self) -> str | None:
        return self.logo_url

    def get_splash_image_url(self) -> str:
        return self.splash_image_url

    def get_providers(self):
        return self.providers

    def get_sector_identifier(self) -> str:
        return self.sector_identifier

    def has_redirection_endpoints(self) -> bool:
        return len(self.redirect_uris) > 0

    def must_push(self) -> bool:
        return self.require_pushed_authorization_requests

    def requires_state(self) -> bool:
        return False

    def resource_owner(self, subject: IRequestSubject) -> IResourceOwner.Key:
        return IResourceOwner.Key(self.client_id, str(subject.id)) # type: ignore

    def update_key(self, update: Callable[[bytes], None]) -> None:
        update(self.key)

    def wants_encryption(self) -> bool:
        return False