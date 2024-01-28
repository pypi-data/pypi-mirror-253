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

from oauthx.lib.exceptions import InvalidToken
from oauthx.resource import AccessToken
from oauthx.server.models import SubjectKey
from oauthx.server.params import Storage
from oauthx.server.protocols import ISubject


async def get(at: AccessToken, storage: Storage) -> ISubject:
    subject = await storage.get(SubjectKey(at.sub))
    if subject is None:
        raise InvalidToken(
            "The subject identified by the access token does not "
            "exist."
        )
    return subject


Subject: TypeAlias = Annotated[ISubject, fastapi.Depends(get)]

