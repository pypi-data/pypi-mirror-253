# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .fatalerror import FatalError


class InsufficientScope(FatalError, ValueError):
    __module__: str = 'oauthx.types'
    status_code: int = 403
    default_description: str = (
        "The request requires higher privileges than "
        "provided by the access token."
    )

    def __init__(self, description: str | None = None, url: str | None = None, allow_redirect: bool = False):
        FatalError.__init__(
            self,
            error='insufficient_scope',
            error_description=description or self.default_description,
            error_uri=url,
            allow_redirect=allow_redirect
        )