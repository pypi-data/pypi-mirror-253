# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.lib.exceptions import InteractionException


class UnauthorizedAccount(InteractionException):
    __module__: str = 'oauthx.server.types'
    allow_redirect: bool = False
    error: str = 'unauthorized_account'
    error_description: str = (
        'The identified account is not authorized to use '
        'delegation through this client.'
    )
    status_code = 403
    template_name = 'oauthx/errors/authorize.unauthorized_account.html.j2'