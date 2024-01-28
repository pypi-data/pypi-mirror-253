# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .masked import Masked


__all__: list[str] = [
    'Unmasked'
]


class Unmasked(Masked):
    __module__: str = 'oauthx.types'

    def __init__(self, masked: str = ''):
        super().__init__(masked)

    def __repr__(self) -> str:
        return f'<Unmasked>'

    def __str__(self) -> str:
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError

    def __eq__(self, key: object) -> bool:
        raise NotImplementedError