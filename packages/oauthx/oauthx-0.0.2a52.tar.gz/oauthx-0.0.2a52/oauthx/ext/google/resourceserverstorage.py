# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import TypeVar

from canonical import ResourceIdentifier

from oauthx.lib.types import AccessTokenHash
from oauthx.types import IStorage
from oauthx.types import Masked
from oauthx.resource import TokenSubject
from oauthx.resource import IResourceServerStorage
from .datastorestorage import DatastoreStorage


T = TypeVar('T')


class ResourceServerStorage(DatastoreStorage, IStorage, IResourceServerStorage):

    async def get(self, key: ResourceIdentifier[Any, T]) -> T | None:
        raise NotImplementedError

    async def get_token_subject(self, at_hash: AccessTokenHash) -> TokenSubject | None:
        return await self.get_model_by_key(TokenSubject, str(at_hash))

    async def mask(self, obj: Any) -> Masked:
        raise NotImplementedError

    async def persist(self, object: Any) -> None:
        await self.put(object, object.pk)