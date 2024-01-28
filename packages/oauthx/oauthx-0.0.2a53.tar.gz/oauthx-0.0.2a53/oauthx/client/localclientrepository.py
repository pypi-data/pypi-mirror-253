# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import logging
import pathlib
import re
import os
from typing import Any

import aiofiles
import jinja2
import yaml
from canonical.protocols import IRepository

from oauthx.client.models import Client


class LocalClientRepository(IRepository[Client]):
    base_dir: pathlib.Path = pathlib.Path('etc/upstream.d')
    logger: logging.Logger = logging.getLogger('uvicorn')
    pattern: re.Pattern[str] = re.compile('^[a-zA-Z0-9]([a-zA-Z0-9.]+)[a-zA-Z0-9]$')

    def construct_path(self, client_id: str) -> pathlib.Path | None:
        if not self.pattern.match(str(client_id) or ''):
            return None
        return self.base_dir.joinpath(f'{client_id}.yaml')

    async def delete(self, instance: Client | int | str) -> None:
        raise NotImplementedError

    async def exists(self, pk: str) -> bool:
        path = self.construct_path(pk)
        return path is not None and path.exists()

    async def get(self, pk: Any) -> Client | None:
        if not await self.exists(pk):
            return
        return await self.open(pk)

    async def one(self, pk: Any) -> Client:
        return await self.open(pk)

    async def open(self, pk: str) -> Client:
        path = self.construct_path(pk)
        if path is None or not path.exists():
            raise self.DoesNotExist
        async with aiofiles.open(path) as f: # type: ignore
            t = jinja2.Template(
                source=await f.read(), # type: ignore
                undefined=jinja2.StrictUndefined,
                variable_start_string='${',
                variable_end_string='}'
            )
            c = {'env': dict(os.environ)}
            params = yaml.safe_load(t.render(c)) # type: ignore
        obj = Client.model_validate(params)
        return obj.attach(self)

    async def persist(self, instance: Client) -> None:
        raise NotImplementedError