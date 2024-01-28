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
from typing import Any
from typing import Callable
from typing import Iterable
from typing import Literal
from typing import MutableMapping
from typing import TypeAlias

import pydantic

from oauthx.lib.protocols import IStorage
from oauthx.lib.types import TargetResource
from oauthx.server.protocols import IUserInfoContributor
from oauthx.server.types import AuthorizationKey
from .basemodel import BaseModel
from .refreshtokenpolicy import RefreshTokenPolicy
from .subjectkey import SubjectKey


AuthorizedTokenType: TypeAlias = Literal[
    'urn:ietf:params:oauth:token-type:access_token',
    'urn:ietf:params:oauth:token-type:refresh_token',
    'urn:ietf:params:oauth:token-type:id_token',
]


class Authorization(BaseModel):
    """A :class:`Authorization` object represents the authorization granted
    by the resource owner through the authorization endpoint.
    """
    authorized: datetime.datetime = pydantic.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    code: str | None = pydantic.Field(
        default=None
    )

    client_id: str = pydantic.Field(
        default=...
    )

    id: int = pydantic.Field(
        default=...
    )
    
    issuer: str = pydantic.Field(
        default=...
    )

    lifecycle: Literal['GRANTED', 'ISSUED'] = pydantic.Field(
        default='ISSUED'
    )

    prompted: bool = pydantic.Field(
        default=False
    )

    refresh_token: RefreshTokenPolicy | None = pydantic.Field(
        default=None
    )
    
    resources: set[TargetResource] = pydantic.Field(
        default_factory=set
    )

    scope: set[str] = pydantic.Field(
        default_factory=set
    )

    sub: SubjectKey = pydantic.Field(
        default=...
    )
    
    token_types: set[AuthorizedTokenType] = pydantic.Field(
        default=...
    )
    
    userinfo: dict[str, Any] = pydantic.Field(
        default={}
    )

    @property
    def pk(self) -> AuthorizationKey:
        return AuthorizationKey(self.id)

    def model_post_init(self, _: Any) -> None:
        if 'offline_access' in self.scope:
            self.token_types.add('urn:ietf:params:oauth:token-type:refresh_token')

    def allows_scope(self, scope: Iterable[str]) -> bool:
        return set(scope) <= self.scope

    def allows_target(self, target: TargetResource | Iterable[TargetResource]) -> bool:
        if isinstance(target, TargetResource):
            target = {target}
        return set(target) <= self.resources

    def is_consumed(self) -> bool:
        return self.lifecycle == 'ISSUED'

    def contribute(self, contributor: IUserInfoContributor) -> None:
        contributor.contribute_to_userinfo(self.userinfo)

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        userinfo.update(self.userinfo)

    def grants_id_token(self) -> bool:
        return 'urn:ietf:params:oauth:token-type:id_token' in self.token_types

    def grants_refresh_token(self) -> bool:
        return 'urn:ietf:params:oauth:token-type:refresh_token' in self.token_types

    def update_key(self, update: Callable[[bytes], None]) -> None:
        return

    async def consume(self, storage: IStorage) -> None:
        self.lifecycle = 'ISSUED'
        await storage.persist(self)

    async def issue_authorization_code(self) -> str:
        if self.code is not None:
            raise TypeError(
                "Authorization code is already issued for this grant."
            )
        self.code = secrets.token_urlsafe(32)
        return self.code

    async def issue_refresh_token(self) -> str:
        if not self.grants_refresh_token():
            raise TypeError(
                "Can not issue a refresh token if the `offline_access` scope is "
                "not granted by the resource owner."
            )
        if not self.refresh_token:
            self.refresh_token = RefreshTokenPolicy(
                use='once'
            )
        else:
            self.refresh_token.rotate()
        await self.persist()
        return self.refresh_token.current