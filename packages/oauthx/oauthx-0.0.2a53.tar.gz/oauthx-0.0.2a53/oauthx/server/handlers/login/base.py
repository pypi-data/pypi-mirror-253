# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import urllib.parse
from gettext import gettext as _
from typing import Any

import fastapi

from oauthx.server.config import Config
from oauthx.server.config import ProviderConfig
from oauthx.server.params import AuthorizationServer
from oauthx.server.params import CurrentConfig
from oauthx.server.params import CurrentSubject
from oauthx.server.params import ObjectFactory
from oauthx.server.params import RequestSession
from oauthx.server.params import Storage
from oauthx.server.params import TokenSigner
from oauthx.server.request import Request
from oauthx.server.types import StopSnooping
from ..baserequesthandler import BaseRequestHandler
from .params import AuthorizationRequest
from .params import Client


class BaseLoginRequestHandler(BaseRequestHandler):
    __module__: str = 'oauthx.server.handlers'
    client: Client
    name: str = 'oauth2.login'
    next_url: str | None = None
    path: str = '/login'
    return_url: str | None = None
    response_class: type[fastapi.Response] = fastapi.responses.RedirectResponse
    response_description: str = "Proceed with authentication"
    session: RequestSession
    subject: CurrentSubject
    summary: str = "Login Endpoint"

    def __init__(
        self,
        server: AuthorizationServer,
        request: Request,
        client: Client,
        factory: ObjectFactory,
        params: AuthorizationRequest,
        session: RequestSession,
        signer: TokenSigner,
        storage: Storage,
        subject: CurrentSubject,
        config: Config = CurrentConfig,
        deny_url: str | None = fastapi.Query(
            default=None,
            alias='d',
            title="Deny URL"
        ),
        next_url: str | None = fastapi.Query(
            default=None,
            alias='n',
            title="Next URL"
        ),
        return_url: str | None = fastapi.Query(
            default=None,
            alias='b',
            title="Return URL"
        ),
        **kwargs: Any
    ):
        self.client = client
        self.deny_url = deny_url
        self.next_url = next_url
        self.params = params
        self.return_url = return_url
        self.session = session
        self.subject = subject
        super().__init__(
            server=server,
            request=request,
            storage=storage,
            config=config,
            factory=factory,
            signer=signer,
            **kwargs
        )

    def allows_next_url(self, request: Request, url: str | None) -> bool:
        try:
            p = urllib.parse.urlparse(url)
            return all([
                p.scheme == request.url.scheme,
                p.netloc == request.url.netloc
            ])
        except Exception:
            return False

    def get_context(self, request: fastapi.Request) -> dict[str, Any]:
        assert self.client is not None
        return {
            'begin_login_url': request.url_for('oauth2.upstream.begin'),
            'client_id': self.client.client_id,
            'client_name': self.client.get_display_name(),
            'client_audience': self.client.get_audience(),
            'deny_url': self.deny_url,
            'next_url': self.next_url,
            'page_title': _("Sign in"),
            'page_subtitle': _("to continue to **%s**") % self.client.get_display_name(),
            'params': self.params,
            'providers': self.get_providers(),
            'request': self.request
        }

    def get_providers(self) -> list[ProviderConfig]:
        assert self.client is not None
        providers: list[ProviderConfig] = []
        for ref in self.client.get_providers():
            provider = self.config.get_provider(ref.name)
            if provider is None:
                continue
            if self.client.get_audience() not in {provider.audience, None}:
                continue
            providers.append(provider)
        if not providers:
            providers = self.config.providers

        # TODO: the list of providers will be empty if the client
        # specifies an audience that matches none of the providers.
        return providers

    def get_templates(self) -> list[str]:
        assert self.client is not None
        if self.client.get_audience() is not None:
            return ['oauthx/login.client.html.j2']
        return ['oauthx/login.upstream.html.j2']\
            if self.config.providers\
            else ['oauthx/login.html.j2']

    async def prepare(self, request: Request) -> fastapi.Response | None:
        if None in {self.next_url}:
            return await request.render_to_response('oauthx/404.html.j2', status_code=404)
        if any([
            not self.allows_next_url(request, self.next_url),
            self.client is None
        ]):
            raise StopSnooping

    async def handle(self, request: Request) -> fastapi.Response:
        assert self.client is not None
        assert self.next_url is not None
        return await request.render_to_response(
            self.get_templates(),
            context=self.get_context(self.request)
        )