# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

from oauthx.lib import RFC9068AccessToken
from oauthx.lib import ServerMetadata
from oauthx.lib.types import AccessTokenHash


class Request(fastapi.Request):
    access_token: RFC9068AccessToken
    at_hash: AccessTokenHash
    issuer: ServerMetadata