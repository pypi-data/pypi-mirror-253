# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Annotated
from typing import Any
from typing import AsyncGenerator
from typing import TypeAlias

import fastapi
from aiopki.ext.jose import CompactSerialized

from oauthx.lib.exceptions import InvalidGrant
from oauthx.lib.exceptions import UnknownClient
from oauthx.lib.params import Logger
from oauthx.lib.types import GrantType
from oauthx.lib.types import RedirectURI
from oauthx.server.models import Authorization as AuthorizationState
from oauthx.server.models import AuthorizationCode
from oauthx.server.params import Storage
from oauthx.server.params import TokenSigner
from .client import Client
from .refreshtoken import RefreshToken
from .resourceowner import ResourceOwner
from .query import CODE
from .query import GRANT_TYPE
from .query import REDIRECT_URI


__all__: list[str] = [
    'Authorization'
]


async def get(
    signer: TokenSigner,
    storage: Storage,
    logger: Logger,
    client: Client,
    owner: ResourceOwner,
    refresh_token: RefreshToken,
    grant_type: GrantType = GRANT_TYPE,
    code: CompactSerialized = CODE,
    redirect_uri: RedirectURI | None = REDIRECT_URI
) -> AsyncGenerator[Any, AuthorizationState | None]:
    if grant_type not in  {'authorization_code', 'refresh_token'}:
        yield None
        return
    if client is None:
        raise UnknownClient(
            "No client could be identified from the Authorization "
            "header, the request parameters, or client assertion."
        )
    if owner is None:
        raise InvalidGrant(
            "The resource owner identified by the grant parameters "
            "does not exist."
        )
    match grant_type:
        case 'authorization_code':
            if not await code.verify(signer):
                raise InvalidGrant("The provided authorization code is not valid.")
            granted = code.payload(AuthorizationCode.model_validate_json)
            if not granted.is_authorized(str(client.id)): # type: ignore
                raise InvalidGrant("The client is not authorized to obtain this grant.")
            if granted.is_revoked(client, owner):
                raise InvalidGrant("This authorization code is revoked.")
            if not granted.allows_redirect(redirect_uri):
                raise InvalidGrant(
                    "The redirect_uri parameter must match the redirect_uri that "
                    "was included in the authorization request."
                )
            authorization = await storage.get(granted.authorization)
            if authorization is None or authorization.is_consumed():
                if authorization is not None:
                    logger.critical(
                        "Authorization code reused (authorization: %s)",
                        str(authorization.pk)
                    )
                logger.debug("No authorization exists")
                raise InvalidGrant(
                    "The authorization code supplied in the request body can not "
                    "be used."
                )
            yield authorization
            await authorization.consume(storage)
        case 'refresh_token':
            assert refresh_token is not None
            authorization = await storage.get(refresh_token.authorization)
            yield authorization
        case _:
            raise NotImplementedError


Authorization: TypeAlias = Annotated[
    AuthorizationState | None,
    fastapi.Depends(get)
]