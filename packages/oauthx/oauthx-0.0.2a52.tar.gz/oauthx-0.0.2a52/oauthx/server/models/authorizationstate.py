# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import secrets
from typing import ClassVar
from typing import Literal

import pydantic
from canonical import ResourceIdentifier

from oauthx.lib.exceptions import InvalidRequest
from oauthx.lib.models import AuthorizationRequestParameters
from oauthx.lib.models import AuthorizationResponse
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import ResponseType
from oauthx.server.protocols import IRequestSubject
from oauthx.server.protocols import IResourceOwner
from .client import Client
from .resourceowner import ResourceOwner


DEFAULT_RESPONSE_MODES: dict[ResponseType, str] = {
    'code': 'query'
}


class AuthorizationState(pydantic.BaseModel):
    default_response_modes: ClassVar[dict[ResponseType, str]] = {
        'code'  : 'query',
        'token' : 'fragment',
    }

    class KeyType(ResourceIdentifier[str, 'AuthorizationState']):
        client_id: str
        openapi_example: str = 'FOpou5oouxBHGGXBYI23R7vfEc3HcRjd4-_5EYYzsuQ'
        openapi_title: str = 'Request ID'

        def __init__(self, request_id: str):
            self.request_id = request_id

        def __str__(self) -> str:
            return self.request_id
        
        def __eq__(self, key: object) -> bool:
            return isinstance(key, type(self)) and key.request_id == self.request_id

    @property
    def client_id(self) -> Client.Key:
        return Client.Key(self.params.client_id)

    @property
    def owner(self) -> ResourceOwner.Key:
        assert self.client_id
        assert self.sub
        return ResourceOwner.Key(self.params.client_id, self.sub)

    @property
    def response_mode(self) -> str:
        return self.default_response_modes[self.response_type]

    @property
    def response_type(self) -> ResponseType:
        return self.params.response_type

    code: str | None = pydantic.Field(
        default=None
    )

    consumed: bool = pydantic.Field(
        default=False
    )

    created: datetime.datetime = pydantic.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    id: str = pydantic.Field(
        default=...
    )

    params: AuthorizationRequestParameters = pydantic.Field(
        default=...
    )

    redirect_uri: RedirectURI | None = pydantic.Field(
        default=None
    )

    signed: bool = pydantic.Field(
        default=False
    )

    source: Literal['ENDPOINT', 'REMOTE', 'PUSHED'] = pydantic.Field(
        default=...
    )

    sub: str | None = pydantic.Field(
        default=None
    )

    async def get_redirect_uri(self) -> str:
        assert self.redirect_uri is not None
        params = AuthorizationResponse.model_validate({
            'code': self.code,
            'state': self.params.state
        })
        return self.redirect_uri.redirect(
            mode=self.response_mode,
            **params.root.model_dump(exclude_defaults=True, exclude_none=True)
        )

    def allows_redirect(self, redirect_uri: RedirectURI | None) -> bool:
        # If the redirect_uri was included in the authorization
        # request, these values must match.
        return self.params.redirect_uri == redirect_uri

    def authorize(self):
        """Authorizes the authorization request."""
        self.code = secrets.token_urlsafe(32)

    def authenticate(self, subject: IRequestSubject):
        """Authenticate the request. Raise an exception if the request is not
        valid.
        """
        if self.sub is None:
            self.sub = subject.id
        if self.sub != subject.id:
            raise InvalidRequest(
                "This authorization request can not be fulfilled."
            )
        
    def consume(self) -> None:
        self.consumed = True

    def has_consent(self, owner: IResourceOwner) -> bool:
        return True

    def is_authorized(self) -> bool:
        return self.code is not None

    def is_consumed(self) -> bool:
        return self.consumed

    def is_openid(self) -> bool:
        return 'openid' in self.params.scope
