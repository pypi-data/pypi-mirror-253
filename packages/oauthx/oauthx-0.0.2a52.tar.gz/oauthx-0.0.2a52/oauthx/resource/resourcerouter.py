# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Iterable
from typing import Literal

import fastapi

from .params import RequestAccessToken
from .params import RequiredScope
from .resourceroute import ResourceRoute


class ResourceRouter(fastapi.APIRouter):

    def __init__(
        self,
        issuers: Iterable[str],
        scope: Iterable[str] | None = None,
        audience: Literal['server', 'endpoint', 'any'] = 'server',
        authenticated: bool = True,
        *args: Any,
        **kwargs: Any
    ):
        kwargs.setdefault('route_class', ResourceRoute)
        dependencies = kwargs.setdefault('dependencies', [])
        dependencies.extend([
            RequestAccessToken(
                issuers=set(issuers),
                audience=audience,
                required=authenticated
            ),
            RequiredScope(set(scope or []))
        ])
        super().__init__(*args, **kwargs)