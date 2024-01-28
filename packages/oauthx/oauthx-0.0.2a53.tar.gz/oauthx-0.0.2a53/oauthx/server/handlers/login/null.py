# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

from oauthx.server.request import Request

from .base import BaseLoginRequestHandler


class NullLoginRequestHandler(BaseLoginRequestHandler):
    __module__: str = 'oauthx.server.handlers'

    async def handle(self, request: Request) -> fastapi.Response:
        return await request.render_to_response(
            template_names='oauthx/docs/implement-login.html.j2',
        )