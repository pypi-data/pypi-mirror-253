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
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue


__all__: list[str] = [
    'OIDCIssuerIdentifier'
]


class OIDCIssuerIdentifier:
    __module__: str = 'oauthx.types'

    @classmethod
    def __get_pydantic_core_schema__(cls, *_: Any) -> CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(max_length=128),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(cls),
                core_schema.chain_schema([
                    core_schema.is_instance_schema(str),
                    core_schema.no_info_plain_validator_function(urllib.parse.urlparse),
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

    def __init__(self, issuer: str | urllib.parse.ParseResult):
        if isinstance(issuer, str):
            issuer = urllib.parse.urlparse(issuer)
        self._issuer = issuer

    def __hash__(self) -> int:
        return hash(self._issuer)

    def __repr__(self) -> str:
        return f'<OIDCIssuerIdentifier: {str(self)}>'

    def __eq__(self, __value: object) -> bool:
        return all([
            isinstance(__value, type(self)),
            str(__value) == str(self)
        ])

    def __str__(self) -> str:
        return urllib.parse.urlunparse(self._issuer)