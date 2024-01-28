# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

from oauthx.lib.exceptions import UserAgentException
from oauthx.lib.types import RedirectURI


class AccountIssues(UserAgentException):
    __module__: str = 'oauthx.types'
    template_name: str = 'oauthx/errors/account.html.j2'
    status_code: int = 400
    
    def __init__(
        self,
        *,
        allow_redirect: bool = False,
        redirect_uri: RedirectURI | None = None,
        context: dict[str, Any] | None = None
    ):
        return_url = None
        if redirect_uri is not None and allow_redirect:
            return_url = redirect_uri.redirect(error='access_denied')
        super().__init__(
            error='access_denied',
            error_description="There are issues with your account. Please contact support.",
            context={
                **(context or {}),
                'allow_redirect': allow_redirect,
                'return_url': return_url
            }
        )