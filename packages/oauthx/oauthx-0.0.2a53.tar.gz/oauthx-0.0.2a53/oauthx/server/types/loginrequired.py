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
import fastapi.responses

from oauthx.lib.protocols import IClient


class LoginRequired(RuntimeError):
    __module__: str = 'oauthx.types'
    client: IClient

    @property
    def client_id(self) -> str:
        return str(self.client.id)

    def __init__(self, client: IClient, deny_url: str | None = None, next_url: str | None = None, **params: Any):
        self.client = client
        self.deny_url = deny_url
        self.next_url = next_url
        self.params = params

    def redirect(self, request: fastapi.Request, name: str, next_url: str) -> fastapi.Response:
        params: dict[str, str] = {
            **self.params,
            'client_id': self.client.id
        }
        if self.deny_url:
            params['d'] = self.deny_url
        if next_url:
            params['n'] = self.next_url or next_url
        return fastapi.responses.RedirectResponse(
            status_code=302,
            url=request.url_for(name).include_query_params(**params),
        )