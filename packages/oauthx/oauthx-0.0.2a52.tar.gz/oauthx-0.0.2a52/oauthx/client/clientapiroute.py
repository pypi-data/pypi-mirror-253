# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import logging
from typing import Any
from typing import Callable
from typing import Coroutine

import fastapi
import fastapi.routing
import starlette.responses
from canonical.exceptions import ProgrammingError

from oauthx.lib.exceptions import InteractionException


class ClientAPIRoute(fastapi.routing.APIRoute):
    logger: logging.Logger = logging.getLogger('uvicorn')

    def get_route_handler(self) -> Callable[[fastapi.Request], Coroutine[Any, Any, starlette.responses.Response]]:
        handler = super().get_route_handler()

        async def f(request: fastapi.Request) -> starlette.responses.Response:
            request = self.setup_request(request)
            try:
                response = await handler(request)
            except InteractionException as e:
                templates = getattr(request, 'templates', None)
                if templates is None:
                    raise ProgrammingError(
                        "Ensure that the ITemplateService dependency is "
                        "injected."
                    )
                response = await e.render_to_response(templates)
            return await self.process_response(response)

        return f

    async def process_response(self, response: fastapi.Response) -> fastapi.Response:
        response.headers.update({
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        })
        return response

    def setup_request(self, request: Any) -> Any:
        return request