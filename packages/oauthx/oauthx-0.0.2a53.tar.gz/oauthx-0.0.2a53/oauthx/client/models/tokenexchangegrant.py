# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

import pydantic

from oauthx.lib.types import TokenType
from .basegrant import BaseGrant


class TokenExchangeGrant(BaseGrant):
    grant_type: Literal['urn:ietf:params:oauth:grant-type:token-exchange'] = pydantic.Field(
        default=...,
        description=(
            "The value `urn:ietf:params:oauth:grant-type:token-exchange` "
            "indicates that a token exchange is being performed."
        )
    )

    resource: str | None = pydantic.Field(
        default=None,
        description=(
            "A URI that indicates the target service or resource where "
            "the client intends to use the requested security token. "
            "This enables the authorization server to apply policy as "
            "appropriate for the target, such as determining the type "
            "and content of the token to be issued or if and how the "
            "token is to be encrypted. In many cases, a client will "
            "not have knowledge of the logical organization of the "
            "systems with which it interacts and will only know a URI "
            "of the service where it intends to use the token. The "
            "resource parameter allows the client to indicate to the "
            "authorization server where it intends to use the issued "
            "token by providing the location, typically as an https "
            "URL, in the token exchange request in the same form that "
            "will be used to access that resource. The authorization "
            "server will typically have the capability to map from a "
            "resource URI value to an appropriate policy. The value "
            "of the resource parameter MUST be an absolute URI that "
            "**may** include a query component and **must not** "
            "include a fragment component. Multiple resource "
            "parameters may be used to indicate that the issued "
            "token is intended to be used at the multiple resources "
            "listed."
        )
    )

    audience: str | None = pydantic.Field(
        default=None,
        description=(
            "The logical name of the target service where the client "
            "intends to use the requested security token. This serves "
            "a purpose similar to the resource parameter but with the "
            "client providing a logical name for the target service. "
            "Interpretation of the name requires that the value be "
            "something that both the client and the authorization "
            "server understand. An OAuth client identifier, a SAML "
            "entity identifier, and an OpenID Connect Issuer Identifier "
            "are examples of things that might be used as audience "
            "parameter values. However, audience values used with a "
            "given authorization server must be unique within that "
            "server to ensure that they are properly interpreted as "
            "the intended type of value. Multiple audience parameters "
            "may be used to indicate that the issued token is intended "
            "to be used at the multiple audiences listed. The audience "
            "and resource parameters may be used together to indicate "
            "multiple target services with a mix of logical names and "
            "resource URIs."
        )
    )

    scope: str | None = pydantic.Field(
        default=None,
        description=(
            "A list of space-delimited, case-sensitive strings, that "
            "allow the client to specify the desired scope of the "
            "requested security token in the context of the service "
            "or resource where the token will be used. The values and "
            "associated semantics of scope are service specific and "
            "expected to be described in the relevant service documentation."
        )
    )

    requested_token_type: TokenType | None = pydantic.Field(
        default=None,
        title="Requested token type",
        description=(
            "An identifier for the type of the requested security "
            "token. If the requested type is unspecified, the issued "
            "token type is at the discretion of the authorization "
            "server and may be dictated by knowledge of the requirements "
            "of the service or resource indicated by the resource or "
            "audience parameter."
        )
    )

    subject_token: str = pydantic.Field(
        default=...,
        title="Subject token",
        description=(
            "A security token that represents the identity of the "
            "party on behalf of whom the request is being made. "
            "Typically, the subject of this token will be the "
            "subject of the security token issued in response to "
            "the request."
        )
    )