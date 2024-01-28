# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.lib.exceptions import InteractionException


class InvalidClient(InteractionException):
    __module__: str = 'oauthx.server.types'
    error: str = 'invalid_client'
    error_description: str = (
        'Client authentication failed (e.g., unknown client, '
        'no client authentication included, or unsupported '
        'authentication method)'
    )
    status_code = 401
    template_name = 'oauthx/errors/authorize.invalid_client.html.j2'