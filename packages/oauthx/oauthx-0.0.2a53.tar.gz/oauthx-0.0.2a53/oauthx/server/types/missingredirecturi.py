# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.lib.exceptions import InteractionException


class MissingRedirectURI(InteractionException):
    __module__: str = 'oauthx.types'
    allow_redirect: bool = False
    error_description: str = (
        "The client did not configure any redirection endpoints. "
        "Without a redirection endpoint, the authorization code "
        "flow or implicit flow can not be used."
    )
    status_code: int = 400
    template_name: str = 'oauthx/errors/missing-redirect-uri.html.j2'