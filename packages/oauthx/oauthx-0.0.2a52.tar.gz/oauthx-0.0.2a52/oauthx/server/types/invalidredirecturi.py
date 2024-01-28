# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.lib.exceptions import InteractionException


class InvalidRedirectURI(InteractionException):
    """Raised when the redirect URI is invalid. Per :rfc:`6749`, this
    is a fatal error that should not redirect the user-agent back
    to the redirection endpoint (because its invalid).
    """
    __module__: str = 'oauthx.server.types'
    status_code = 403
    template_name = 'oauthx/errors/authorize.redirect.html.j2'