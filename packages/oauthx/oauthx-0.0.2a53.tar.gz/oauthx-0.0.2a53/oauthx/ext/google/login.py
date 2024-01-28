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

from oauthx.server.config import ProviderConfig
from oauthx.server.handlers import BaseLoginRequestHandler


class LoginRequestHandler(BaseLoginRequestHandler):
    __module__: str = 'oauthx.ext.google'

    def get_context(self, request: fastapi.Request) -> dict[str, Any]:
        ctx = super().get_context(request)
        return {
            **ctx,
            'login_internal_url': request.url_for('oauth2.login.enrolled')\
                .include_query_params(**self.request.query_params)
        }

    def get_providers(self) -> list[ProviderConfig]:
        # Return the default providers if the client overrides the
        # set.
        assert self.client is not None
        if self.client.get_audience() is not None:
            return super().get_providers()

        return [x for x in self.config.providers if x.audience == 'personal']