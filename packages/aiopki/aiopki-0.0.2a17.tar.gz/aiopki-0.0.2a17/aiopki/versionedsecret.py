# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Literal

import pydantic


class VersionedSecret(pydantic.BaseModel):
    _discovered: bool = pydantic.PrivateAttr(default=False)
    backend: str
    name: str
    default_version: Literal['__default__'] | str = '__default__'
    annotations: dict[str, int | str] = {}

    async def discover(self) -> None:
        raise NotImplementedError

    def has_default(self) -> bool:
        return self.default_version != '__default__'

    def is_discovered(self) -> bool:
        return self._discovered

    async def default(self) -> Any:
        raise NotImplementedError

    async def _discover(self):
        if not self.is_discovered():
            await self.discover()
            self._discovered = True
        return self

    def __await__(self):
        return self._discover().__await__()