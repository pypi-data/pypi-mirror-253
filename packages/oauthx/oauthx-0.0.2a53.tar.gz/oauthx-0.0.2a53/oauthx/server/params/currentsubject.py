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

from oauthx.lib.params import Logger
from oauthx.server.protocols import ISubject
from oauthx.server.request import Request
from .storage import Storage


__all__: list[str] = ['CurrentSubject']


async def get(
    logger: Logger,
    request: Request,
    storage: Storage
) -> ISubject | None:
    if request.subject:
        logger.debug(
            "Retrieving Subject from storage (sub: %s)",
            str(request.subject.pk)
        )
        return await storage.get(request.subject.pk)


CurrentSubject: TypeAlias =  Annotated[ISubject | None, fastapi.Depends(get, use_cache=True)]