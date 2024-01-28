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
from typing import ClassVar
from typing import MutableMapping

import pydantic
from canonical import UnixTimestamp

from .sessionkey import SessionKey


class Session(pydantic.BaseModel):
    Key: ClassVar[type[SessionKey]] = SessionKey
    auth_time: UnixTimestamp | None = None
    email: str | None = None
    id: str
    sub: str | None = None
    taints: set[str] = set()
    _is_dirty: bool = pydantic.PrivateAttr(default=False)

    @classmethod
    def new(cls):
        return cls.model_validate({'id': secrets.token_urlsafe(64)})

    def authenticate(self, sub: str, email: str | None) -> None:
        """Authenticates the session as the given subject."""
        self.set('auth_time', UnixTimestamp.now(datetime.timezone.utc))
        self.set('sub', sub)
        if email is not None:
            self.set('email', email)

    def claims(self) -> dict[str, Any]:
        return self.model_dump(include={'id', 'sub', 'email', 'auth_time'})

    def contribute_to_userinfo(self, userinfo: MutableMapping[str, Any]) -> None:
        if self.auth_time is not None:
            userinfo['auth_time'] = self.auth_time
        if self.email is not None:
            userinfo['email'] = self.email

    def is_dirty(self) -> bool:
        return self._is_dirty

    def logout(self) -> None:
        self.set('auth_time', None)
        self.set('email', None)
        self.set('sub', None)

    def set(self, key: str, value: Any) -> None:
        if key not in self.model_fields:
            raise AttributeError(key)
        if getattr(self, key) == value:
            return
        setattr(self, key, value)
        self._is_dirty = True

    def taint(self, name: str) -> None:
        self.taints.add(name)
        self._is_dirty = True
        