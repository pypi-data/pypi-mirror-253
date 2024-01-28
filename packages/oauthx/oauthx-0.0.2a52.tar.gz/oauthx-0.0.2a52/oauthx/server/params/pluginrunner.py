# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import itertools
from typing import Annotated
from typing import TypeAlias

import fastapi

from oauthx.server.models import AuthorizationRequest
from oauthx.server.protocols import IClient
from oauthx.server.request import Request
from .currentsubject import CurrentSubject
from .objectfactory import ObjectFactory
from .storage import Storage


__all__: list[str] = ['PluginRunner']


class _PluginRunner:
    plugins: list

    def __init__(
        self,
        request: Request,
        factory: ObjectFactory,
        storage: Storage,
        subject: CurrentSubject
    ):
        self.plugins = [ # type: ignore
            cls(request, factory, storage, subject)
            for cls in request.plugins  # type: ignore
        ]
        self.request = request
        self.storage = storage
        self.subject = subject

    async def validate_scope(
        self,
        client: IClient,
        request: AuthorizationRequest,
        scope: set[str]
    ) -> fastapi.Response | None:
        """Validates the requested scope when authorizing a request
        or issueing a token.
        """
        response = None
        for plugin, name in itertools.product(self.plugins, sorted(scope)):
            if not plugin.handles_scope(name):
                continue
            name, params = await plugin.resolve_scope(client, request, name)
            if not name:
                continue
            url = self.request.url_for(name, pk=request.id, **params)
            response = fastapi.responses.RedirectResponse(
                status_code=302,
                url=url
            )
            break
        return response


PluginRunner: TypeAlias = Annotated[_PluginRunner, fastapi.Depends(_PluginRunner)]