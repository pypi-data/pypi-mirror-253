# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

from aiopki.types import SubjectID
from aiopki.types import EncryptionResult

from .baseprincipal import BasePrincipal


class SubjectIdentifierPrincipal(BasePrincipal):
    kind: Literal['subject'] = 'subject'
    value: EncryptionResult | SubjectID
    
    def to_bytes(self) -> bytes:
        assert not isinstance(self.value, EncryptionResult)
        return str.encode(self.value.model_dump_json())