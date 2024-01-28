# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import fastapi
import fastapi.params

from oauthx.server.config import ProviderConfig
from oauthx.server.params import ClientAuthorizationState
from oauthx.server.params import CurrentSubject
from oauthx.server.params import ObtainedGrant
from oauthx.server.params import OIDCToken
from oauthx.server.params import ReturnURL
from oauthx.server.params import SubjectLogger
from oauthx.server.params import UpstreamProvider
from oauthx.server.request import Request
from oauthx.server.types import AccountIssues
from ..baserequesthandler import BaseRequestHandler
from .params import AuthorizationRequest
from .params import Client
from .params import ClientDependency


class UpstreamCallbackHandler(BaseRequestHandler):
    __module__: str = 'oauthx.server.handlers'
    dependencies: list[fastapi.params.Depends] = [ClientDependency]
    include_in_schema: bool = False
    name: str = 'oauth2.upstream.callback'
    methods: list[str] = ['GET']
    path: str = '/callback'
    provider: ProviderConfig
    response_description: str = "Proceed to the configured return URL"
    return_url: str
    state: ClientAuthorizationState
    summary: str = "Upstream Redirection Endpoint"

    def setup(
        self,
        *,
        client: Client,
        grant: ObtainedGrant,
        id_token: OIDCToken,
        state: ClientAuthorizationState,
        params: AuthorizationRequest,
        provider: UpstreamProvider,
        return_url: ReturnURL,
        subject: CurrentSubject,
        logger: SubjectLogger,
        **_: Any
    ):
        self.client = client
        self.grant = grant
        self.id_token = id_token
        self.params = params
        self.provider = provider
        self.publisher = logger
        self.return_url = return_url
        self.subject = subject
        self.state = state

    async def handle(self, request: Request) -> fastapi.Response:
        """Retrieve the Open ID Connect ID Token from the identity
        provider and authenticate the user. On success, redirect
        the user-agent to the ``return-url`` that was configured
        when the authorization request was created.
        """
        if self.id_token.email is None:
            raise NotImplementedError
        if self.subject is not None:
            raise NotImplementedError
        try:
            subject, created = await self.server.onboard_oidc(
                token=self.id_token,
                use=self.provider.audience,
                request_id=self.params.id,
                client_id=self.client.client_id,
            )
        except self.server.OrphanedPrincipal:
            raise AccountIssues
        await self.storage.delete(self.state)
        if created:
            self.publisher.onboarded(
                sub=int(subject.get_primary_key()), # type: ignore
                registrar='self',
                authorization_id=self.params.id,
                client_id=self.client.client_id
            )
        request.authenticate(
            sub=str(subject.get_primary_key()),
            email=self.id_token.email
        )
        return self.redirect(self.return_url)