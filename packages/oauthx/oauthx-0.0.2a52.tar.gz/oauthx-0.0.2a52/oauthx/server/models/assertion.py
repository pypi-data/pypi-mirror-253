# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic
from aiopki.ext.jose import AudienceType
from aiopki.ext.jose import CompactSerialized

from oauthx.lib.types import GrantType
from oauthx.server.protocols import IResourceOwner
from .clientkey import ClientKey


class Assertion(pydantic.BaseModel):
    grant_type: GrantType
    jws: CompactSerialized
    aud: AudienceType
    iss: str
    sub: str

    @property
    def client_id(self) -> ClientKey:
        return ClientKey(self.iss)

    @property
    def owner(self) -> IResourceOwner.Key:
        return IResourceOwner.Key(self.iss, self.sub)

    def is_client(self) -> bool:
        """Return a boolean if the assertion was created by a
        client. This is detected based on the `iss` claim, as
        a client identifier should not be a URL.
        """
        return self.iss != self.sub

    def is_self_issued(self) -> bool:
        """Return a boolean indicating if the assertion is
        self-issued.
        """
        return self.iss == self.sub