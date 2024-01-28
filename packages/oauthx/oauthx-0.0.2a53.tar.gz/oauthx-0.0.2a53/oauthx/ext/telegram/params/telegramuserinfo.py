# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import dataclasses
import datetime
import hmac
from typing import Annotated
from typing import TypeAlias

import fastapi
from aiopki.types import SubjectID
from canonical import UnixTimestamp

from oauthx.lib.types import MaskedPrincipal
from oauthx.lib.types import OIDCIssuerIdentifier
from oauthx.server.params import Masker
from oauthx.server.types import StopSnooping
from ..const import ISSUER
from .telegramtoken import TelegramToken


__all__: list[str] = ['TelegramUserInfo']


MAX_AGE: int = 2


@dataclasses.dataclass
class UserInfo:
    id: SubjectID
    issuer: OIDCIssuerIdentifier
    username: str
    masked: MaskedPrincipal


async def get(
    request: fastapi.Request,
    masker: Masker,
    token: TelegramToken,
    auth_date: UnixTimestamp,
    user_id: int = fastapi.Query(alias='id'),
    username: str = fastapi.Query(),
    mac: str = fastapi.Query(alias='hash'),
) -> UserInfo:
    now = datetime.datetime.now(datetime.timezone.utc)
    age = abs(int((now - auth_date).total_seconds()))
    check_sequence = bytes.join(b'\n', [
        str.encode(f'{k}={v}') for k, v
        in sorted(request.query_params.items(), key=lambda x: x[0])
        if k != 'hash'
    ])
    is_valid = hmac.compare_digest(
        hmac.new(token, check_sequence, 'sha256').hexdigest(),
        mac
    )
    if not is_valid:
        raise StopSnooping
    if age > MAX_AGE:
        raise StopSnooping

    subject_id = SubjectID(iss=ISSUER, sub=str(user_id))

    return UserInfo(
        id=subject_id,
        issuer=OIDCIssuerIdentifier(ISSUER),
        masked=await masker.mask(subject_id),
        username=username
    )


TelegramUserInfo: TypeAlias = Annotated[UserInfo, fastapi.Depends(get)]