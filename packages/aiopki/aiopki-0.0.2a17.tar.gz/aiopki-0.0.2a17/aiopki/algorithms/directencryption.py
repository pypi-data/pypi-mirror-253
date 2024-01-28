# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from cryptography.hazmat.primitives.ciphers.modes import GCM

from .encryptionalgorithm import EncryptionAlgorithm


class DirectEncryption(EncryptionAlgorithm):
    __module__: str = 'oauthx.algorithms'

    def can_encrypt(self) -> bool:
        return True

    def can_sign(self) -> bool:
        return False

    def get_initialization_vector(self, iv: bytes | None = None, tag: bytes | None = None) -> tuple[GCM, bytes]:
        raise NotImplementedError

    def is_direct(self) -> bool:
        return True

    def supports_aad(self) -> bool:
        return False