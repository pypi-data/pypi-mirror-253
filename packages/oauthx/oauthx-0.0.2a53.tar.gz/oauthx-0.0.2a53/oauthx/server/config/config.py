# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import os

import aiopki
import jinja2
import pydantic
import yaml
from canonical import PythonSymbol

from oauthx.lib.protocols import IStorage
from oauthx.lib.types import GrantType
from oauthx.lib.utils.loader import import_symbol
from oauthx.server.models import Client
from oauthx.server.protocols import IRequestSubject
from oauthx.server.protocols import IPlugin
from .authenticationconfig import AuthenticationConfig
from .cacheconfig import CacheConfig
from .implementationconfig import ImplementationConfig
from .issuerconfig import IssuerConfig
from .providerconfig import ProviderConfig
from .scopespecification import ScopeSpecification
from .storageconfig import StorageConfig
from .uiconfig import UIConfig


class Config(pydantic.BaseModel):
    authentication: AuthenticationConfig
    cache: CacheConfig = pydantic.Field(
        default_factory=CacheConfig
    )

    client: Client | None
    grant_types_supported: set[GrantType] = set()
    impl: ImplementationConfig
    issuer: IssuerConfig
    plugins: list[PythonSymbol[type[IPlugin]]] = []
    providers: list[ProviderConfig] = []
    scopes: list[ScopeSpecification] = []
    storage: StorageConfig
    ui: UIConfig

    @property
    def storage_class(self) -> type[IStorage]:
        return import_symbol(self.impl.storage)

    @property
    def subject_class(self) -> type[IRequestSubject]:
        return import_symbol(self.impl.subject)

    @classmethod
    def load(cls, fp: str) -> 'Config':
        with open(fp, 'r') as f:
            t = jinja2.Template(
                source=f.read(),
                undefined=jinja2.StrictUndefined,
                variable_start_string='${',
                variable_end_string='}'
            )
        c = {
            'env': dict(os.environ)
        }
        return cls.model_validate(yaml.safe_load(t.render(c)))

    async def discover(self):
        await asyncio.gather(*map(ProviderConfig.discover, self.providers))
        return self

    def get_cek(self) -> aiopki.CryptoKeyType:
        return self.storage.encryption_key

    def get_splash_image_url(self) -> str:
        return 'https://static.webiam.id/shared/splash.jpg'

    def get_provider(self, name: str) -> ProviderConfig | None:
        return {x.name: x for x in self.providers}.get(name)

    def has_authorize_endpoint(self) -> bool:
        """Return a boolean indicating if the authorization server should
        expose the Authorization Endpoint.
        """
        return 'authorization_code' in self.grant_types_supported
    
    def __await__(self):
        return self.discover().__await__()
