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
from typing import TypeVar

from pydantic_core import CoreSchema
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from pydantic import GetCoreSchemaHandler
from pydantic import GetJsonSchemaHandler


T = TypeVar('T', bound='RequestURI')


class RequestURI(str):
    __module__: str = 'headless.ext.oidc.types'
    _parsed: urllib.parse.ParseResult
    _request_id: str | None

    @property
    def id(self) -> str | None:
        return self._request_id

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        core_schema: CoreSchema,
        handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        json_schema = handler(core_schema)
        json_schema = handler.resolve_ref_schema(json_schema)
        return json_schema

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _: Any,
        handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(str))

    def __new__(cls, v: str):
        if not v:
            raise ValueError('The request_uri parameter can not be empty.')
        if len(v) > 2048:
            raise ValueError('Provided value is too long to be a URI.')
        p = urllib.parse.urlparse(v)
        if p.scheme in {'http', 'https'} and not p.netloc:
            raise ValueError('Provided value is not a valid URI.')
        if not p.scheme:
            raise ValueError(f"The request_uri parameter must be a valid URN.")
        if p.scheme not in {'urn', 'https'}:
            raise ValueError(f'The request_uri parameter uses an unknown scheme.')
        instance = super().__new__(cls, urllib.parse.urlunparse(p))
        instance._parsed = urllib.parse.urlparse(v)
        instance._request_id = None
        if instance._parsed.scheme == 'urn':
            instance._request_id = str.rsplit(instance, ':', 1)[-1]
        return instance
    
    def is_external(self) -> bool:
        return self._parsed.scheme in {'http', 'https'}

    def __repr__(self) -> str: # pragma: no cover
        return f'RequestURI({self})'