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
from aiopki.ext.jose import CompactSerialized
from aiopki.ext.jose import JWT

from oauthx.lib.exceptions import InvalidGrant
from oauthx.lib.types import GrantType
from oauthx.server import models
from .query import CLIENT_ASSERTION
from .query import GRANT_TYPE


__all__: list[str] = [
    'ClientAssertion'
]


MAX_AGE: int = 600


async def get(
    request: fastapi.Request,
    grant_type: GrantType = GRANT_TYPE,
    client_assertion_type: str | None = fastapi.Form(
        default=None
    ),
    client_assertion: CompactSerialized | None = CLIENT_ASSERTION,
) -> models.Assertion | None:
    if client_assertion is None:
        return
    if client_assertion_type != 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer':
        raise NotImplementedError
    aud = str(request.url_for('oauth2.token'))
    jwt = client_assertion.payload(JWT.model_validate)
    if not jwt.validate_aud(aud):
        raise InvalidGrant(
            "The audience specified by the assertion is invalid. "
            "An assertion must point to the authorization servers' "
            f"token endpoint ({aud})."
        )

    if not all([jwt.validate_exp(), jwt.validate_nbf()]):
        raise InvalidGrant(
            "The provided assertion can not be used at the current "
            "date and time."
        )

    if not jwt.validate_iat(MAX_AGE):
        raise InvalidGrant("The provided assertion is too old.")

    return models.Assertion.model_validate({
        **jwt.model_dump(mode='json'),
        'grant_type': grant_type,
        'jws': client_assertion
    })


ClientAssertion: TypeAlias = Annotated[
    models.Assertion | None,
    fastapi.Depends(get)
]