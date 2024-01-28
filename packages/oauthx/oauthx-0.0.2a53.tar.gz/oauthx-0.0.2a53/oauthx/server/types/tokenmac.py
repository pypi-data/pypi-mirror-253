# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import hashlib

from aiopki.utils import b64encode

from .ikeypart import IKeyPart

class TokenMAC:
    __module__: str = 'oauthx.server.types'

    @classmethod
    def concat(cls, parts: list[IKeyPart]) -> str:
        return str(cls(parts))

    def __init__(self, parts: list[IKeyPart] | None = None):
        self.hasher = hashlib.sha256()
        for part in (parts or []):
            self.add(part)

    def add(self, part: IKeyPart) -> None:
        part.update_key(self.hasher.update)

    def __str__(self) -> str:
        return bytes.decode(bytes(self))

    def __bytes__(self) -> bytes:
        return b64encode(self.hasher.digest())