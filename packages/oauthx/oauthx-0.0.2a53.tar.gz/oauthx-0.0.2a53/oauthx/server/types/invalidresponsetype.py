# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.lib.exceptions import InteractionException


class InvalidResponseType(InteractionException):
    """Raised when the `response_type` URI is invalid or not
    allowed by the client.
    """
    __module__: str = 'oauthx.server.types'
    error: str = 'unsupported_response_type'
    status_code = 403
    template_name = 'oauthx/errors/authorize.redirect.html.j2'