# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

from oauthx.lib.types import RedirectURI


class InvalidAuthorizationRequest(Exception):
    __module__: str = 'oauthx.types'
    allow_redirect: bool = True
    kind: str = 'authorize'
    media_type: str | None = None
    redirect_uri: RedirectURI | None = None
    status_code: int = 400
    template_name: str = 'oauthx/errors/authorize.html.j2'

    def __init__(
        self,
        *,
        error: str,
        context: Any,
        error_description: str | None = None,
        error_uri: str | None = None,
        redirect_uri: RedirectURI | None = None,
        allow_redirect: bool = True
    ):
        self.allow_redirect = allow_redirect
        self.context = context
        self.error = error
        self.error_description = error_description
        self.error_uri = error_uri
        self.redirect_uri = redirect_uri

    def get_context(self) -> dict[str, Any]:
        return {}

    def get_template_names(self) -> list[str] | str:
        return [
            f'oauthx/errors/{self.kind}.{self.error}.html.j2',
            self.template_name
        ]