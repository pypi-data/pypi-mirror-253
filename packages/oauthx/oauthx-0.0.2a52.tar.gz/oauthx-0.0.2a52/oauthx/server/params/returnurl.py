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
from oauthx.server.types import StopSnooping


__all__: list[str] = ['ReturnURL']


async def get(
    state: ClientAuthorizationState,
) -> str:
    if state is None:
        raise StopSnooping
    return_url = state.annotation('return-url')
    if return_url is None:
        raise NotImplementedError
    return return_url


ReturnURL: TypeAlias = Annotated[str, fastapi.Depends(get)]