# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Generator
from typing import Generic
from typing import TypeVar

from .resource import Resource
from .versionedsecret import VersionedSecret


__all__: list[str] = [
    'Secret'
]


T = TypeVar('T')


class Secret(Resource[VersionedSecret], Generic[T]):
    __module__: str = 'aiopki'
    model = VersionedSecret

    async def decode(self, value: Any) -> T:
        raise NotImplementedError

    async def discover(self) -> T:
        if not self.ready:
            await self.impl
        return await self.decode(await self.impl.default())

    def __await__(self) -> Generator[None, None, T]:
        return super().__await__()