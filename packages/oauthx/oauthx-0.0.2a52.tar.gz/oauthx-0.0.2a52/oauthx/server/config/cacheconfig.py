# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import aiopki
import pydantic
from canonical import PythonSymbol
from canonical.protocols import ICache


class CacheConfig(pydantic.BaseModel):
    impl: PythonSymbol[type[ICache]] = pydantic.Field(
        default='oauthx.lib.MemoryCache'
    )
    
    encryption_key: aiopki.CryptoKeyType | None = pydantic.Field(
        default=None
    )