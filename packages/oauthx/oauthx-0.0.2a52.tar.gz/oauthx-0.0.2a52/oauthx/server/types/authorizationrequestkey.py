# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from aiopki.utils import b64decode_int
from canonical import ResourceIdentifier

from oauthx.lib.types import RequestURI

from .iauthorizationrequest import IAuthorizationRequest


class AuthorizationRequestKey(ResourceIdentifier[int, IAuthorizationRequest]):
    __module__: str = 'oauthx.server.types'

    @classmethod
    def fromuri(cls, request_uri: RequestURI):
        assert request_uri.id is not None
        return cls(b64decode_int(request_uri.id))

    def __init__(self, pk: int):
        self.__pk = pk

    def cast(self) -> int:
        return self.__pk

    def __int__(self) -> int:
        return int(self.__pk)

    def __str__(self) -> str:
        return str(self.__pk)

    def __hash__(self) -> int:
        return hash(self.__pk)

    def __repr__(self) -> str:
        return f'<AuthorizationRequestKey: {str(self)}>'