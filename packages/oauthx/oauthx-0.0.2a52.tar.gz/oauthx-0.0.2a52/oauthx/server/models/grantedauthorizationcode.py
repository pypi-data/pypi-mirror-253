# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from oauthx.server.protocols import IResourceOwner
from .authorizationcode import AuthorizationCode
from .subjectkey import SubjectKey


class GrantedAuthorizationCode(pydantic.BaseModel):
    client_id :str
    sub: SubjectKey
    consumed: bool = False
    redirect_uri: str | None
    scope: set[str]
    value: AuthorizationCode

    @property
    def owner(self) -> IResourceOwner.Key:
        return IResourceOwner.Key(self.client_id, str(self.sub))

    def allows_redirect(self, redirect_uri: str) -> bool:
        return any([
            self.redirect_uri is None,
            str(self.redirect_uri) == redirect_uri
        ])

    def consume(self) -> None:
        self.consumed = True

    def has_consent(self, owner: IResourceOwner) -> bool:
        return True

    def is_authorized(self, client_id: str) -> bool:
        return self.client_id == client_id

    def is_consumed(self) -> bool:
        return self.consumed