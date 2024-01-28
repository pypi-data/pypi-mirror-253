# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from canonical import ResourceIdentifier

from oauthx.lib.protocols import IClient


class ClientKey(ResourceIdentifier[int | str, IClient]):
    __module__: str = 'oauthx.types'
    
    def __init__(self, client_id: str):
        self.client_id = client_id

    def __str__(self) -> str:
        return self.client_id

    def __hash__(self) -> int:
        return hash(self.client_id)

    def __repr__(self) -> str:
        return f'<ClientKey: {str(self)}>'
    
    def __eq__(self, key: object) -> bool:
        return all([
            isinstance(key, type(self)),
            hash(self) == hash(key)
        ])