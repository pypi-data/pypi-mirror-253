# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Iterable
from typing import Literal

import httpx

from oauthx.client.models import Client
from oauthx.lib.models import ObtainedGrant
from oauthx.client.auth import LocalAuthorization


class GoogleCommandLineAuth(LocalAuthorization):
    use: Literal['access_token', 'id_token']

    def __init__(
        self,
        scope: Iterable[str] | None = None,
        path: str | None = None,
        use: Literal['access_token', 'id_token'] = 'access_token'
    ):
        client = Client.model_validate({
            'provider': 'https://accounts.google.com',
            'client_id': '764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com',
            'credential': 'd-FL95Q19q7MQmFpd7hHD0Ty',
            'token_endpoint_auth_method': 'client_secret_basic'
        })
        scope = set(scope or [])
        scope.update(['email'])
        super().__init__(client, scope, path)
        self.use = use

    def get_token(self, grant: ObtainedGrant) -> str:
        token = grant.access_token
        if self.use == 'id_token':
            assert grant.id_token is not None
            token = grant.id_token.encode(bytes.decode, compact=True)
        return token