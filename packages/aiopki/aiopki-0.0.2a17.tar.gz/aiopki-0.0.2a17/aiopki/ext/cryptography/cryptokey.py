# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import aiopki
from aiopki import CryptoKeyVersion
from aiopki.types import EncryptionResult, IAlgorithm, Plaintext


class LocalKey(aiopki.VersionedCryptoKey):

    async def discover(self) -> None:
        for k in self.versions:
            self._index[k.thumbprint] = k

    async def decrypt(
        self,
        version: CryptoKeyVersion,
        ct: EncryptionResult,
        algorithm: IAlgorithm
    ) -> Plaintext:
        assert version.key is not None
        return await version.key.decrypt(ct, algorithm)

    async def encrypt(
        self,
        version: CryptoKeyVersion,
        pt: Plaintext,
        algorithm: IAlgorithm
    ) -> EncryptionResult:
        assert version.key is not None
        return await version.key.encrypt(pt, algorithm)

    async def sign(
        self,
        version: CryptoKeyVersion,
        message: bytes,
        algorithm: IAlgorithm
    ) -> bytes:
        assert version.key is not None
        return await version.key.sign(message, algorithm)

    async def verify(
        self,
        version: CryptoKeyVersion,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm
    ) -> bool:
        assert version.key is not None
        return await version.key.verify(signature, message, algorithm)