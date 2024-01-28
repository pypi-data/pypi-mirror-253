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

from oauthx.lib.exceptions import Error
from .config import Config
from .request import Request


class ClientRouteHandler(fastapi.routing.APIRoute):
    config: Config
    logger: logging.Logger = logging.getLogger('uvicorn')
    login_endpoint: str

    def get_route_handler(self) -> Callable[[fastapi.Request], Coroutine[Any, Any, starlette.responses.Response]]:
        handler = super().get_route_handler()

        async def f(request: fastapi.Request) -> starlette.responses.Response:
            request = Request(request.scope, request.receive)
            request.config = self.config # type: ignore
            try:
                response = await handler(request)
            except fastapi.exceptions.RequestValidationError as e:
                # If any of the error is in the path, then the response is
                # 404, else 400.
                self.logger.exception("Error")
                response = fastapi.responses.JSONResponse(
                    status_code=400,
                    headers={
                        'X-Error': 'invalid_request'
                    },
                    content={
                        'error': 'invalid_request',
                        'error_description': (
                            "The request is missing a required parameter, "
                            "includes an unsupported parameter value (other "
                            "than grant type), repeats a parameter, includes "
                            "multiple credentials, utilizes more than one "
                            "mechanism for authenticating the client, or is "
                            "otherwise malformed."
                        )
                    }
                )
            except Error as e:
                self.logger.error("Caught fatal %s", type(e).__name__)
                response = fastapi.responses.JSONResponse(
                    status_code=e.status_code,
                    content=e.dict()
                )
            except Exception as e:
                self.logger.exception("Caught fatal %s", type(e).__name__)
                response = fastapi.responses.JSONResponse(
                    status_code=500,
                    content={
                        'error': 'server_error',
                        'error_description': (
                            "The authorization server encountered an unexpected "
                            "condition that prevented it from fulfilling the "
                            "request."
                        ),
                    }
                )
            return await request.process_response(response)

        return f