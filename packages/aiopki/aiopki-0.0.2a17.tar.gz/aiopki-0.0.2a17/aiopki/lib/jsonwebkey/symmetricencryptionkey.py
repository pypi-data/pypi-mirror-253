# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import hashlib
from typing import Any
from typing import Literal

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES

import aiopki
from aiopki.algorithms import AESEncryption
from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import Plaintext
from aiopki.utils import b64decode
from aiopki.utils import b64encode
from .basejwk import BaseJWK


class SymmetricEncryptionKey(BaseJWK):
    k: str
    alg: Literal['dir'] # type: ignore
    kty: Literal['oct']
    use: Literal['enc'] | None = 'enc' # type: ignore
    key_ops: list[Literal['encrypt', 'decrypt']] = ['encrypt', 'decrypt'] # type: ignore

    @property
    def public(self) -> None:
        return None

    @property
    def thumbprint(self) -> str:
        message = self.model_dump_json(include={'k', 'kty'})
        return b64encode(hashlib.sha256(str.encode(message)).digest(), encoder=bytes.decode)

    def can_use(self, algorithm: IAlgorithm) -> bool:
        return all([
            isinstance(algorithm, AESEncryption),
            len(self._key) == algorithm.length(),
        ])

    def default_algorithm(self) -> IAlgorithm:
        assert self.use is not None
        algorithm: IAlgorithm = aiopki.algorithms.get('notimplemented')
        if self.use == 'enc':
            algorithm = aiopki.algorithms.get('A256GCM')
        return algorithm

    def encrypt_sync(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm | None = None
    ) -> EncryptionResult:
        if isinstance(pt, bytes):
            pt = Plaintext(pt=pt)
        algorithm = algorithm or self.default_algorithm()
        mode, iv = algorithm.get_initialization_vector()
        cipher = Cipher(AES(self._key), mode)
        encrypter = cipher.encryptor()
        if algorithm.supports_aad():
            encrypter.authenticate_additional_data(pt.aad or b'')
        ct = encrypter.update(bytes(pt)) + encrypter.finalize()
        return EncryptionResult.model_validate({
            'aad': pt.aad or b'',
            'alg': algorithm.name,
            'kid': self.kid,
            'ct': ct,
            'iv': iv,
            'tag': encrypter.tag
        })

    def model_post_init(self, *args: Any, **kwargs: Any) -> None:
        self._key = b64decode(self.k)

    def to_bytes(self) -> bytes:
        return self._key

    async def decrypt(
        self,
        ct: EncryptionResult,
        algorithm: IAlgorithm | None = None
    ) -> Plaintext:
        assert ct.root.tag is not None
        algorithm = algorithm or self.default_algorithm()
        mode, _ = algorithm.get_initialization_vector(ct.root.iv, ct.root.tag)
        cipher = Cipher(AES(self._key), mode)
        decrypter = cipher.decryptor()
        if algorithm.supports_aad():
            decrypter.authenticate_additional_data(ct.aad)
        return Plaintext.model_validate({
            'pt': decrypter.update(bytes(ct)) + decrypter.finalize(),
            'aad': ct.aad
        })

    async def encrypt(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm | None = None
    ) -> EncryptionResult:
        return self.encrypt_sync(pt, algorithm)

    async def sign( # type: ignore
        self,
        message: bytes,
        algorithm: IAlgorithm,
    ) -> bytes:
        raise NotImplementedError

    async def verify( # type: ignore
        self,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm,
        using: str | None = None
    ) -> bool:
        raise NotImplementedError