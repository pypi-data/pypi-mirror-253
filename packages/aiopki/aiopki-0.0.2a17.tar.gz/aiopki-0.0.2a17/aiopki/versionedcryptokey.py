# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

import pydantic

from aiopki.lib import JSONWebKey
from aiopki.lib import JSONWebKeySet
from aiopki.types import IAlgorithm
from .cryptokeyversion import CryptoKeyVersion
from .types import EncryptionResult
from .types import Plaintext


class VersionedCryptoKey(pydantic.BaseModel):
    backend: str
    name: str
    default_version: Literal['__default__'] | str = '__default__'
    annotations: dict[str, int | str] = {}
    versions: list[CryptoKeyVersion] = []
    _discovered: bool = pydantic.PrivateAttr(default=False)
    _index: dict[str, CryptoKeyVersion] = pydantic.PrivateAttr(default_factory=dict)

    @property
    def latest(self) -> CryptoKeyVersion:
        return self._index[self.default_version]

    @property
    def thumbprint(self) -> str:
        return self._index[self.default_version].thumbprint

    def add_version(
        self,
        name: str,
        alg: str,
        enabled: bool = True,
        thumbprint: str | None = None,
        public: JSONWebKey | None = None,
        key: JSONWebKey | None = None
    ) -> None:
        assert thumbprint is not None
        self._index[thumbprint] = version = CryptoKeyVersion.model_validate({
            'name': name,
            'alg': alg,
            'enabled': enabled,
            'thumbprint': thumbprint if not public else public.thumbprint,
            'public': public,
            'key': key
        })
        self._index[name] = version
        self.versions.append(version)

    def as_jwks(self) -> JSONWebKeySet:
        return JSONWebKeySet(keys=[x.public for x in self.versions if x.public])

    def can_decrypt(self) -> bool:
        return self.latest.can_decrypt()

    def can_use(self, algorithm: IAlgorithm) -> bool:
        return self.latest.alg == algorithm.name

    def default_algorithm(self) -> IAlgorithm:
        return self.latest.default_algorithm()

    def get(self, using: str | None) -> CryptoKeyVersion:
        if using is None:
            using = self.default_version
        return self._index[using]

    def has(self, name: str) -> bool:
        return name in self._index

    def has_default(self) -> bool:
        return self.default_version != '__default__'

    def is_discovered(self) -> bool:
        return self._discovered

    async def discover(self) -> None:
        raise NotImplementedError

    async def decrypt(
        self,
        version: CryptoKeyVersion,
        ct: EncryptionResult,
        algorithm: IAlgorithm
    ) -> Plaintext:
        raise NotImplementedError

    async def encrypt(
        self,
        version: CryptoKeyVersion,
        pt: Plaintext,
        algorithm: IAlgorithm
    ) -> EncryptionResult:
        raise NotImplementedError

    async def sign(
        self,
        version: CryptoKeyVersion,
        message: bytes,
        algorithm: IAlgorithm,
    ) -> bytes:
        raise NotImplementedError

    async def verify(
        self,
        version: CryptoKeyVersion,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm
    ) -> bool:
        raise NotImplementedError

    async def _discover(self):
        if not self.is_discovered():
            await self.discover()
            self._discovered = True
        return self

    def __await__(self):
        return self._discover().__await__()