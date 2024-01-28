# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Annotated
from typing import Any
from typing import TypeAlias

import fastapi
from aiopki.ext.jose import OIDCToken

from .contentencryptionkey import ContentEncryptionKey
from .currentsubject import CurrentSubject
from .objectfactory import ObjectFactory


__all__: list[str] = [
    'RequestUserInfo',
    'RequestUserInfoDependency',
]


async def get(
    factory: ObjectFactory,
    subject: CurrentSubject,
    cek: ContentEncryptionKey,
) -> OIDCToken | None:
    if subject is None or not subject.is_authenticated():
        return None
    await subject.decrypt_keys(cek)
    return await factory.userinfo(
        subject=subject,
        scope={'profile', 'email'},
        aud='self'
    )


RequestUserInfoDependency: Any = fastapi.Depends(get)

RequestUserInfo: TypeAlias  = Annotated[None, RequestUserInfoDependency]