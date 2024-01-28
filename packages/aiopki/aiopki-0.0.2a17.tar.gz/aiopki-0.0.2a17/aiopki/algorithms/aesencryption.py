# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import secrets
import os
from typing import Any
from typing import Callable
from typing import Literal
from typing import TypeVar

from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.ciphers.modes import GCM

from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import IDecrypter
from aiopki.utils import b64encode
from .encryptionalgorithm import EncryptionAlgorithm


T = TypeVar('T')


class AESEncryption(EncryptionAlgorithm):
    __module__: str = 'oauthx.algorithms'
    iv_length: int = 12
    _modes: dict[str, type[CBC | GCM]] = {
        'CBC': CBC,
        'GCM': GCM
    }

    def __init__(self, size: int, mode: Literal['CBC', 'GCM']) -> None:
        self._mode = mode
        self._size = size

    def can_encrypt(self) -> bool:
        return True

    def can_sign(self) -> bool:
        return False

    def cek(self, factory: Callable[[dict[str, Any]], T]) -> T:
        return factory({
            'kty': 'oct',
            'alg': self.name,
            'key_ops': ['wrapKey', 'unwrapKey'],
            'k': b64encode(secrets.token_bytes(self._size))
        })

    def get_initialization_vector(self, iv: bytes | None = None, tag: bytes | None = None) -> tuple[GCM, bytes]:
        Mode = self._modes[self._mode]
        iv = iv or os.urandom(self.iv_length)
        
        assert Mode == GCM
        return Mode(iv, tag=tag), iv # type: ignore

    def length(self) -> int:
        return self._size

    def supports_aad(self) -> bool:
        return self._mode == 'GCM'

    async def unwrap(
        self,
        algorithm: IAlgorithm,
        decrypter: IDecrypter,
        ct: EncryptionResult,
        factory: Callable[[dict[str, Any]], T]
    ) -> T:
        pt = await decrypter.decrypt(ct, algorithm)
        return factory({
            'kty': 'oct',
            'alg': 'dir',
            'key_ops': ['decrypt', 'encrypt'],
            'k': b64encode(bytes(pt))
        })