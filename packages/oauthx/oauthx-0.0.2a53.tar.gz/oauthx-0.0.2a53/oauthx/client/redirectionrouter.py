#!/usr/bin/env python3
# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

from .models import ObtainedCredential
from .params import AuthorizationCodeGrant
from .params import Client
from .params import ClientStorage


class RedirectionRouter(fastapi.APIRouter):
    __module__: str = 'oauthx.client'

    def __init__(self, name: str):
        self.name = name
        super().__init__(
            dependencies=[fastapi.Depends(self.set_client)],
            include_in_schema=True
        )
        self.add_api_route(
            methods=['GET'],
            path='/authorize',
            name=f'oauth2.authorize.{self.name}',
            endpoint=self.authorize,
        )
        self.add_api_route(
            methods=['GET'],
            path='/callback',
            name=f'oauth2.callback.{self.name}',
            endpoint=self.callback,
        )

    async def authorize(
        self, request: fastapi.Request,
        client: Client,
        storage: ClientStorage
    ) -> fastapi.responses.RedirectResponse:
        state = await client.authorize(
            redirect_uri=str(request.url_for(f'oauth2.callback.{self.name}'))
        )
        await storage.persist(state)
        return state.redirect(fastapi.responses.RedirectResponse)

    async def callback(
        self,
        grant: AuthorizationCodeGrant,
        storage: ClientStorage
    ) -> None:
        if not grant.access_token:
            raise NotImplementedError
        credential = ObtainedCredential(
            client_id=self.name,
            name=self.name,
            access_token=grant.access_token,
            refresh_token=grant.refresh_token
        )
        await storage.persist(credential)

    def set_client(self, request: fastapi.Request) -> None:
        setattr(request.state, 'oauth_active_client', self.name)