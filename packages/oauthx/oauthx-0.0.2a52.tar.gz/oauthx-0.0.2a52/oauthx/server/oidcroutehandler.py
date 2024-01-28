# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import logging
import uuid
from typing import Any
from typing import Callable
from typing import Coroutine

import fastapi
import fastapi.routing
import starlette.responses

from oauthx.lib.exceptions import Error
from oauthx.lib.exceptions import UserAgentException
from .config import Config
from .request import Request
from .types import InteractionException
from .types import InvalidAuthorizationRequest
from .types import LoginRequired


class OIDCRouteHandler(fastapi.routing.APIRoute):
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
                for error in e.errors():
                    ctx = error.get('ctx')
                    if not ctx or not ctx.get('error'):
                        continue
                    e = ctx['error']
                    if isinstance(e, Error):
                        response = await request.error(
                            e.get_template_names(),
                            error=e.error,
                            error_description=e.error_description,
                            status_code=e.status_code,
                            media_type=e.media_type,
                            context={**e.get_context(), 'exception': e},
                            allow_redirect=e.allow_redirect
                        )
                        break
                else:
                    raise NotImplementedError
            except UserAgentException as e:
                response = await e.render_to_response(
                    request=request,
                    templates=request.templates
                )
            except LoginRequired as e:
                response = e.redirect(request, self.login_endpoint, str(request.url))
            except (Error, InteractionException, InvalidAuthorizationRequest) as e:
                self.logger.error(
                    "Caught fatal %s (error: %s, error_description: %s)",
                    type(e).__name__, e.error, e.error_description)
                response = await request.error(
                    e.get_template_names(),
                    error=e.error,
                    error_description=e.error_description,
                    status_code=e.status_code,
                    media_type=e.media_type,
                    context={**e.get_context(), 'exception': e},
                    allow_redirect=e.allow_redirect
                )
            except Exception as e:
                self.logger.exception("Caught fatal %s", type(e).__name__)
                response = await request.error(
                    'oauthx/errors/fatal.html.j2',
                    error='server_error',
                    error_description=(
                        "The authorization server encountered an unexpected "
                        "condition that prevented it from fulfilling the "
                        "request."
                    ),
                    status_code=500,
                    context={'incident_id': str(uuid.uuid4())}
                )
            response = await request.process_response(response)
            response.headers.update({
                'permissions-policy': str.join(',', [
                    'accelerometer=()',
                    'ambient-light-sensor=()',
                    'autoplay=()',
                    'battery=()',
                    'camera=()',
                    'display-capture=()',
                    'document-domain=()',
                    'encrypted-media=()',
                    'fullscreen=()',
                    'gamepad=()',
                    'geolocation=()',
                    'gyroscope=()',
                    'layout-animations=(self)',
                    'legacy-image-formats=(self)',
                    'magnetometer=()',
                    'microphone=()',
                    'midi=()',
                    'oversized-images=(self)',
                    'payment=()',
                    'picture-in-picture=()',
                    'publickey-credentials-get=()',
                    'speaker-selection=()',
                    'sync-xhr=(self)',
                    'unoptimized-images=(self)',
                    'unsized-media=(self)',
                    'usb=()',
                    'screen-wake-lock=()',
                    'web-share=()',
                    'xr-spatial-tracking=()'
                ]),
                'referrer-policy': 'no-referrer',
                'x-content-type-options': 'nosniff',
                'x-frame-options': 'deny',
                'x-permitted-cross-domain-policies': 'none',
            })
            if request.url.scheme == 'https':
                response.headers['strict-transport-security'] = 'max-age=31536000; includeSubDomains; preload'
            return response

        return f