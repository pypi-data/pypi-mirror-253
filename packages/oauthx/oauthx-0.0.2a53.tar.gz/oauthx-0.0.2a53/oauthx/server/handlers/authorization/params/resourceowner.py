# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Annotated
from typing import TypeAlias

import fastapi

from oauthx.server import models
from oauthx.server.params import CurrentSubject
from oauthx.server.params import Storage
from oauthx.server.protocols import IResourceOwner
from .client import Client


__all__: list[str] = [
    'ResourceOwner'
]


async def get(
    storage: Storage,
    client: Client,
    subject: CurrentSubject,
) -> IResourceOwner | None:
    if subject is None:
        return None
    owner = await storage.get(models.ResourceOwnerKey(client.id, str(subject.get_primary_key())))
    if owner is None:
        owner = models.ResourceOwner.model_validate({
            'client_id': str(client.id), # type: ignore
            'sub': subject.get_primary_key(),
            'sector_identifier': client.get_sector_identifier()
        })
        await storage.persist(owner)
        owner.attach(storage)
    return owner # type: ignore


ResourceOwner: TypeAlias = Annotated[IResourceOwner | None, fastapi.Depends(get)]