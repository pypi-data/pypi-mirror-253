# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import TypeVar

import pydantic

from oauthx.server.params import ContentEncryptionKey
from .basedatastorestorage import BaseDatastoreStorage
from .params import DatastoreClient


T = TypeVar('T', bound=pydantic.BaseModel)


class DatastoreStorage(BaseDatastoreStorage):

    def __init__( # type: ignore
        self,
        *,
        client: DatastoreClient, # type: ignore
        key: ContentEncryptionKey
    ) -> None:
        self.client = client
        self.key = key