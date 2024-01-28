# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os
from typing import Annotated
from typing import TypeAlias

import fastapi
from aiopki.utils import b64decode


__all__: list[str] = ['TelegramToken']


def get() -> bytes:
    return b64decode(os.environ['TELEGRAM_LOGIN_TOKEN'])


TelegramToken: TypeAlias = Annotated[bytes, fastapi.Depends(get)]