# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi
import fastapi.params

from oauthx.lib.exceptions import InsufficientScope
from .accesstoken import AccessToken


__all__: list[str] = ['RequiredScope']


def RequiredScope(scope: set[str]) -> fastapi.params.Depends:
    def f(at: AccessToken) -> None:
        if not at.validate_scope(scope):
            raise InsufficientScope
    return fastapi.Depends(f)