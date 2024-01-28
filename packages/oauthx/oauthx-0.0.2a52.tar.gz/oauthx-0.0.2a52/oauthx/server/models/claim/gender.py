# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

from aiopki.types import EncryptionResult

from .baseclaim import BaseClaim


class GenderClaim(BaseClaim):
    kind: Literal['gender'] = 'gender'
    value: Literal['male', 'female', 'other', 'withheld'] | EncryptionResult

    def get_encryption_input(self) -> bytes:
        assert isinstance(self.value, str)
        return str.encode(self.value, 'ascii')

    @BaseClaim.requires_decryption
    def get_masking_input(self) -> bytes:
        assert isinstance(self.value, str)
        return str.encode(self.value.lower(), 'ascii')