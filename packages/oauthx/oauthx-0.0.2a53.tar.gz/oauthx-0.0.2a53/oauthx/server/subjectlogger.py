# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import logging
import uuid
from typing import Literal

import fastapi

from oauthx.lib.types import OIDCIssuerIdentifier
from .protocols import ISubjectLogger


class SubjectLogger(ISubjectLogger):
    __module__: str = 'oauthx.server'
    logger: logging.Logger
    request: fastapi.Request

    def __init__(self, request: fastapi.Request):
        self.logger = logging.getLogger('oauthx.events.subject')
        self.request = request
        setattr(request, 'subject_logger', self)

    def onboarded(
        self,
        sub: int,
        registrar: str,
        authorization_id: int | None = None,
        timestamp: datetime.datetime | None = None,
        client_id: str | None = None
    ) -> None:
        dto = {
            'apiVersion': 'v1',
            'kind': 'SubjectOnboarded',
            'metadata': {
                'id': str(uuid.uuid4()),
                'name': f'onboarded/{sub}',
                'host': self.get_host(),
                'timestamp': (timestamp or self.now()).isoformat(timespec='seconds'),
                'endpoint': self.request.scope['route'].name
            },
            'data': {
                'sub': sub,
                'authorizationId': authorization_id,
                'clientId': client_id,
                'registrar': registrar
            }
        }
        self.logger.info(dto)

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
    ):
        dto = {
            'apiVersion': 'v1',
            'kind': 'PersonalDataReceived',
            'metadata': {
                'id': str(uuid.uuid4()),
                'name': f'receipts/{receipt_id}',
                'host': self.get_host(),
                'timestamp': (timestamp or self.now()).isoformat(timespec='seconds'),
                'endpoint': self.request.scope['route'].name
            },
            'data': {
                'authorizationId': request_id,
                'clientId': client_id,
                'receiptId': receipt_id,
                'sub': sub,
                'obtained': obtained.isoformat(timespec='seconds'),
                'processed': list(processed),
                'provider': provider,
                'purpose': purpose,
                'received': list(received)
            }
        }
        self.logger.info(dto)

    def get_host(self) -> str:
        assert self.request.client is not None
        return self.request.client.host

    def now(self) -> datetime.datetime:
        return datetime.datetime.now(datetime.timezone.utc)