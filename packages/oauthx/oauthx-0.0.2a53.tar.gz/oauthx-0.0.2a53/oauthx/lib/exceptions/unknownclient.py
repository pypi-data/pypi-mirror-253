# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .fatalerror import FatalError


class UnknownClient(FatalError, ValueError):
    __module__: str = 'oauthx.types'

    def __init__(self, description: str):
        FatalError.__init__(
            self,
            error='invalid_client',
            error_description=description,
            allow_redirect=False
        )