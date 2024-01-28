# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Literal
from typing import Protocol

from oauthx.lib.types import OIDCIssuerIdentifier


class ISubjectLogger(Protocol):
    __module__: str = 'oauthx.server.types'

    def onboarded(
        self,
        sub: int,
        registrar: str,
        authorization_id: int | None = None,
        timestamp: datetime.datetime | None = None,
        client_id: str | None = None,
    ) -> None:
        ...

    def receipt(
        self,
        receipt_id: int,
        sub: int,
        obtained: datetime.datetime,
        processed: set[str],
        provider: OIDCIssuerIdentifier,
        purpose: Literal['IDENTIFY', 'INVITE', 'LOGIN', 'VERIFY_ACCOUNT'],
        received: set[str],
        client_id: str | None = None,
        request_id: int | None = None,
        timestamp: datetime.datetime | None = None
    ) -> None:
        ...