# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import TypeVar

import fastapi
import fastapi.params
from canonical.protocols import ICache

from oauthx.lib import MemoryCache
from oauthx.lib.params import ApplicationCache
from .models import *
from .params import *
from .resourceroute import ResourceRoute
from .resourcerouter import ResourceRouter


__all__: list[str] = [
    'AccessToken',
    'RequestAccessToken',
    'RequestSubject',
    'RequiredScope',
    'ResourceRoute',
    'ResourceRouter',
]


T = TypeVar('T', bound=fastapi.FastAPI)


def application_factory(
    cache: type[ICache] = MemoryCache,
    cls: type[T] = fastapi.FastAPI,
    **kwargs: Any
) -> T:
    dependencies: list[fastapi.params.Depends] = kwargs.setdefault('dependencies', [])
    dependencies.extend([
        ApplicationCache(cache)
    ])
    return cls(**kwargs)