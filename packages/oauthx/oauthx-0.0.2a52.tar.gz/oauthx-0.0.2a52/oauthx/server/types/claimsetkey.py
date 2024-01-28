# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from canonical import ResourceIdentifier

from oauthx.lib.types import OIDCIssuerIdentifier
from .iclaimset import IClaimSet


class ClaimSetKey(ResourceIdentifier[int, IClaimSet]):
    __module__: str = 'oauthx.server.types'
    
    def __init__(self, iss: OIDCIssuerIdentifier, sub: int):
        self.iss = iss
        self.sub = sub

    def __hash__(self) -> int:
        return hash((self.iss, self.sub))

    def __repr__(self) -> str:
        return f'<ClaimSetKey: {self.iss}/sub/{self.sub}>'