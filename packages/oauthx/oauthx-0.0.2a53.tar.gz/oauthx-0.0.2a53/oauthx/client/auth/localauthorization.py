# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pathlib
import webbrowser
from typing import Iterable

import httpx

from oauthx.client.models import Client
from oauthx.lib.models import ObtainedGrant
from ..cli import LocalRedirection


class LocalAuthorization(httpx.Auth):
    client: Client
    grant: ObtainedGrant | None = None
    path: pathlib.Path | None = None

    def __init__(
        self,
        client: Client,
        scope: Iterable[str] | None = None,
        path: str | None = None
    ):
        self.client = client
        if path is not None:
            self.path = pathlib.Path(path).expanduser()
        self.scope = scope

        # Open the file at the given path to obtain the grant stored
        # locally.
        if self.path and self.path.exists():
            with open(self.path, 'r') as f:
                self.grant = ObtainedGrant.model_validate_json(f.read())

    async def async_auth_flow(self, request: httpx.Request):
        if not self.grant or self.grant.is_expired():
            port = self.client.get_local_port()
            state = await self.client.authorize(
                scope=self.scope,
                redirect_uri=f'http://127.0.0.1:{port}',
            )
            with LocalRedirection(self.client, state, port) as callback:
                webbrowser.open(state.authorize_url, new=2, autoraise=False)
            if callback.grant is None:
                callback.result.raise_for_status()
            assert callback.grant is not None
            self.grant = callback.grant
            await self.on_grant_obtained(self.grant)
            if self.path:
                with open(self.path, 'w') as f:
                    f.write(self.grant.model_dump_json(indent=2))

        self.set_authorization_header(request, self.grant)
        yield request

    async def on_grant_obtained(self, grant: ObtainedGrant) -> None:
        pass

    def get_token(self, grant: ObtainedGrant) -> str:
        return grant.access_token

    def set_authorization_header(self, request: httpx.Request, grant: ObtainedGrant):
        request.headers['Authorization'] = f'Bearer {self.get_token(grant)}'