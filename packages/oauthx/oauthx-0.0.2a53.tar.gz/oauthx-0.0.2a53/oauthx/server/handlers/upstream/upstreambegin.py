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

from oauthx.server.params import CurrentSubject
from oauthx.server.request import Request
from ..baserequesthandler import BaseRequestHandler


class UpstreamBeginHandler(BaseRequestHandler):
    __module__: str = 'oauthx.server.handlers'
    include_in_schema: bool = False
    name: str = 'oauth2.upstream.begin'
    methods: list[str] = ['POST']
    path: str = '/begin'
    response_description: str = "Initiate the authentication flow"
    subject: CurrentSubject
    summary: str = "Upstream provider"

    def setup(
        self,
        *,
        request_id: str = fastapi.Form(...),
        client_id: str = fastapi.Form(...),
        provider: str = fastapi.Form(...),
        next_url: str = fastapi.Form(...),
        subject: CurrentSubject,
        **_: Any
    ):
        self.client_id = client_id
        self.next_url = next_url
        self.request_id = request_id
        self.provider = self.config.get_provider(provider)
        self.subject = subject

    async def begin(self, request: Request) -> None:
        if self.provider is not None:
            await self.provider
        return await super().begin(request)

    async def handle(self, request: Request) -> fastapi.Response:
        if self.provider is None or self.subject is not None:
            return fastapi.Response(status_code=403)
        state = await self.provider.identify(
            client_id=self.client_id,
            redirect_uri=str(request.url_for('oauth2.upstream.callback')),
            return_url=self.next_url
        )
        state.annotate('request', str(self.request_id))
        await self.storage.persist(state)
        self.logger.debug(
            "Initiating OIDC login flow (provider: %s, client: %s, request: %s)",
            self.provider.name, self.client_id, self.request_id
        )
        return fastapi.responses.RedirectResponse(
            status_code=302,
            url=state.authorize_url
        )