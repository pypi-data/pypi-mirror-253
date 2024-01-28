# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
import inspect
from typing import Any
from typing import TypeVar

from oauthx.lib import utils
from .config import Config
from .params import CurrentConfig


T = TypeVar('T')


class BaseTokenRevoker:
    __module__: str = 'oauthx.server.ref'
    config: Config

    @utils.class_property
    def __signature__(cls) -> inspect.Signature:
        return utils.merge_signatures([
            inspect.signature(cls.__init__),
            inspect.signature(cls.setup)
        ])

    def __init__(self, config: Config = CurrentConfig, **kwargs: Any) -> None:
        self.config = config
        self.setup(**kwargs)

    def setup(self, **kwargs: Any) -> None:
        pass

    async def revoke_hashed(self, token: str) -> None:
        raise NotImplementedError

    @functools.singledispatchmethod
    async def revoke(self, token: Any) -> None:
        raise NotImplementedError

    @revoke.register
    async def _(self, token: str) -> None:
        return await self.revoke_hashed(token)