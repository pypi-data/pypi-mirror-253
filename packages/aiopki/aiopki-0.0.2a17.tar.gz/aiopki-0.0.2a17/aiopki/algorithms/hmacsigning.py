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


class HMACSigning:
    __module__: str = 'aiopki.algorithms'
    name: str

    @property
    def digestmod(self) -> str:
        return self._digalg

    def __init__(self, digalg: str):
        self._digalg = digalg

    def can_encrypt(self) -> bool:
        return False

    def can_sign(self) -> bool:
        return True

    def get_curve_name(self) -> str | None:
        return None

    def get_digest_algorithm(self) -> Any:
        raise NotImplementedError

    def get_digest_name(self) -> str:
        return self._digalg

    def get_initialization_vector(self, iv: bytes | None = None, tag: bytes | None = None) -> Any:
        raise NotImplementedError

    def get_padding(self) -> Any:
        raise NotImplementedError

    def digest(self, value: bytes) -> bytes:
        return hashlib.new(self._digalg).digest()

    def supports_aad(self) -> bool:
        raise NotImplementedError