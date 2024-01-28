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

from oauthx.lib.params import ClientAuthorizationState
from oauthx.server.config import Config
from oauthx.server.config import ProviderConfig
from oauthx.server.types import StopSnooping
from .currentconfig import CurrentConfig


__all__: list[str] = ['UpstreamProvider']


async def get(
    state: ClientAuthorizationState,
    config: Config = CurrentConfig,
) -> ProviderConfig:
    if state is None:
        raise StopSnooping
    name = state.annotation('provider')
    if name is None:
        raise NotImplementedError
    provider = config.get_provider(name)
    if provider is None:
        raise NotImplementedError(name)
    return provider


UpstreamProvider: TypeAlias = Annotated[
    ProviderConfig,
    fastapi.Depends(get)
]