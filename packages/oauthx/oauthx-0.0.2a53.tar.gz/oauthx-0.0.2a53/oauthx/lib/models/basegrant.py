# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pydantic
from aiopki.ext.jose import JOSEObject

from oauthx.lib.exceptions import InvalidRequest
from oauthx.lib.exceptions import UnknownClient
from oauthx.lib.protocols import IClient
from oauthx.lib.types import ClientAssertionType
from oauthx.lib.types import TargetResource


class BaseGrant(pydantic.BaseModel):
    model_config = {'populate_by_name': True}

    client_id: str | None = pydantic.Field(
        default=None,
        title="Client ID",
        description=(
            "This parameter is **required** if the client is not authenticating with "
            "the authorization server and the grant requires client identifiation, "
            "otherwise it **must** be omitted.\n\n"
            "If the client authenticates using an implementation of the RFC 7521 "
            "assertion framework, then the `client_id` parameter is unnecessary "
            "for client assertion authentication because the client is identified "
            "by the subject of the assertion.  If present, the value of the "
            "`client_id` parameter **must** identify the same client as is "
            "identified by the client assertion."
        )
    )

    client_secret: str | None = pydantic.Field(
        default=None,
        title="Client secret",
        description=(
            "This parameter is **required** if the client is authenticating using "
            "the `client_secret_post` method, otherwise is **must** be "
            "omitted."
        )
    )

    # RFC 7521 Assertion Framework for OAuth 2.0 Client
    # Authentication and Authorization Grants
    client_assertion_type: ClientAssertionType | None = pydantic.Field(
        default=None,
        title="Client assertion type",
        description=(
            "The format of the assertion as defined by the authorization server. "
            "The value is an absolute URI."
        )
    )

    client_assertion: JOSEObject | None = pydantic.Field(
        default=None,
        title='Client assertion',
        description=(
            "The assertion being used to authenticate the client. "
            "Specific serialization of the assertion is defined by "
            "profile documents for `client_assertion_type`."
        )
    )

    # RFC 8707 Resource Indicators for OAuth 2.0
    resources: set[TargetResource] | None = pydantic.Field(
        default=None,
        alias='resource',
        description=(
            "Specifies the intended resource to use the issued access token and "
            "(optionally) ID token with."
        )
    )

    def model_post_init(self, _: Any):
        if self.client_secret and (self.client_assertion or self.client_assertion_type):
            raise InvalidRequest(
                "The request must not utilize more than one "
                "mechanism for authenticating the client"
            )
        if (self.client_assertion_type or self.client_assertion)\
        and not all([self.client_assertion_type, self.client_assertion]):
            raise UnknownClient(
                "Provide both the `client_assertion_type` and "
                "`client_assertion` parameters."
            )
        if self.client_secret and not self.client_id:
            raise UnknownClient(
                "The `client_secret` parameter is required."
            )

    def has_credentials(self) -> bool:
        return any([
            self.client_secret is not None,
            self.client_assertion_type is not None
        ])

    def must_authenticate(self) -> bool:
        """Return a boolean if the client must always authenticate when
        using this grant.
        """
        return True

    def must_identify(self) -> bool:
        """Return a boolean if the client must identify when
        using this grant.
        """
        return True

    def requires_offline_access(self) -> bool:
        """Return a boolean indicating if the grant requires the
        ``offline_access`` scope.
        """
        return False

    def verify(self, client: IClient):
        """Verifies that the grant is valid for the given client."""
        pass