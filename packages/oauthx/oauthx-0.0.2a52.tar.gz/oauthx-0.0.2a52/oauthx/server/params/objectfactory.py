# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Annotated
from typing import TypeAlias

import fastapi

from oauthx.lib.params import Storage
from oauthx.server.config import Config
from oauthx.server.models import ObjectFactory as DefaultImplementation
from .currentconfig import CurrentConfig
from .issueridentifier import IssuerIdentifier
from .masker import Masker


__all__: list[str] = ['ObjectFactory']


async def get(
    issuer: IssuerIdentifier,
    masker: Masker,
    storage: Storage,
    config: Config = CurrentConfig
) -> DefaultImplementation:
    return DefaultImplementation(
        issuer=issuer,
        masker=masker, # type: ignore
        storage=storage,
        scopes=[x.scope for x in config.scopes],
    )


ObjectFactory: TypeAlias = Annotated[DefaultImplementation, fastapi.Depends(get)]