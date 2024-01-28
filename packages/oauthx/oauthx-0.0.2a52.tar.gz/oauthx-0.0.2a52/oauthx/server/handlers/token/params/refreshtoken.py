# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Annotated
from typing import TypeAlias

import fastapi
import pydantic
from aiopki.ext.jose import CompactSerialized

from oauthx.lib.exceptions import InvalidGrant
from oauthx.lib.exceptions import InvalidRequest
from oauthx.server.params import Issuer
from oauthx.server.params import TokenSigner
from oauthx.server.models import RefreshToken as RefreshTokenModel
from .client import Client
from .granttype import GrantType
from .query import REFRESH_TOKEN


__all__: list[str] = [
    'RefreshToken'
]


MAX_AGE: int = 180 * 86400


async def get(
    issuer: Issuer,
    signer: TokenSigner,
    request: fastapi.Request,
    client: Client,
    grant_type: GrantType,
    jws: CompactSerialized | None = REFRESH_TOKEN
) -> RefreshTokenModel | None:
    if grant_type != 'refresh_token' or client is None:
        return None
    if jws is None:
        raise InvalidRequest("The refresh_token parameter is required.")
    try:
        rt = jws.payload(RefreshTokenModel.model_validate)
    except pydantic.ValidationError:
        raise InvalidGrant("The refresh token is malformed.")
    if not rt.validate_exp() or not rt.validate_nbf() or not rt.validate_iat(MAX_AGE):
        raise InvalidGrant("The refresh token is inactive or expired.")
    if not client.id == rt.client_id:
        raise InvalidGrant("The refresh token was issued to a different client.")
    if jws.typ != 'jwt+refresh-token':
        raise InvalidGrant("Invalid refresh token.")
    if not rt.validate_iss(issuer):
        raise InvalidGrant("The refresh token was issued by an untrusted issuer.")
    if not await jws.verify(signer):
        raise InvalidGrant("The signature of the refresh token did not validate.")
    if not rt.validate_aud(f'{request.url.scheme}://{request.url.netloc}{request.url.path}'):
        raise InvalidGrant(f"Invalid audience: {rt.aud}")
    return rt


RefreshToken: TypeAlias = Annotated[
    RefreshTokenModel | None,
    fastapi.Depends(get)
]