# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os
from typing import Any

import fastapi

from oauthx.resource import AccessToken
from oauthx.resource import RequestAccessToken
from oauthx.server.params import ContentEncryptionKey
from oauthx.server.params import HTTPClientDependency
from oauthx.server.params import ObjectFactory
from oauthx.server.request import Request
from ..baserequesthandler import BaseRequestHandler
from .params import Client
from .params import Subject
from .userinforoute import UserInfoRoute


class UserInfoEndpointHandler(BaseRequestHandler):
    __module__: str = 'oauthx.server.handlers'
    methods: list[str] = ['GET']
    name: str = 'oidc.userinfo'
    path: str = '/userinfo'
    dependencies = [
        RequestAccessToken(
            issuers={os.getenv('OAUTH_ISSUER_IDENTIFIER') or 'self'},
            audience='any',
            http_factory=HTTPClientDependency
        )
    ]
    description: str = (
        "Returns Claims about the authenticated End-User. To obtain "
        "the requested Claims about the End-User, the Client makes "
        "a request to the UserInfo Endpoint using an Access Token "
        "obtained through OpenID Connect Authentication. These Claims "
        "are normally represented by a JSON object that contains a "
        "collection of name and value pairs for the Claims."
    )
    response_description: str = (
        "Claims about the authenticated end-user"
    )
    route_class = UserInfoRoute
    status_code: int = 200
    summary: str = "UserInfo Endpoint"

    def setup(
        self,
        *,
        access_token: AccessToken,
        factory: ObjectFactory,
        key: ContentEncryptionKey,
        client: Client,
        subject: Subject,
        **_: Any
    ):
        self.access_token = access_token
        self.factory = factory
        self.client = client
        self.key = key
        self.subject = subject

    async def handle(self, request: Request) -> fastapi.Response:
        await self.subject.decrypt_keys(self.key)
        userinfo = await self.factory.userinfo(
            subject=self.subject,
            scope=self.access_token.scope,
            contributors=[self.client]
        )
        return fastapi.responses.PlainTextResponse(
            status_code=200,
            media_type='application/json;indent=2',
            content=userinfo.model_dump_json(indent=2, exclude_none=True)
        )