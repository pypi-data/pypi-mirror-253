# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Callable
from typing import Protocol
from typing import TypeVar

from cryptography.hazmat.primitives.ciphers.modes import GCM

from .encryptionresult import EncryptionResult


T = TypeVar('T')


class IAlgorithm(Protocol):
    __module__: str = 'aiopki.types'
    name: str

    def can_encrypt(self) -> bool: ...
    def can_sign(self) -> bool: ...
    def cek(self, factory: Callable[[dict[str, Any]], T]) -> T: ...
    def get_digest_algorithm(self) -> Any: ...
    def get_padding(self) -> Any: ...

    def digest(self, value: bytes) -> bytes:
        raise NotImplementedError

    def get_curve_name(self) -> str | None:
        raise NotImplementedError

    def get_digest_name(self) -> str:
        raise NotImplementedError

    def get_initialization_vector(self, iv: bytes | None = None, tag: bytes | None = None) -> tuple[GCM, bytes]:
        raise NotImplementedError

    def is_direct(self) -> bool:
        """Return a boolean indicating if the algorithm is the ``dir``
        algorithm as defined in :rfc:`7518`.
        """
        return False

    def length(self) -> int:
        raise NotImplementedError

    def supports_aad(self) -> bool:
        raise NotImplementedError

    async def unwrap(
        self,
        algorithm: 'IAlgorithm',
        decrypter: Any,
        ct: EncryptionResult,
        factory: Callable[[dict[str, Any]], T]
    ) -> T:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f'<{type(self).__name__}: {self.name}>'