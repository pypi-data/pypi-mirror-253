# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import json
import logging
from typing import Any
from typing import Callable
from typing import Coroutine

import fastapi
import fastapi.routing
import starlette.responses

from oauthx.lib.exceptions import InvalidRequest
from oauthx.lib.exceptions import InvalidToken
from oauthx.lib.exceptions import InsufficientScope


class ResourceRoute(fastapi.routing.APIRoute):
    logger: logging.Logger = logging.getLogger('uvicorn')

    def get_route_handler(self) -> Callable[[fastapi.Request], Coroutine[Any, Any, starlette.responses.Response]]:
        handler = super().get_route_handler()

        async def f(request: fastapi.Request) -> starlette.responses.Response:
            request = self.setup_request(request)
            try:
                return await handler(request)
            except (InvalidRequest, InvalidToken, InsufficientScope) as e:
                return fastapi.responses.PlainTextResponse(
                    status_code=e.status_code,
                    media_type='application/json;indent=2',
                    headers={
                        'WWW-Authenticate': str.join(',', [
                            f'error="{e.error}"',
                            f'error_description="{e.error_description}"'
                        ])
                    },
                    content=json.dumps({
                        'error': e.error,
                        'error_description': e.error_description
                    }, indent=2)
                )

        return f

    def setup_request(self, request: Any) -> Any:
        return request