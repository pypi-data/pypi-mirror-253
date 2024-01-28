# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

from .application import create_application
from .auth import AuthorizationCodeCredential
from .clientresolver import ClientResolver
from .settings import ClientSettings
from .defaultclient import DefaultClient
from .localclientrepository import LocalClientRepository
from .models import *
from .redirectionrouter import RedirectionRouter
from . import params
from . import protocols


__all__: list[str] = [
    'create_application',
    'AuthorizationCodeCredential',
    'Client',
    'ClientSettings',
    'ClientResolver',
    'DefaultClient',
    'LocalClientRepository',
    'RedirectionRouter',
]


def setup_dependencies(
    storage_class: Any
) -> list[Any]:
    return [
        params.ClientStorageImplementation(storage_class)
    ]