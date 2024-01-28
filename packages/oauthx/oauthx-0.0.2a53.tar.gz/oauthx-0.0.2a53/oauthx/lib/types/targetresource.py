# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import httpx
from pydantic_core import CoreSchema
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from pydantic import GetJsonSchemaHandler

from oauthx.lib.exceptions import InvalidTarget


__all__: list[str] = [
    'TargetResource'
]


class TargetResource:
    __module__: str = 'oauthx.types'

    @classmethod
    def __get_pydantic_core_schema__(cls, *_: Any) -> CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(
                serialization=core_schema.plain_serializer_function_ser_schema(str)
            ),
            python_schema=core_schema.union_schema([
                core_schema.chain_schema([
                    core_schema.is_instance_schema(str),
                    core_schema.no_info_plain_validator_function(cls)
                ]),
                core_schema.is_instance_schema(cls)
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

    def __init__(self, url: str):
        self.url = httpx.URL(url)
        if not self.url.is_absolute_url:
            raise InvalidTarget("The target audience must be an absolute URL.")

    def __str__(self) -> str:
        return str(self.url)

    def __repr__(self) -> str:
        return f'<TargetResource: {str(self)}>'