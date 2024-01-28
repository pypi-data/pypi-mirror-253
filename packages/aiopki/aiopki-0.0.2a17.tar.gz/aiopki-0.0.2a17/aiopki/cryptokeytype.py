# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .lib import JSONWebKeySet
from .types import EncryptionResult
from .types import IAlgorithm
from .types import ITrustStore
from .types import Plaintext
from .resource import Resource
from .versionedcryptokey import VersionedCryptoKey


__all__: list[str] = [
    'CryptoKeyType'
]


class CryptoKeyType(Resource[VersionedCryptoKey]):
    __module__: str = 'aiopki'
    model = VersionedCryptoKey

    @property
    def crv(self) -> str | None:
        return None

    @property
    def thumbprint(self) -> str:
        return self.impl.thumbprint

    def as_jwks(self) -> JSONWebKeySet:
        return self.impl.as_jwks()

    def can_decrypt(self) -> bool:
        return self.impl.can_decrypt()

    def can_use(self, algorithm: IAlgorithm) -> bool:
        return self.impl.can_use(algorithm)

    def default_algorithm(self) -> IAlgorithm:
        return self.impl.default_algorithm()

    def get_encryption_algorithms(self) -> set[str]:
        return {x.alg for x in self.impl.versions if x.can_encrypt()}

    def get_signing_algorithms(self) -> set[str]:
        return {x.alg for x in self.impl.versions if x.can_sign()}

    async def discover(self):
        if not self.ready:
            await self.impl
        return self

    async def decrypt(
        self,
        ct: EncryptionResult,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> Plaintext:
        version = self.impl.get(using)
        algorithm = algorithm or version.default_algorithm()
        if not version.can_use(algorithm):
            raise ValueError(f"Algorithm {algorithm} can not be used with this key.")
        return await self.impl.decrypt(
            version=version,
            ct=ct,
            algorithm=algorithm
        )

    async def encrypt(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> EncryptionResult:
        version = self.impl.get(using)
        algorithm = algorithm or version.default_algorithm()
        if not version.can_use(algorithm):
            raise ValueError(f"Algorithm {algorithm} can not be used with this key.")
        if not isinstance(pt, Plaintext):
            pt = Plaintext(pt=pt)
        if version.is_asymmetric():
            return await version.encrypt(pt, algorithm)
        return await self.impl.encrypt(
            version=version,
            pt=pt,
            algorithm=algorithm
        )

    async def sign(
        self,
        message: bytes,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> bytes:
        await self.impl
        version = self.impl.get(using)
        return await self.impl.sign(
            version=version,
            message=message,
            algorithm=algorithm or version.default_algorithm()
        )

    async def verify(
        self,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> bool:
        await self.impl
        if using and not self.impl.has(using):
            return False
        version = self.impl.get(using)
        return await self.impl.verify(
            version=version,
            signature=signature,
            message=message,
            algorithm=algorithm or version.default_algorithm(),
        )

    async def trust(self, truststore: ITrustStore) -> None:
        for version in self.impl.versions:
            await truststore.trust(version)

    def __await__(self):
        return self.discover().__await__()

    def __or__(self, key: 'CryptoKeyType') -> JSONWebKeySet:
        s1 = self.as_jwks()
        s2 = key.as_jwks()
        return JSONWebKeySet(keys=[*s1.keys, *s2.keys])