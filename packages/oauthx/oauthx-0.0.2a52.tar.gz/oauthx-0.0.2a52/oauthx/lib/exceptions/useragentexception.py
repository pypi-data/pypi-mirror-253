# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import uuid
from typing import Any

from canonical.protocols import ITemplateService
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi import Response


class UserAgentException(Exception):
    """An exception class that indicates that a HTML response
    may be sent to the user agent.

    Args:
        error (str): the OAuth 2.x/OpenID Connect error code
            identifying the error condition that occurred. 
    """
    __module__: str = 'oauthx.types'
    allow_redirect: bool
    context: dict[str, Any]
    status_code: int = 400
    template_name: str

    def __init__(
        self,
        *,
        error: str,
        error_description: str | None = None,
        context: dict[str, Any] | None = None
    ):
        self.context = context or {}
        self.error = error
        self.error_description = error_description
        self.id = uuid.uuid4()

    async def render_to_response(
        self,
        request: Request,
        templates: ITemplateService
    ) -> Response:
        return HTMLResponse(
            status_code=self.status_code,
            headers={
                'X-Error': self.error,
                'X-Error-Description': self.error_description or ''
            },
            content=await templates.render_template(
                self.get_template_names(),
                context={
                    **self.context,
                    'error': self.error,
                    'error_description': self.error_description,
                    'exception': self,
                    'incident_id': self.id,
                    'request': request
                }
            )
        )
        
    def get_template_names(self) -> list[str] | str:
        return self.template_name