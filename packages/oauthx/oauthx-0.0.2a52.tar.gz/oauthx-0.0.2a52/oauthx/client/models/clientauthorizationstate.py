# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Any
from typing import Callable
from typing import TypeVar

import pydantic

from oauthx.lib.exceptions import TrustIssues
from .authorizationrequestparameters import AuthorizationRequestParameters
from .redirectionparameters import RedirectionParameters


T = TypeVar('T')


class ClientAuthorizationState(pydantic.BaseModel):
    """Maintains state for an OAuth 2.x/OpenID Connect client in the
    context of an authorization request.
    """

    authorize_url: str = pydantic.Field(
        default=...
    )

    client_id: str = pydantic.Field(
        default=...
    )

    created: datetime.datetime = pydantic.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    params: AuthorizationRequestParameters = pydantic.Field(
        default=...
    )

    annotations: dict[str, str] = pydantic.Field(
        default_factory=dict
    )

    @property
    def pk(self) -> str:
        if self.params.state is None:
            raise NotImplementedError(
                "The authorization request did not include the `state` "
                "parameter."
            )
        return self.params.state

    @property
    def redirect_uri(self) -> str | None:
        return self.params.redirect_uri

    def annotate(self, name: str, value: str) -> None:
        self.annotations[name] = value

    def annotation(
        self,
        name: str,
        decoder: Callable[[Any], T] = lambda x: x
    ) -> T | None:
        value = self.annotations.get(name)
        if value is None:
            return None

        return decoder(value)

    def get_authorize_url(self) -> str:
        return self.authorize_url

    def redirect(self, request_factory: Callable[..., T]) -> T:
        return request_factory(url=self.authorize_url)

    async def verify(self, params: RedirectionParameters):
        if str(params.state) != str(self.params.state):
            raise TrustIssues(
                "The state returned by the authorization server "
                "does not match the expected state."
            )