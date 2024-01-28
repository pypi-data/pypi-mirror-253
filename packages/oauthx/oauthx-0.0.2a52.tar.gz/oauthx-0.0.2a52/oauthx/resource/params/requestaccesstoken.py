# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import ssl
from typing import cast
from typing import Annotated
from typing import Any
from typing import AsyncGenerator
from typing import Callable
from typing import Literal
from typing import TypeVar

import httpx
import fastapi
import fastapi.params
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from aiopki.ext import jose

from oauthx.lib import LazyServerMetadata
from oauthx.lib import RFC9068AccessToken
from oauthx.lib import ServerMetadata
from oauthx.lib.exceptions import InvalidRequest
from oauthx.lib.exceptions import InvalidToken
from oauthx.lib.types import AccessTokenHash


__all__: list[str] = ['RequestAccessToken']

T = TypeVar('T', bound=RFC9068AccessToken)

ISSUER_CACHE: dict[str, ServerMetadata | LazyServerMetadata] = {}


async def get_http_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient() as client:
        yield client


async def get_issuer_metadata(
    http: httpx.AsyncClient,
    issuer: str,
    timeout: int = 5
) -> ServerMetadata:
    ISSUER_CACHE.setdefault(issuer, LazyServerMetadata(iss=issuer))
    metadata: ServerMetadata | LazyServerMetadata = ISSUER_CACHE[issuer]
    if isinstance(metadata, LazyServerMetadata):
        try:
            metadata = await metadata.discover(http=http)
        except (asyncio.TimeoutError, asyncio.CancelledError, httpx.ReadTimeout):
            raise InvalidToken("The issuer did not respond in time.")
        except ssl.SSLCertVerificationError:
            raise InvalidToken(
                "Unable to establish a secure connection with the issuer "
                "of the access token."
            )
        except Exception:
            raise InvalidToken(
                "The issuer of the access token is not a "
                "discoverable authorization server."
            )
        ISSUER_CACHE[issuer] = metadata
    assert isinstance(metadata, ServerMetadata)
    return metadata


def RequestAccessToken(
    issuers: str | set[str] | None,
    factory:  Callable[[bytes], T] = RFC9068AccessToken.model_validate,
    max_age: int | None = None,
    issuer_timeout: int = 5,
    required: bool = True,
    audience: Literal['server', 'endpoint', 'any'] = 'server',
    types: set[str | None] = {'at+jwt', 'application/at+jwt'},
    http_factory: Any = get_http_client
) -> fastapi.params.Depends:
    issuers = issuers or set()
    if isinstance(issuers, str):
        issuers = {issuers}
    if not isinstance(http_factory, fastapi.params.Depends):
        http_factory = fastapi.Depends(http_factory)


    async def get(
        request: fastapi.Request,
        authorization: Annotated[
            HTTPAuthorizationCredentials | None,
            fastapi.Depends(HTTPBearer(auto_error=False))
        ],
        http: httpx.AsyncClient = cast(Any, http_factory)
    ) -> RFC9068AccessToken | None:
        trust = set(issuers)
        if 'self' in trust:
            trust.remove('self')
            trust.add(f'{request.url.scheme}://{request.url.netloc}')
        allow: set[str] = {
            f'{request.url.scheme}://{request.url.netloc}{request.url.path}',
        }
        if audience == 'server':
            allow = {f'{request.url.scheme}://{request.url.netloc}'}
        if authorization is None:
            if required:
                raise InvalidRequest("The Authorization header is required.")
            return None
        if str.lower(authorization.scheme) != 'bearer':
            raise InvalidRequest("The 'Bearer' scheme is required.")
        try:
            jws = jose.parse(authorization.credentials)
            at = jws.payload(factory=factory)
        except Exception:
            raise InvalidRequest("Malformed access token.")
        if jws.is_encrypted():
            raise InvalidRequest("Encrypted access tokens are not supported.")
        if jws.typ not in types:
            raise InvalidToken("Token 'typ' claim must be at+jwt or application/at+jwt.")
        if audience != 'any' and not at.validate_aud(allow):
            raise InvalidToken("This resource server is not the audience of the access token.")
        if not at.validate_exp():
            raise InvalidToken("The access token is expired.")
        if not any(map(at.validate_iss, trust)):
            raise InvalidToken(
                "The access token is issued by an untrusted authorization server. "
                f"Trusted authorization servers are: {', '.join(sorted(trust))}"
            )
        if not at.validate_nbf(required=False):
            raise InvalidToken("The access token is inactive.")
        if max_age is not None and not at.validate_iat(max_age=max_age, required=True):
            raise InvalidToken("The access token is too old.")
        assert at.iss is not None
        metadata = await get_issuer_metadata(
            http=http,
            issuer=at.iss,
            timeout=issuer_timeout
        )
        if not await jws.verify(metadata.jwks):
            raise InvalidToken("The signature of the access token did not validate.")
        setattr(request, 'access_token', at)
        setattr(request, 'credentials', authorization.credentials)
        setattr(request, 'at_hash', AccessTokenHash.parse_at(authorization.credentials))
        setattr(request, 'issuer', metadata)

    return fastapi.Depends(get)