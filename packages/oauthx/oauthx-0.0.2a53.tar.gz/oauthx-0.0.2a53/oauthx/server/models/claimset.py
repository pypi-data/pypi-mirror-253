# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import itertools
from typing import AsyncIterable
from typing import Iterable

from oauthx.lib.types import OIDCIssuerIdentifier
from .claim import Claim


class ClaimSet:
    _known: set[tuple[str, str]]

    @classmethod
    async def fromquery(cls, provider: OIDCIssuerIdentifier, query: AsyncIterable[Claim]):
        return  cls(provider, [claim async for claim in query])

    def __init__(self, provider: OIDCIssuerIdentifier, claims: Iterable[Claim]):
        self.userinfo = {}
        self.provider = provider
        self.claims = list(claims)
        self._known = {(str(x.root.kind), str(x.root.issuer)) for x in claims}

    def is_known(self, claim: Claim) -> bool:
        return (str(claim.root.kind), str(claim.root.issuer)) in self._known

    def diff(self, claims: Iterable[Claim]) -> list[Claim]:
        """Return the :class:`Claim` objects from iterable `claims`
        that have changed with respect to the claims contained in the
        :class:`ClaimSet`.
        """
        claims = [x for x in claims if x.root.provider == self.provider]
        changed: list[Claim] = [x for x in claims if not self.is_known(x)]
        for old, new in itertools.product(self.claims, claims):
            if new in changed:
                continue
            if old.root.kind != new.root.kind:
                continue
            if (old.root.issuer, old.root.masked) == (new.root.issuer, new.root.masked):
                continue
            changed.append(new)
        return changed

    def __bool__(self) -> bool:
        return bool(self.claims)