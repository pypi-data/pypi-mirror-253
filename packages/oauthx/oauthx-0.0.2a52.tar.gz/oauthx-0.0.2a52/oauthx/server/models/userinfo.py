# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any, Iterator
from typing import MutableMapping

from oauthx.lib.protocols import IStorage
from oauthx.server.protocols import ISubject
from .claim import Claim


class UserInfo(MutableMapping[str, Any]):
    _known: set[tuple[str, str]]
    claims: dict[str, Any]

    @classmethod
    async def restore(cls, subject: ISubject, storage: IStorage):
        q = storage.find(
            kind=Claim,
            filters=[('sub', '=', int(subject.get_primary_key()))], # type: ignore
            sort=['obtained']
        )
        self = cls()
        async for claim in q:
            await claim.decrypt(subject)
            claim.contribute_to_userinfo(self)
        return self

    def __init__(self):
        self.claims = {}

    def dump(self, claims: set[str]) -> dict[str, Any]:
        return {
            k: self.claims[k] for k in claims
            if self.claims.get(k) not in {None, ''}
        }

    def has(self, claim: str) -> bool:
        return claim in self.claims

    def __delitem__(self, __key: str) -> None:
        return self.claims.__delitem__(__key)

    def __getitem__(self, __key: str) -> Any:
        return self.claims.__getitem__(__key)

    def __iter__(self) -> Iterator[str]:
        return self.claims.__iter__()

    def __len__(self) -> int:
        return self.claims.__len__()

    def __setitem__(self, __key: str, __value: Any) -> None:
        self.claims[__key] = __value