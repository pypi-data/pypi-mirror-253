# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

from canonical import ResourceIdentifier
from pydantic_core import CoreSchema
from pydantic_core import core_schema
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue


__all__: list[str] = [
    'MaskedPrincipal'
]


class MaskedPrincipal(ResourceIdentifier[str, Any]):
    __module__: str = 'oauthx.types'

    @classmethod
    def __get_pydantic_core_schema__(cls, *_: Any) -> CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(max_length=128),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(cls),
                core_schema.chain_schema([
                    core_schema.is_instance_schema(str),
                    core_schema.no_info_plain_validator_function(lambda x: cls(x))
                ])
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

    def __init__(self, masked: str):
        self._masked= masked

    def __repr__(self) -> str:
        return f'<MaskedPrincipal: {str(self)}>'

    def __str__(self) -> str:
        return self._masked

    def __hash__(self) -> int:
        return hash(self._masked)

    def __eq__(self, key: object) -> bool:
        return all([
            isinstance(key, type(self)),
            hash(self) == hash(key)
        ])