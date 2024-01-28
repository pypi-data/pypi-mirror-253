# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import logging
import re
import pathlib

import aiofiles
import yaml

from .models import Client


class LocalClientStorage:
    __module__: str = 'oauthx.server'
    base_dir: pathlib.Path = pathlib.Path('etc/clients.d')
    logger: logging.Logger = logging.getLogger('uvicorn')
    pattern: re.Pattern[str] = re.compile('^[a-zA-Z0-9]([a-zA-Z0-9.]+)[a-zA-Z0-9]$')

    async def get(self, client_id: str) -> Client | None:
        if not self.pattern.match(str(client_id) or ''):
            return None
        path = self.base_dir.joinpath(f'{client_id}.yaml')
        if not path.exists():
            self.logger.debug(
                "Client does not exist in local configuration (client: %s)",
                client_id
            )
            return None
        try:
            async with aiofiles.open(path) as f:
                params = yaml.safe_load(await f.read())
            return Client.model_validate({**params, 'client_id': client_id})
        except Exception as e:
            self.logger.critical(
                "Caught fatal %s while retrieving client from "
                "local configuration  (client: %s)",
                type(e).__name__, client_id
            )
            return None
        