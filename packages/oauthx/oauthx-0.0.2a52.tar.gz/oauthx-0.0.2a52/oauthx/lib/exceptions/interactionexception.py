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

import fastapi
from canonical.protocols import ITemplateService


class InteractionException(Exception):
    """Base class for all fatal and non-redirectable exceptions
    raised during an interaction with a :term:`Resource Owner`.
    """
    __module__: str = 'oauthx.server.types'
    allow_redirect: bool = True
    error: str = 'illegal_request'
    error_description: str = 'Your request is blocked.'
    media_type: str = 'text/html'
    status_code: int = 400
    template_name: str = NotImplemented

    def __init__(self, context: dict[str, Any] | None = None) -> None:
        self.context = context or {}
        self.id = str(uuid.uuid4())

    def get_context(self) -> dict[str, Any]:
        return {**self.context, 'incident_id': self.id}

    def get_template_names(self) -> list[str]:
        """Return the list of template names to render the HTML response
        for this exception.
        """
        if self.template_name == NotImplemented:
            raise NotImplementedError
        return [self.template_name]

    async def render_to_response(self, templates: ITemplateService) -> fastapi.Response:
        return fastapi.responses.HTMLResponse(
            status_code=self.status_code,
            headers={
                'X-Error': self.error,
                'X-Error-Description': self.error_description
            },
            content=await templates.render_template(
                templates=self.get_template_names(),
                context=self.get_context()
            )
        )