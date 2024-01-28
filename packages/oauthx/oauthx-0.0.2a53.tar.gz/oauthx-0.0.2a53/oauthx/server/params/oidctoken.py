# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import warnings
from typing import Annotated
from typing import TypeAlias

import fastapi
from aiopki.ext import jose

from oauthx.lib.params import ClientAuthorizationState
from .obtainedgrant import ObtainedGrant
from .requestingclient import RequestingClient
from .upstreamprovider import UpstreamProvider


__all__: list[str] = ['OIDCToken']


def get(
    client: RequestingClient,
    state: ClientAuthorizationState,
    grant: ObtainedGrant,
    provider: UpstreamProvider
) -> jose.OIDCToken:
    warnings.warn("OIDC ID Token is not verified.")
    if grant.id_token is None:
        raise NotImplementedError
    token = grant.id_token.payload(jose.OIDCToken.model_validate)
    return provider.process_oidc_token(client, state, token)


OIDCToken: TypeAlias = Annotated[jose.OIDCToken, fastapi.Depends(get)]