# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.lib.exceptions import InteractionException


class UnauthorizedClient(InteractionException):
    __module__: str = 'oauthx.server.types'
    error: str = 'unauthorized_client'
    error_description: str = (
        'The identified client is not authorized to use '
        'this authorization grant type.'
    )
    status_code = 400
    template_name = 'oauthx/errors/authorize.unauthorized_client.html.j2'