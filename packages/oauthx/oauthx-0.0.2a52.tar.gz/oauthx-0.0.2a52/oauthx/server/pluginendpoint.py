# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import asyncio.coroutines
import inspect
from typing import Annotated
from typing import Any
from typing import Callable
from typing import Literal

import fastapi

from oauthx.lib.utils import merge_signatures
from oauthx.lib.utils import merged_call
from .request import Request
from .params import ContentEncryptionKey
from .params import CurrentSubject
from .params import Storage
from .plugin import Plugin
from .types import AuthorizationRequestKey
from .types import StopSnooping


class PluginEndpoint:
    __module__: str = 'oauthx.server'
    _is_coroutine = asyncio.coroutines._is_coroutine # type: ignore

    @property
    def __signature__(self) -> inspect.Signature:
        sig = merge_signatures([
            inspect.signature(self.__call__),
            inspect.signature(self.plugin_class),
            inspect.signature(self.func)
        ])
        if self.context == 'authorize':
            sig = merge_signatures([sig, inspect.signature(self.authorization)])
        return sig
            

    def authorization(self, authorization_id: Annotated[AuthorizationRequestKey | None, fastapi.Path(..., alias='pk')]) -> None:
        pass

    def __init__(
        self,
        context: Literal['authorize', 'login', 'token'],
        plugin_class: type[Plugin],
        func: Callable[..., Any],
        authenticated: bool = True,
        needs_data: bool = False
    ) -> None:
        self.authenticated = authenticated
        self.context = context
        self.plugin_class = plugin_class
        self.needs_data = needs_data
        self.func = func

        # Check if the asyncio.iscoroutinefunction() call returns
        # True for this object, since it depends on a private
        # symbol.
        assert asyncio.iscoroutinefunction(self) # nosec

    async def __call__(
        self,
        request: Request,
        key: ContentEncryptionKey,
        storage: Storage,
        subject: CurrentSubject,
        authorization_id: AuthorizationRequestKey | None,
        **kwargs: Any
    ) -> Any:
        if self.needs_data and subject is not None:
            await subject.decrypt_keys(key)

        authorization = None
        if authorization_id is not None:
            authorization = await storage.get(authorization_id)
            if authorization is None:
                raise StopSnooping
            request.set_context(await authorization.get_context(storage))
        return await merged_call(self.func, {
            'request': request,
            'storage': storage,
            'subject': subject,
            **kwargs,
            'self': merged_call(self.plugin_class, {
                **kwargs,
                'authorization': authorization,
                'request': request,
                'storage': storage,
                'subject': subject
            })
        })