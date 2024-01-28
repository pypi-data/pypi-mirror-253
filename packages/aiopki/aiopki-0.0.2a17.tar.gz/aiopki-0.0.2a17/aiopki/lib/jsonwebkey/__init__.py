# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Union

import pydantic

from aiopki.algorithms import get as get_algorithm
from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import Plaintext
from .edwardscurveprivatekey import EdwardsCurvePrivateKey
from .edwardscurvepublickey import EdwardsCurvePublicKey
from .ellipticcurveprivatekey import EllipticCurvePrivateKey
from .ellipticcurvepublickey import EllipticCurvePublicKey
from .octetsigningkey import OctetSigningKey
from .rsaprivatekey import RSAPrivateKey
from .rsapublickey import RSAPublicKey
from .symmetricencryptionkey import SymmetricEncryptionKey
from .symmetricwrappingkey import SymmetricWrappingKey


__all__: list[str] = ['JSONWebKey']

JWKType = Union[
    EdwardsCurvePrivateKey,
    EllipticCurvePrivateKey,
    SymmetricEncryptionKey,
    SymmetricWrappingKey,
    OctetSigningKey,
    RSAPrivateKey,
    EdwardsCurvePublicKey,
    EllipticCurvePublicKey,
    RSAPublicKey,
]


class JSONWebKey(pydantic.RootModel[JWKType]):

    @property
    def alg(self) -> str | None:
        return self.root.alg

    @property
    def crv(self) -> str | None:
        return self.root.crv

    @property
    def kid(self) -> str | None:
        return self.root.kid

    @property
    def key_ops(self) -> tuple[str, ...]:
        return tuple(self.root.key_ops or [])

    @property
    def kty(self) -> str:
        return self.root.kty

    @property
    def public(self) -> Union['JSONWebKey', None]:
        if self.root.public:
            return JSONWebKey.model_validate(self.root.public.model_dump())

    @property
    def thumbprint(self) -> str:
        return self.root.thumbprint

    @property
    def use(self) -> str | None:
        return self.root.use

    def can_decrypt(self) -> bool:
        return self.root.can_decrypt()

    def can_encrypt(self) -> bool:
        return self.root.can_encrypt()

    def can_use(self, algorithm: IAlgorithm) -> bool:
        return self.root.can_use(algorithm)

    def default_algorithm(self) -> IAlgorithm:
        if self.root.alg is not None:
            return get_algorithm(self.root.alg)
        if not self.root.use:
            raise ValueError(
                "Can not determine default algorithm if the `use` "
                "claim is not specified."
            )
        return self.root.default_algorithm()

    def encrypt_sync(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm | None = None
    ) -> EncryptionResult:
        return self.root.encrypt_sync(pt, algorithm)

    def is_active(self) -> bool:
        if self.root.nbf is None:
            return True
        now = datetime.datetime.now(datetime.timezone.utc).timestamp()
        return self.root.nbf <= now

    def is_available(self) -> bool:
        return not self.is_expired() and self.is_active()

    def is_expired(self) -> bool:
        if self.root.exp is None:
            return False
        now = datetime.datetime.now(datetime.timezone.utc).timestamp()
        return now >= self.root.exp

    def is_public(self) -> bool:
        return isinstance(self.root, (
            EdwardsCurvePublicKey,
            EllipticCurvePublicKey,
            RSAPublicKey,
        ))

    def process_signature(self, signature: bytes) -> bytes:
        return self.root.process_signature(signature)

    async def decrypt(
        self,
        ct: EncryptionResult,
        algorithm: IAlgorithm | None = None
    ) -> Plaintext:
        return await self.root.decrypt(ct, algorithm)

    async def encrypt(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm | None = None
    ) -> EncryptionResult:
        return await self.root.encrypt(pt, algorithm)

    async def sign(
        self,
        message: bytes,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> bytes:
        if algorithm is None:
            algorithm = self.root.get_algorithm()
        return await self.root.sign(message, algorithm) # type: ignore

    async def verify(
        self,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> bool:
        if not self.is_available():
            return False
        if using is not None and using not in {self.kid, self.thumbprint}:
            return False
        if algorithm is None:
            algorithm = self.root.get_algorithm()
        return await self.root.verify(signature, message, algorithm, using) # type: ignore

    def __bytes__(self) -> bytes:
        return bytes(self.root)