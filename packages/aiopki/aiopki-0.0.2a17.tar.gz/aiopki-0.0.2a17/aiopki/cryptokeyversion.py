# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from aiopki.lib import JSONWebKey
from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import Plaintext
from .algorithms import get as algorithm


class CryptoKeyVersion(pydantic.BaseModel):
    name: str
    alg: str
    enabled: bool
    thumbprint: str
    public: JSONWebKey | None = None
    key: JSONWebKey | None = None

    @property
    def kid(self) -> str:
        t = self.thumbprint
        if self.public and self.public.kid:
            t = self.public.kid
        return t

    def can_decrypt(self) -> bool:
        return self.default_algorithm().can_encrypt()

    def can_encrypt(self) -> bool:
        return self.default_algorithm().can_encrypt()

    def can_sign(self) -> bool:
        return self.default_algorithm().can_sign()

    def can_use(self, algorithm: IAlgorithm) -> bool:
        return self.alg == algorithm.name

    def default_algorithm(self) -> IAlgorithm:
        return algorithm(self.alg)

    async def encrypt(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm
    ) -> EncryptionResult:
        if self.public is None:
            raise NotImplementedError("Can only encrypt with asymmetric encryption.")
        return await self.public.encrypt(pt, algorithm=algorithm)

    def is_asymmetric(self) -> bool:
        return self.public is not None

    def process_signature(self, signature: bytes) -> bytes:
        if self.public is not None:
            signature = self.public.process_signature(signature)
        return signature
