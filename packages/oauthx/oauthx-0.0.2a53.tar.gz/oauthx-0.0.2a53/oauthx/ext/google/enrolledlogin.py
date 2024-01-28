# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from gettext import gettext as _
from typing import Any

import fastapi

from oauthx.server.config import ProviderConfig
from oauthx.server.handlers import BaseLoginRequestHandler


class EnrolledLoginRequestHandler(BaseLoginRequestHandler):
    __module__: str = 'oauthx.ext.google'

    def get_context(self, request: fastapi.Request) -> dict[str, Any]:
        ctx = super().get_context(request)
        return {
            **ctx,
            'deny_url': None,
            'page_title': _("Sign in for work or school"),
            'previous_url': request.url_for('oauth2.login')\
                .include_query_params(**request.query_params),
        }

    def get_templates(self) -> list[str]:
        return ['oauthx/login.upstream.enrolled.html.j2']

    def get_providers(self) -> list[ProviderConfig]:
        return [x for x in self.config.providers if x.audience == 'institutional']