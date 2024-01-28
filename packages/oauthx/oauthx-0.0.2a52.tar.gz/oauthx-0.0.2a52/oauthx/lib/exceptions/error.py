# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any


class Error(Exception):
    __module__: str = 'oauthx.lib.exceptions'
    allow_redirect: bool = True
    error: str
    error_description: str | None = None
    error_uri: str | None = None
    media_type: str | None = None
    status_code: int = 400

    @classmethod
    def invalid_request(cls, description: str):
        return cls(error='invalid_request', error_description=description)

    def __init__(
        self,
        *,
        error: str,
        error_description: str | None,
        error_uri: str | None = None,
        allow_redirect: bool = False,
        state: str | None = None,
        **kwargs: Any
    ):
        self.allow_redirect = allow_redirect
        self.error = error
        self.error_description = error_description
        self.error_uri = error_uri
        self.state = state

    def can_redirect(self) -> bool:
        return self.allow_redirect

    def dict(self) -> dict[str, str]:
        dto = {'error': self.error}
        if self.error_description:
            dto['error_description'] = self.error_description
        if self.error_uri:
            dto['error_uri'] = self.error_uri
        return dto

    def fatal(self) -> bool:
        return False

    def get_context(self) -> Any:
        return {}

    def get_template_names(self) -> list[str]:
        return [f'oauthx/errors/error.{self.error}.html.j2']

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.error_description or 'None'}')"