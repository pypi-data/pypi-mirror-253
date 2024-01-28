# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import inspect
from typing import Any

import fastapi

from oauthx.lib import utils
from oauthx.lib.exceptions import StopSnooping
from oauthx.lib.params import ClientAuthorizationState
from .models import Client


class ClientResolver:
    __module__: str = 'oauthx.client'
    _is_coroutine = asyncio.coroutines._is_coroutine # type: ignore
    request_attname: str = 'oauth_client'

    @utils.class_property
    def __signature__(cls) -> inspect.Signature:
        return utils.merge_signatures([
            inspect.signature(cls.__call__),
            inspect.signature(cls.resolve)
        ])

    def __new__(cls, *args: Any, **kwargs: Any):
        self = super().__new__(cls, *args, **kwargs)

        # Check if the asyncio.iscoroutinefunction() call returns
        # True for this object, since it depends on a private
        # symbol.
        assert asyncio.iscoroutinefunction(self) # nosec
        return self

    def as_provider(self) -> Any:
        async def f(request: fastapi.Request, state: ClientAuthorizationState) -> None:
            if state is None:
                raise StopSnooping
            setattr(request, 'provider', await self.get(state.client_id))
        return fastapi.Depends(f)

    async def get(self, client_id: str) -> Client:
        raise NotImplementedError

    async def resolve(self, *args: Any, **kwargs: Any) -> Client:
        raise NotImplementedError

    async def __call__(
        self,
        request: fastapi.Request,
        **kwargs: Any
    ) -> None:
        client = await utils.merged_call(self.resolve, {
            'request': request,
            **kwargs
        })
        setattr(request, self.request_attname, client)