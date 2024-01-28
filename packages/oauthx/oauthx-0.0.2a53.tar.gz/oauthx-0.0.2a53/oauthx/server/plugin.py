# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import fastapi

from oauthx.lib.protocols import IClient
from .models import Authorization
from .params import ObjectFactory
from .params import Storage
from .params import CurrentSubject
from .request import Request


class Plugin:
    __module__: str = 'oauthx.server'

    def __init__(
        self,
        request: Request,
        factory: ObjectFactory,
        storage: Storage,
        subject: CurrentSubject,
        authorization: Authorization | None = None
    ) -> None:
        self.authorization = authorization
        self.factory = factory
        self.request = request
        self.storage = storage
        self.subject = subject

    @classmethod
    def __register__(cls, app: fastapi.FastAPI | fastapi.APIRouter) -> None:
        pass

    def handles_scope(self, name: str) -> bool:
        """Return a boolean indicating if the handler knows the
        give scope `name`.
        """
        return False

    async def render_to_response(
        self,
        template_names: list[str] | str,
        context: dict[str, Any] | None = None,
        status_code: int = 200,
        headers: dict[str, Any] | None = None
    ) -> fastapi.Response:
        return await self.request.render_to_response(
            template_names=template_names,
            context=context,
            status_code=status_code,
            headers=headers
        )

    async def resolve_scope(
        self,
        client: IClient,
        authorization: Authorization,
        name: str
    ) -> tuple[str | None, dict[str, str]]:
        """Ensure that the given scope can be granted. Return
        ``None`` if the scope can be granted, otherwise
        return a tuple containing a named URL (string) and
        its parameters (dict).
        """
        raise NotImplementedError