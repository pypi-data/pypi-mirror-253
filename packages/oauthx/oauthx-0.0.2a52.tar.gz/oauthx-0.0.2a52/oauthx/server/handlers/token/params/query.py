# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import fastapi
from aiopki.ext.jose import CompactSerialized

from oauthx.lib.types import GrantType
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import ScopeType


__all__: list[str] = [
    'CLIENT_ID',
    'CLIENT_SECRET',
    'CODE',
    'GRANT_TYPE',
    'REDIRECT_URI',
]


ASSERTION: CompactSerialized | None = fastapi.Form(
    default=None,
    description=(
        "A compact-encoded JSON Web Token (JWT) that is signed, "
        "containing the claims specified in RFC 7523."
    )
)


CLIENT_ASSERTION: CompactSerialized | None = fastapi.Form(
    default=None,
    description=(
        "A compact-encoded JSON Web Token (JWT) that is signed, "
        "containing the claims specified in RFC 7523 for the "
        "client assertion profile."
    )
)

CLIENT_ID: Any = fastapi.Form(
    default=None,
    title="Client ID",
    description=(
        "Required if the client is not authenticating with "
        "the authorization server"
    )
)

CLIENT_SECRET: str | None = fastapi.Form(
    default=None,
    title="Client secret",
    description=(
        "This parameter is **required** if the client is authenticating using "
        "the `client_secret_post` method, otherwise is **must** be "
        "omitted."
    )
)

CODE: CompactSerialized | Any = fastapi.Form(
    default=None,
    description=(
        "The authorization code received from the authorization "
        "server when using the `authorization_code` grant."
    )
)

GRANT_TYPE: GrantType = fastapi.Form(
    default=...,
    description="Specifies the grant to obtain."
)

REDIRECT_URI: RedirectURI | None = fastapi.Form(
    default=None,
    title="Redirect URI",
    description=(
        "Required if the `redirect_uri` parameter was included "
        "in the authorization request, and their values must "
        "be identical."
    )
)

REFRESH_TOKEN: Any = fastapi.Form(
    default=None,
    alias='refresh_token',
    title="Refresh token",
    description="The refresh token issued to the client."
)

RESOURCE: Any = fastapi.Form(
    default=None,
    alias='resource',
    title='Resource'
)

SCOPE: str | None = fastapi.Form(
    default_factory=ScopeType,
    title="Scope",
    description=(
        "The requested access token scope. The resource owner "
        "**must** allow the requested scope."
    )
)
