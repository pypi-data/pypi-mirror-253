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
from typing import Awaitable
from typing import Generic
from typing import TypeVar

from canonical import HTTPResourceLocator
from canonical import ResourceName
from pydantic_core import CoreSchema
from pydantic_core import core_schema
from pydantic import GetJsonSchemaHandler
from pydantic import TypeAdapter
from pydantic.json_schema import JsonSchemaValue

from .backends import parse
from .types import CryptoKeySpecification


__all__: list[str] = [
    'Resource'
]


S = TypeVar('S', bound='Resource[Any]')
T = TypeVar('T', bound=Awaitable[Any])
HTTPResourceLocatorAdapter = TypeAdapter(HTTPResourceLocator)
ResourceNameAdapter = TypeAdapter(ResourceName)


class Resource(Generic[T]):
    __module__: str = 'aiopki'
    model: type[T]

    @classmethod
    def __get_pydantic_core_schema__(cls, *_: Any) -> CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(max_length=2048),
            python_schema=core_schema.union_schema([
                core_schema.chain_schema([
                    core_schema.is_instance_schema(str),
                    core_schema.union_schema([
                        core_schema.no_info_plain_validator_function(ResourceNameAdapter.validate_python),
                        core_schema.no_info_plain_validator_function(HTTPResourceLocatorAdapter.validate_python),
                        core_schema.no_info_plain_validator_function(urllib.parse.urlparse)
                    ]),
                    core_schema.no_info_plain_validator_function(cls.parse),
                ]),
                core_schema.chain_schema([
                    core_schema.dict_schema(),
                    core_schema.no_info_plain_validator_function(cls.parse)
                ]),
                core_schema.chain_schema([
                    core_schema.is_instance_schema(cls.model),
                    core_schema.no_info_plain_validator_function(cls)
                ]),
                core_schema.is_instance_schema(cls)
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(str)
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _: CoreSchema,
        handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(core_schema.str_schema())

    @classmethod
    def parse(cls: type[S], name: CryptoKeySpecification) -> S:
        obj = parse(name)
        if not isinstance(obj, cls.model):
            raise ValueError(f"Invalid type: {type(obj).__name__}")
        return cls(obj)

    def __init__(self, impl: T):
        self.impl = impl
        self.ready = False

    async def discover(self) -> Any:
        raise NotImplementedError

    def __await__(self):
        return self.discover().__await__()