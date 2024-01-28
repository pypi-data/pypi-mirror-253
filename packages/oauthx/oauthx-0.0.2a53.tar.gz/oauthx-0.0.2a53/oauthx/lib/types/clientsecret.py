# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import urllib.parse
from typing import Any

from pydantic_core import CoreSchema
from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue


__all__: list[str] = [
    'ClientSecret'
]


class ClientSecret(str):
    __module__: str = 'oauthx.types'

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _: Any,
        handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        
        def is_not_uri(client_secret: str):
            # TODO: this assumes that a client secret never contains a colon.
            p = urllib.parse.urlparse(client_secret)
            if p.netloc or p.scheme:
                raise ValueError("A client secret can not be an URI.")
            return client_secret

        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(max_length=128),
            python_schema=core_schema.chain_schema([
                core_schema.is_instance_schema(str),
                core_schema.no_info_plain_validator_function(is_not_uri),
                core_schema.no_info_plain_validator_function(cls)
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(str)
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _: CoreSchema,
        handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(core_schema.str_schema(max_length=128))
    
    def __await__(self):
        async def f(): return self
        return f().__await__()