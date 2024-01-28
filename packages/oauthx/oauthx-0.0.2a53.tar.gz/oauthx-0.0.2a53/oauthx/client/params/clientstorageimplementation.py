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


__all__: list[str] = ['ClientStorageImplementation']


def ClientStorageImplementation(cls: Any) -> Any:
    def f(request: fastapi.Request, impl: cls = fastapi.Depends(cls)):
        setattr(request.state, 'oauth_client_storage', impl)
        return impl
    return fastapi.Depends(f)