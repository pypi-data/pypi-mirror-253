# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Awaitable
from typing import Callable
from typing import TypeAlias

from oauthx.lib import AuthorizationRequest
from oauthx.lib import ClientAuthorizationState
from oauthx.lib import Error
from oauthx.lib import RedirectionParameters


AuthorizeReturn: TypeAlias = tuple[AuthorizationRequest, Error | RedirectionParameters, ClientAuthorizationState]

AuthorizeFactory: TypeAlias = Callable[..., Awaitable[AuthorizeReturn]]