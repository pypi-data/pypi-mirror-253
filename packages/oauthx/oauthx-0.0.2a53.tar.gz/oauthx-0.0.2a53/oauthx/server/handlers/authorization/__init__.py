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

from oauthx.server.models import SubjectKey
from oauthx.server.params import AuthorizationServer
from oauthx.server.params import CurrentSubject
from oauthx.server.params import ObjectFactory
from oauthx.server.params import PluginRunner
from oauthx.server.params import RequestSession
from oauthx.server.request import Request
from ..baserequesthandler import BaseRequestHandler
from .params import AuthorizationRequest
from .params import Client
from .params import ResponseMode
from .params import ResourceOwner
from .params import UserInfo



router: fastapi.APIRouter = fastapi.APIRouter()


@router.options('/authorize', name='oauth2.authorize')
async def options(
    client: Client
):
    raise NotImplementedError


@router.get('/authorize', name='oauth2.authorize')
async def get(
    server: AuthorizationServer,
    factory:  ObjectFactory,
    plugins: PluginRunner,
    client: Client,
    mode: ResponseMode,
    params: AuthorizationRequest,
    session: RequestSession,
    userinfo: UserInfo,
) -> fastapi.Response:
    response = await plugins.validate_scope(
        client=client,
        request=params,
        scope=params.scope
    )
    if response is not None:
        return response

    async with params.consume():
        query = await server.authorize(
            client=client,
            userinfo=userinfo,
            params=params,
            mode=mode,
            contributors=[params, session]
        )
        return await mode.redirect(**query)
    authorization = await factory.authorization(
        request=params,
        client_id=client.id,
        lifecycle='GRANTED',
        scope=params.scope,
        sub=SubjectKey(userinfo.sub),
        token_types=mode.get_token_types(),
        contributors=[params, session]
    )
    await authorization.persist()
    await params.delete()
    return mode.redirect()


class AuthorizationRequestHandler(BaseRequestHandler):
    """Provides an interface for the resource owner to authorize a certain
    scope for a client, and redirect back to the clients' redirection
    endpoint.
    """
    __module__: str = 'oauthx.server.handlers'
    client: Client
    name: str = 'oauth2.authorize'
    path: str = '/authorize'
    responses: dict[int | str, Any] = {
        400: {
            'description': (
                "Unrecoverable error that is not allowed to redirect"
            )
        }
    }
    response_class: type[fastapi.Response] = fastapi.responses.RedirectResponse
    response_description: str = "Redirect to the clients' redirection endpoint."
    status_code: int = 302
    subject: CurrentSubject | None
    summary: str = "Authorization Endpoint"

    def setup(
        self,
        *,
        client: Client,
        response_mode: ResponseMode,
        subject: CurrentSubject,
        params: AuthorizationRequest,
        plugins: PluginRunner,
        owner: ResourceOwner,
        session: RequestSession,
        userinfo: UserInfo,
        **_: Any
    ):
        self.client = client
        self.owner = owner
        self.params = params
        self.plugins = plugins
        self.response_mode = response_mode
        self.session = session
        self.subject = subject
        self.userinfo = userinfo

    async def handle(self, request: Request) -> fastapi.Response:
        assert self.subject
        assert self.owner
        response = await self.plugins.validate_scope(
            client=self.client,
            request=self.params,
            scope=self.params.scope
        )
        if response is not None:
            return response

        assert self.params.id
        await self.storage.delete(self.params)
        authorization = await self.factory.authorization(
            request=self.params,
            client_id=self.client.id,
            lifecycle='GRANTED',
            scope=self.params.scope,
            sub=self.subject.get_primary_key(), # type: ignore
            token_types=self.response_mode.get_token_types(),
            contributors=[self.params, self.session]
        )
        await authorization.persist()

        async with self.owner.atomic():
            self.owner.consent(authorization.scope)

        return await self.response_mode.redirect(
            code=await self.server.issue_authorization_code(
                client=self.client,
                owner=self.owner,
                authorization_id=authorization.id,
                redirect_uri=self.params.redirect_uri
            )
        )