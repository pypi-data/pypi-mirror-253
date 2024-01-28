# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Iterable
from typing import Literal
from typing import TypeVar

import pydantic
from aiopki.ext.jose import OIDCToken
from canonical import DomainName
from canonical import EmailAddress
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema
from pydantic_core import core_schema


__all__: list[str] = ['ClientACL']


T = TypeVar('T')


class ClientACL:
    __module__: str = 'oauthx.server.models'
    conditions: list['Condition']

    @classmethod
    def __get_pydantic_core_schema__(cls, *_: Any) -> CoreSchema:
        schema = core_schema.union_schema([
            core_schema.chain_schema([
                core_schema.list_schema(),
                core_schema.no_info_plain_validator_function(cls.fromiterable)
            ]),
            core_schema.chain_schema([
                core_schema.none_schema(),
                core_schema.no_info_plain_validator_function(cls.null)
            ])   
        ])
        return core_schema.json_or_python_schema(
            json_schema=schema,
            python_schema=core_schema.union_schema([
                schema,
                core_schema.is_instance_schema(cls)
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(lambda x: x.serialize())
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _: CoreSchema,
        handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(core_schema.union_schema([
            core_schema.list_schema(),
            core_schema.none_schema()
        ]))

    @classmethod
    def fromiterable(cls, v: Iterable[str]) -> 'ClientACL':
        conditions: list[Condition] = []
        for condition in v:
            kind, value = str.split(condition, ':', 1)
            conditions.append(Condition.model_validate({
                'kind': kind,
                'value': value
            }))

        return cls(conditions=conditions)

    @classmethod
    def null(cls, v: None = None) -> 'ClientACL':
        return cls(conditions=[Condition.model_validate({'kind': 'null'})])

    def __init__(
        self,
        conditions: Iterable['Condition'] | None = None
    ) -> None:
        self.conditions = list(conditions or [])

    def serialize(self) -> list[str] | None:
        return [
            str(condition) for condition in self.conditions
        ]

    def has_access(self, userinfo: OIDCToken) -> bool:
        return any([x.has_access(userinfo) for x in self.conditions])


class BaseCondition(pydantic.BaseModel):
    kind: Any
    value: Any

    def get_value(self) -> str:
        return self.value

    def has_access(self, userinfo: OIDCToken) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        return f'{self.kind}:{self.get_value()}'


class DomainCondition(BaseCondition):
    kind: Literal['domain']
    value: DomainName

    def has_access(self, userinfo: OIDCToken) -> bool:
        return userinfo.email is not None and userinfo.email.domain == self.value


class EmailCondition(BaseCondition):
    kind: Literal['email']
    value: EmailAddress

    def has_access(self, userinfo: OIDCToken) -> bool:
        return userinfo.email is not None and userinfo.email == self.value


class NullCondition(BaseCondition):
    kind: Literal['null']
    value: str = 'allUsers'

    def has_access(self, userinfo: OIDCToken) -> bool:
        return True


class Condition(pydantic.RootModel[DomainCondition | EmailCondition | NullCondition]):

    def has_access(self, userinfo: OIDCToken) -> bool:
        return self.root.has_access(userinfo)

    def __hash__(self) -> int:
        return hash((self.root.get_value(), self.root.kind))

    def __str__(self) -> str:
        return str(self.root)