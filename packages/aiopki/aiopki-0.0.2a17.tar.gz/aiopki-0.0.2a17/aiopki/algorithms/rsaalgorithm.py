# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

from cryptography.hazmat.primitives.hashes import Hash
from cryptography.hazmat.primitives.hashes import HashAlgorithm
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hashes import SHA384
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.hazmat.primitives.asymmetric.padding import AsymmetricPadding
from cryptography.hazmat.primitives.asymmetric.padding import MGF1
from cryptography.hazmat.primitives.asymmetric.padding import OAEP
from cryptography.hazmat.primitives.asymmetric.padding import PSS
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

from ..types import IAlgorithm


DIGEST_ALGORITHMS: dict[str, type[HashAlgorithm]] = {
    'sha1'  : SHA1,
    'sha256': SHA256,
    'sha384': SHA384,
    'sha512': SHA512,
}

PADDING_ALGORITHMS: dict[str, type[OAEP|PKCS1v15|PSS]] = {
    'EME-OAEP': OAEP,
    'RSASSA-PKCS1-v1_5': PKCS1v15
}


class RSAAlgorithm(IAlgorithm):
    __module__: str = 'aiopki.algorithms'
    name: str

    def __init__(self, digalg: str, padding: str):
        self._digalg = DIGEST_ALGORITHMS[digalg]
        self._padding = PADDING_ALGORITHMS[padding]
        self._padding_name = padding

    def can_encrypt(self) -> bool:
        return False

    def can_sign(self) -> bool:
        return False

    def digest(self, value: bytes) -> bytes:
        h = Hash(self._digalg())
        h.update(value)
        return h.finalize()

    def get_curve_name(self) -> str | None:
        return None

    def get_digest_algorithm(self) -> HashAlgorithm:
        return self._digalg()
    
    def get_padding(self) -> AsymmetricPadding:
        params = self.get_padding_params(self._padding_name)
        if self._padding == PSS:
            raise NotImplementedError
        return self._padding(**params) # type: ignore

    def get_padding_params(self, padding: str) -> dict[str, Any]:
        params: dict[str, Any] = {}
        match padding:
            case 'EME-OAEP':
                params.update({
                    'mgf': MGF1(self.get_digest_algorithm()),
                    'algorithm': self.get_digest_algorithm(),
                    'label': None
                })
            case _:
                pass
        return params