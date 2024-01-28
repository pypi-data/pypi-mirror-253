# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .models import AuthorizationRequest
from .request import Request


class Policy:
    __module__: str = 'oauthx.server'

    async def apply(
        self,
        request: Request,
        params: AuthorizationRequest
    ) -> None:
        pass

    def error(
        self,
        error: str,
        error_description: str | None = None,
        error_uri: str | None = None
    ) -> None:
        pass