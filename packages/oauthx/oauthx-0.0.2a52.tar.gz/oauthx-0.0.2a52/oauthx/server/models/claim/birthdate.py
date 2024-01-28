# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import re
from typing import Annotated
from typing import Literal

from aiopki.types import EncryptionResult
from pydantic.functional_validators import AfterValidator

from .baseclaim import BaseClaim


__all__: list[str] = ['BirthdateClaim']


def validate_year(value: str) -> str:
    if not re.match('^[0-9]{4}$', value):
        raise ValueError("Invalid birthdate format.")
    return value


Birthyear = Annotated[str, AfterValidator(validate_year)]
BirthdateType = datetime.datetime | datetime.date | Birthyear | Literal['0000']


class BirthdateClaim(BaseClaim):
    kind: Literal['birthdate'] = 'birthdate'
    value: BirthdateType | EncryptionResult

    def get_encryption_input(self) -> bytes:
        return self.get_masking_input()

    @BaseClaim.requires_decryption
    def get_masking_input(self) -> bytes:
        assert not isinstance(self.value, EncryptionResult)
        if isinstance(self.value, (datetime.datetime, datetime.date)):
            v = self.value.isoformat()
        else:
            v = str(self.value)
        return str.encode(v, 'ascii')