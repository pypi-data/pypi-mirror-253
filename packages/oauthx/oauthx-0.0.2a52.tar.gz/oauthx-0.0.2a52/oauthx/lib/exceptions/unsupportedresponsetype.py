# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .fatalerror import FatalError


class UnsupportedResponseType(FatalError, ValueError):
    __module__: str = 'oauthx.types'

    def __init__(self, url: str | None = None, allow_redirect: bool = False):
        FatalError.__init__(
            self,
            error='unsupported_response_type',
            error_description=(
                "The requested response type is not allowed by the client or "
                "not supported by the authorization server."
            ),
            error_uri=url,
            allow_redirect=allow_redirect
        )