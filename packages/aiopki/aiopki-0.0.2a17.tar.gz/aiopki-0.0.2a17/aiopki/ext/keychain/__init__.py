# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
from typing import Any

from aiopki import BaseCryptoKey
from aiopki import CryptoKeyType
from aiopki import CryptoKeyVersion
from aiopki.lib import JSONWebKey
from aiopki.lib import JSONWebKeySet
from aiopki.types import IAlgorithm
from aiopki.types import ICryptoKey


__all__: list[str] = [
    'Keychain'
]


class Keychain(BaseCryptoKey):
    keys: list[CryptoKeyType] = []
    _default: str | None = None
    _discovered: bool = False
    _index: dict[str, CryptoKeyType] = {}
    _trust: dict[str, CryptoKeyVersion] = {}

    @property
    def crv(self) -> str:
        # TODO: remove this attribute
        return self.default().crv # type: ignore

    def as_jwks(self) -> JSONWebKeySet:
        keys: list[JSONWebKey] = []
        for _, obj in self._trust.items():
            if not obj.is_asymmetric() or obj.public is None:
                continue
            keys.append(obj.public)
        return JSONWebKeySet.model_validate({'keys': keys})

    def model_post_init(self, _: Any) -> None:
        self._index = {}
        self._trust = {}

    def can_use(self, algorithm: IAlgorithm) -> bool:
        return True

    def default(self) -> ICryptoKey:
        assert self._default
        return self._index[self._default] # type: ignore

    def default_algorithm(self) -> IAlgorithm:
        return self.default().default_algorithm()

    def get(self, using: str) -> ICryptoKey:
        return self._index[using] # type: ignore

    def get_thumbprint(self) -> str:
        return self.default().get_thumbprint()

    async def discover(self):
        if not self._discovered:
            await asyncio.gather(*map(asyncio.ensure_future, self.keys))
            self._default = self.keys[0].thumbprint
            for key in self.keys:
                self._index[key.thumbprint] = key
                await key.trust(self)
        self._discovered = True
        return self

    async def trust(self, key: CryptoKeyVersion) -> None:
        if key.public is None:
            return
        self._trust[key.thumbprint] = key

    async def sign(
        self,
        message: bytes,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> bytes:
        key = self.get(using) if using else self.default()
        return await key.sign(message, algorithm)

    async def verify(
        self,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> bool:
        if using not in self._trust:
            raise NotImplementedError(using, list(self._trust))
        k = self._trust[using]
        assert k.public
        return await k.public.verify(signature, message, algorithm)