# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Protocol

from .ialgorithm import IAlgorithm
from .encryptionresult import EncryptionResult
from .plaintext import Plaintext


class IDecrypter(Protocol):

    def can_decrypt(self) -> bool: ...

    def can_use(self, algorithm: IAlgorithm) -> bool:
        ...

    async def decrypt(
        self,
        ct: EncryptionResult,
        algorithm: IAlgorithm | None = None
    ) -> Plaintext:
        ...