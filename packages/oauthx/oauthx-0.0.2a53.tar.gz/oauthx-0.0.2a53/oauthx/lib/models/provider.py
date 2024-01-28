# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from urllib.parse import urlencode
from typing import Any

import httpx
import pydantic
from aiopki.lib import JSONWebKeySet
from aiopki.ext.jose import JOSEObject
from starlette.datastructures import URL

from oauthx.lib import utils
from oauthx.lib.exceptions import Error
from oauthx.lib.exceptions import TrustIssues
from .grant import Grant
from .discoverableprovider import DiscoverableProvider
from .lazyservermetadata import LazyServerMetadata
from .obtainedgrant import ObtainedGrant
from .redirectionparameters import RedirectionParameters
from .servermetadata import ServerMetadata


class Provider(pydantic.RootModel[ServerMetadata | LazyServerMetadata | DiscoverableProvider]):
    root: ServerMetadata | LazyServerMetadata | DiscoverableProvider

    @property
    def authorization_endpoint(self) -> URL:
        assert isinstance(self.root, ServerMetadata)
        if not self.root.authorization_endpoint:
            raise NotImplementedError(
                "The authorization server does not provide the "
                "Authorization Endpoint."
            )
        return URL(self.root.authorization_endpoint)

    @property
    def issuer(self) -> str:
        assert isinstance(self.root, ServerMetadata)
        return self.root.issuer

    @property
    def token_endpoint(self) -> URL:
        assert isinstance(self.root, ServerMetadata)
        if not self.root.token_endpoint:
            raise NotImplementedError(
                "The authorization server does not provide the "
                "Token Endpoint."
            )
        return URL(self.root.token_endpoint)

    @property
    def signing_keys(self) -> JSONWebKeySet:
        keys = []
        if isinstance(self.root, ServerMetadata):
            keys = [x for x in self.root.jwks.keys if x.use in {'sig', None}]
        return JSONWebKeySet(keys=keys)

    def authorize(self, **params: Any) -> str:
        return str(httpx.URL(str(self.authorization_endpoint), params=params))

    async def discover(self, http: httpx.AsyncClient | None = None):
        if isinstance(self.root, LazyServerMetadata):
            self.root = await self.root.discover(http=http)
        assert isinstance(self.root, ServerMetadata)
        await self.root.discover(http=http)
        return self   

    @utils.http
    async def grant(self, http: httpx.AsyncClient, grant: Grant):
        response = await http.post(
            url=str(self.token_endpoint),
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            content=urlencode(grant.root.model_dump(by_alias=True, exclude_none=True), True)
        )
        if response.status_code >= 400:
            raise Error(**response.json())
        return ObtainedGrant.model_validate(response.json())

    async def verify(self, params: RedirectionParameters) -> None:
        assert isinstance(self.root, ServerMetadata)
        if self.root.authorization_response_iss_parameter_supported:
            if params.iss is None:
                raise TrustIssues(
                    "The server advertises to support the `iss` parameter "
                    "in authorization responses but did not provide it."
                )

            if params.iss != self.root.issuer:
                raise TrustIssues(
                    f"The `iss` response parameter {params.iss} does not match the "
                    f"expected issuer {self.root.issuer}"
                )

    async def verify_id_token(self, obj: JOSEObject):
        assert not obj.is_encrypted()
        assert isinstance(self.root, ServerMetadata)
        if not await obj.verify(self.root.jwks):
            raise TrustIssues(
                "The signature of the OpenID Connect ID Token did not "
                "validate against the public keys known for issuer "
                f"{self.root.issuer}"
            )

    async def userinfo(self, access_token: str, http: httpx.AsyncClient | None = None):
        assert isinstance(self.root, ServerMetadata)
        return await self.root.userinfo(access_token, http=http)

    def __await__(self):
        return self.discover().__await__()