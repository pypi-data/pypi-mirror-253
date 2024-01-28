# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import hashlib
import hmac
from typing import Any
from typing import Literal

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES

import aiopki
from aiopki.algorithms import HMACSigning
from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import Plaintext
from aiopki.utils import b64decode
from aiopki.utils import b64encode
from .basejwk import BaseJWK


class OctetSigningKey(BaseJWK):
    k: str
    kty: Literal['oct']
    use: Literal['sig'] | None = None # type: ignore

    @property
    def public(self) -> None:
        return None

    @property
    def thumbprint(self) -> str:
        message = self.model_dump_json(include={'k', 'kty'})
        return b64encode(hashlib.sha256(str.encode(message)).digest(), encoder=bytes.decode)

    def can_use(self, algorithm: IAlgorithm) -> bool:
        return isinstance(algorithm, HMACSigning)

    def default_algorithm(self) -> IAlgorithm:
        return aiopki.algorithms.get(self.alg or 'HS256')

    def model_post_init(self, *args: Any, **kwargs: Any) -> None:
        self._key = b64decode(self.k)
        if self.key_ops:
            invalid_ops: set[Any] = set(map(str, self.key_ops)) - {'sign', 'verify'}
            if invalid_ops:
                raise ValueError(
                    f'Invalid key ops for {type(self).__name__}: '
                    f'{str.join(",", sorted(invalid_ops))}'
                )

    async def decrypt(
        self,
        ct: EncryptionResult,
        algorithm: IAlgorithm | None = None
    ) -> Plaintext:
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
        if isinstance(pt, bytes):
            pt = Plaintext(pt=pt)
        algorithm = algorithm or self.default_algorithm()
        mode, iv = algorithm.get_initialization_vector()
        cipher = Cipher(AES(self._key), mode)
        encrypter = cipher.encryptor()
        if algorithm.supports_aad():
            encrypter.authenticate_additional_data(b'') # type: ignore
        ct = encrypter.update(bytes(pt)) + encrypter.finalize()
        return EncryptionResult.model_validate({
            'aad': b'',
            'alg': algorithm.name,
            'kid': self.kid,
            'ct': ct,
            'iv': iv,
            'tag': encrypter.tag
        })

    async def sign( # type: ignore
        self,
        message: bytes,
        algorithm: HMACSigning,
    ) -> bytes:
        return hmac.digest(self._key, message, algorithm.digestmod)

    async def verify( # type: ignore
        self,
        signature: bytes,
        message: bytes,
        algorithm: HMACSigning,
        using: str | None = None
    ) -> bool:
        h = hmac.new(self._key, message, algorithm.digestmod)
        return hmac.compare_digest(h.digest(), signature)