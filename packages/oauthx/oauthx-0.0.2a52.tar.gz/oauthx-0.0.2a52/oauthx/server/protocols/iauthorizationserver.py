# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Literal
from typing import Protocol

from aiopki.ext.jose import OIDCToken

from oauthx.lib.types import RedirectURI
from oauthx.lib.types import OIDCIssuerIdentifier
from .iregisteredclient import IRegisteredClient
from .iresourceowner import IResourceOwner
from .iresponsemode import IResponseMode
from .isubject import ISubject
from .iuserinfocontributor import IUserInfoContributor


class IAuthorizationServer(Protocol):
    """Specifies the interface for a concrete implementation of an
    OAuth 2.x/OpenID Connect authorization server.
    """
    __module__: str = 'oauthx.types'
    
    #: Raised when a set of principals resolves to multiple subjects.
    AmbiguousPrincipal: type[Exception] = type(
        'AmbiguousPrincipal', (Exception,), {}
    )

    #: Raised when we receive an assertion that is not trusted.
    UntrustedAssertion: type[Exception] = type(
        'UntrustedAssertion', (Exception,), {}
    )
    
    #: Raised when a Principal is orphaned.
    OrphanedPrincipal: type[Exception] = type(
        'OrphanedPrincipal', (Exception,), {}
    )

    async def authorize(
        self,
        client: IRegisteredClient,
        userinfo: OIDCToken,
        params: Any,
        mode: IResponseMode,
        contributors: list[IUserInfoContributor] = []
    ) -> dict[str, str]:
        ...

    async def get_subject(self, pk: Any) -> ISubject | None:
        """Return the subject identified by the primary key."""
        ...

    async def issue_authorization_code(
        self,
        client: IRegisteredClient,
        owner: IResourceOwner,
        authorization_id: int,
        redirect_uri: RedirectURI | None = None
    ) -> str:
        """Issue an authorization code that the client can use to obtain
        an access token.
        """
        ...

    async def onboard_oidc(
        self,
        token: OIDCToken,
        use: Literal['personal', 'institutional'],
        request_id: int | None = None,
        client_id: str | None = None
    ) -> tuple[ISubject, bool]:
        """Onboard or retrieve a :class:`~oauthx.types.ISubject` using
        an OpenID Connect ID Token. Return a tuple containing the
        :class:`ISubject` instance and a boolean indicating if the
        subject was onboarded (it did not previously exist).
        
        Args:
            token (aiopki.ext.jose.OIDCToken): the OpenID Connect ID Token
                that was obtained at a trusted identity provider.

        Returns:
            :class:`tuple`

        Raises:
            :exc:`AmbiguousPrincipal`: the principals
                included in the ID Token resolved to multiple
                subjects.
            :exc:`OrphanedPrincipal`: the principals provided were known
                by the authorization server but could not resolve to
                a subject.
            :exc:`UntrustedAssertion`: the ID Token did not include
                any principals that were trusted by the authorization
                server.
        """
        ...

    async def register_principal(
        self,
        *,
        issuer: OIDCIssuerIdentifier,
        subject: ISubject,
        value: Any,
        created: bool = False,
        verified: bool = False
    ) -> None:
        """Registers the given principals for the subject."""
        ...