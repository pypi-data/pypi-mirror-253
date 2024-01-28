# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import urllib.parse
from typing import Annotated
from typing import TypeAlias

import fastapi


__all__: list[str] = ['NextURL']


def is_allowed(request: fastapi.Request, url: str | None) -> bool:
    try:
        p = urllib.parse.urlparse(url)
        return all([
            p.scheme == request.url.scheme,
            p.netloc == request.url.netloc
        ])
    except Exception:
        return False

def get(
    request: fastapi.Request,
    next_url: str | None = fastapi.Query(
        default=None,
        alias='n',
        title="Next URL"
    ),
) -> str | None:
    if not is_allowed(request, next_url):
        raise NotImplementedError
    return next_url


NextURL: TypeAlias = Annotated[str | None, fastapi.Depends(get)]