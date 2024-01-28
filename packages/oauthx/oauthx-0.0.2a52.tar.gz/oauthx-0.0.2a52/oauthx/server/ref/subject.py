# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import dataclasses

from oauthx.server.models import SubjectKey
from oauthx.server.protocols import IRequestSubject
from oauthx.server.params import RequestSession


@dataclasses.dataclass
class RequestSubject:
    sub: str
    
    @property
    def pk(self) -> SubjectKey:
        return SubjectKey(self.sub)

    @classmethod
    async def resolve(cls, session: RequestSession) -> IRequestSubject | None:
        if session.sub is None:
            return None
        return cls(sub=session.sub)

    def is_authenticated(self) -> bool:
        return True