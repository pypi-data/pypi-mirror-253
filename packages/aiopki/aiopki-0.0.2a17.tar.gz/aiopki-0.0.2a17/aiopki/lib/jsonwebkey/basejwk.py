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
from canonical import UnixTimestamp

import aiopki
from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import Plaintext


KeyOp = Literal['sign', 'verify', 'encrypt', 'decrypt', 'wrapKey', 'unwrapKey', 'deriveKey', 'deriveBits']
KeyUse = Literal['enc', 'sig']


class BaseJWK(pydantic.BaseModel):
    alg: str | None = None
    crv: str | None = None
    exp: UnixTimestamp | None = None
    iat: UnixTimestamp | None = None
    key_ops: list[KeyOp] | None = None
    kid: str | None = None
    nbf: UnixTimestamp | None = None
    use: KeyUse | None = None

    @property
    def thumbprint(self) -> str:
        raise NotImplementedError

    @pydantic.model_validator(mode='before')
    def preprocess(cls, values: dict[str, Any] | Any) -> dict[str, Any]:
        key = values.get('key', None)
        if key is not None:
            try:
                values.update(cls.preprocess_key(key), **values)
            except NotImplementedError:
                pass
        return values

    @classmethod
    def preprocess_key(cls, key: Any, **values: Any) -> dict[str, Any]:
        raise NotImplementedError

    def can_decrypt(self) -> bool:
        return any([
            self.use == 'enc',
            self.key_ops and 'decrypt' in self.key_ops,
            self.key_ops and 'unwrapKey' in self.key_ops,
        ])

    def can_encrypt(self) -> bool:
        return any([
            self.use == 'enc',
            self.key_ops and 'encrypt' in self.key_ops,
            self.key_ops and 'wrapKey' in self.key_ops,
        ])

    def can_use(self, algorithm: IAlgorithm) -> bool:
        raise NotImplementedError

    def default_algorithm(self) -> IAlgorithm:
        raise NotImplementedError

    def encrypt_sync(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm | None = None
    ) -> EncryptionResult:
        raise NotImplementedError

    def get_algorithm(self) -> IAlgorithm:
        if not self.alg:
            raise NotImplementedError
        return aiopki.algorithms.get(self.alg)

    def get_thumbprint(self) -> str:
        return self.thumbprint

    def is_public(self) -> bool:
        raise NotImplementedError

    def process_signature(self, signature: bytes) -> bytes:
        return signature

    def to_bytes(self) -> bytes:
        raise NotImplementedError

    async def decrypt(
        self,
        ct: EncryptionResult,
        algorithm: IAlgorithm | None = None
    ) -> Plaintext:
        raise NotImplementedError

    async def encrypt(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm | None = None
    ) -> EncryptionResult:
        raise NotImplementedError

    async def sign(
        self,
        message: bytes,
        algorithm: IAlgorithm,
    ) -> bytes:
        raise NotImplementedError

    async def verify(
        self,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm,
        using: str | None = None
    ) -> bool:
        raise NotImplementedError

    def __bytes__(self) -> bytes:
        return self.to_bytes()