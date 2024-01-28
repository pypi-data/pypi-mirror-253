# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
from typing import Any

import fastapi

from oauthx.lib.exceptions import InvalidScope
from oauthx.lib.exceptions import InvalidTarget
from oauthx.lib.exceptions import InvalidRequest
from oauthx.lib.models import AuthorizationCodeGrant
from oauthx.lib.models import ClientCredentialsGrant
from oauthx.lib.models import JWTBearerGrant
from oauthx.lib.models import Grant
from oauthx.lib.models import ObtainedGrant
from oauthx.lib.models import RefreshTokenGrant
from oauthx.server.params import ContentEncryptionKey
from oauthx.server.params import TokenIssuer
from oauthx.server.request import Request
from oauthx.server.types import InvalidClient
from oauthx.server.types import UnauthorizedClient
from ..baserequesthandler import BaseRequestHandler
from .params import Assertion
from .params import Client
from .params import Grant
from .params import Authorization
from .params import ResourceOwner


class TokenEndpointHandler(BaseRequestHandler):
    __module__: str = 'oauthx.server.handlers'

    def invalid_scope(self) -> InvalidScope:
        return InvalidScope(
            "The requested scope exceeds the scope granted by "
            "the resource owner."
        )

    def invalid_target(self) -> InvalidTarget:
        return InvalidTarget(
            "The requested audience(s) are not previously accepted by "
            "the resource owner."
        )

    def setup(
        self,
        *,
        assertion: Assertion,
        cek: ContentEncryptionKey,
        client: Client,
        authorization: Authorization,
        grant: Grant,
        issuer: TokenIssuer,
        owner: ResourceOwner,
        **_: Any
    ) -> None:
        self.assertion = assertion
        self.authorization = authorization
        self.cek = cek
        self.client = client
        self.grant = grant
        self.issuer = issuer
        self.owner = owner
        
        if grant.must_identify() and client is None:
            raise InvalidClient
        if client is not None:
            if not client.can_grant(self.grant.grant_type):
                raise UnauthorizedClient
            if not client.allows_scope(grant.scope):
                raise self.invalid_scope()

    async def begin(self, request: Request) -> None:
        await self.grant.decrypt(NotImplemented)

    async def handle(self, request: Request) -> fastapi.Response:
        issued = await self.issue(self.grant.root)
        await self.on_grant_obtained(self.grant.root, issued)
        response = fastapi.responses.PlainTextResponse(
            media_type='application/json; indent=2',
            content=issued.model_dump_json(indent=2)
        )
        return response

    async def on_grant_obtained(self, grant: Any, obtained: ObtainedGrant):
        pass

    async def authorization_code(self, grant: AuthorizationCodeGrant) -> ObtainedGrant:
        assert self.authorization is not None
        assert self.client is not None
        assert self.owner is not None
        scope = grant.scope or self.authorization.scope
        if not self.authorization.allows_scope(scope):
            raise self.invalid_scope()

        target = grant.resources or self.authorization.resources
        if not self.authorization.allows_target(target):
            raise self.invalid_target()

        id_token = None
        refresh_token = None
        subject = await self.storage.get(self.owner.sub)
        if subject is None:
            raise NotImplementedError
        at = await self.issuer.access_token(
            signer=self.signer,
            client_id=str(self.client.id),
            aud=set(map(str, target)) or str(self.client.id),
            sub=str(self.owner.pk.sub),
            scope=self.authorization.scope
        )
        
        if self.authorization.grants_id_token():
            await subject.decrypt_keys(self.cek)
            userinfo = await self.factory.userinfo(
                subject=subject,
                scope=grant.scope or self.authorization.scope,
                contributors=[self.authorization, self.client],
                aud=str(self.client.id)
            )
            id_token = await self.issuer.id_token(
                signer=self.signer,
                userinfo=userinfo,
                access_token=at,
                code=grant.code
            )
        if self.authorization.grants_refresh_token():
            refresh_token = await self.issuer.refresh_token(
                signer=self.signer,
                client=self.client,
                owner=self.owner,
                authorization=self.authorization
            )
        return ObtainedGrant(
            token_type='Bearer',
            expires_in=self.issuer.default_ttl,
            access_token=at,
            id_token=id_token,
            refresh_token=refresh_token
        )

    async def client_credentials(self, grant: ClientCredentialsGrant) -> ObtainedGrant:
        assert self.client is not None
        return ObtainedGrant(
            token_type='Bearer',
            expires_in=self.issuer.default_ttl,
            access_token=await self.issuer.access_token(
                signer=self.signer,
                client_id=str(self.client.id),
                sub=str(self.client.id),
                scope=grant.scope
            )
        )

    async def jwt(self, grant: JWTBearerGrant) -> ObtainedGrant:
        assert self.assertion is not None
        assert self.client is not None
        if self.assertion.is_self_issued():
            raise NotImplementedError

        owner = await self.storage.get(self.assertion.owner)
        if owner is None:
            raise InvalidRequest(
                "The resource owner identified by the assertion "
                "does not exist."
            )
        if not owner.grants_consent(grant.scope):
            raise InvalidScope(
                "The requested scope exceeds the scope granted by "
                "the resource owner."
            )

        return ObtainedGrant(
            token_type='Bearer',
            expires_in=self.issuer.default_ttl,
            access_token=await self.issuer.access_token(
                signer=self.signer,
                client_id=str(self.client.id),
                sub=self.assertion.sub,
                scope=grant.scope
            )
        )

    async def refresh_token(self, grant: RefreshTokenGrant) -> ObtainedGrant:
        assert self.authorization is not None
        assert self.client is not None
        scope = grant.scope or self.authorization.scope
        if not self.authorization.allows_scope(scope):
            raise self.invalid_scope()
        target = grant.resources or self.authorization.resources
        if not self.authorization.allows_target(target):
            raise self.invalid_target()
        return ObtainedGrant(
            token_type='Bearer',
            expires_in=self.issuer.default_ttl,
            access_token=await self.issuer.access_token(
                signer=self.signer,
                client_id=str(self.client.id),
                sub=str(self.authorization.sub),
                scope=scope
            ),
            refresh_token=grant.refresh_token
        )

    @functools.singledispatchmethod
    async def issue(self, grant: Any) -> ObtainedGrant:
        raise NotImplementedError

    @issue.register
    async def _(self, grant: AuthorizationCodeGrant) -> ObtainedGrant:
        return await self.authorization_code(grant)

    @issue.register
    async def _(self, grant: ClientCredentialsGrant) -> ObtainedGrant:
        return await self.client_credentials(grant)

    @issue.register
    async def _(self, grant: JWTBearerGrant) -> ObtainedGrant:
        return await self.jwt(grant)

    @issue.register
    async def _(self, grant: RefreshTokenGrant) -> ObtainedGrant:
        return await self.refresh_token(grant)