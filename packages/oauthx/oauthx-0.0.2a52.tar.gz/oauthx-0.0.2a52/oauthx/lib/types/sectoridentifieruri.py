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
from pydantic.json_schema import JsonSchemaValue
from pydantic import GetJsonSchemaHandler


__all__: list[str] = [
    'SectorIdentifierURI'
]


class SectorIdentifierURI(str):
    _sector: str

    @classmethod
    def __get_pydantic_core_schema__(cls, *_: Any) -> CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.chain_schema([
                core_schema.is_instance_schema(str),
                core_schema.no_info_plain_validator_function(cls),
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(str),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _: CoreSchema,
        handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(core_schema.str_schema())

    @property
    def sector(self) -> str:
        return self._sector

    def __new__(cls, value: str) -> 'SectorIdentifierURI':
        p = urllib.parse.urlparse(value)
        if p.scheme != 'https':
            raise ValueError("A Sector Identifier URI must use the https scheme.")
        if p.hostname is None:
            raise ValueError("A Sector Identifier URI point to a valid host.")
        self = super().__new__(cls, value)
        self._sector = p.hostname
        return self