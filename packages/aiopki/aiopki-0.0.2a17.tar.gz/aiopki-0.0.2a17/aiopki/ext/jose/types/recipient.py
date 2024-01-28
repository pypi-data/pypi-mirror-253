# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pydantic

import aiopki
from aiopki.algorithms import DirectEncryption
from aiopki.lib import JSONWebKey
from aiopki.types import Base64
from aiopki.types import IAlgorithm
from aiopki.types import IDecrypter
from aiopki.types import EncryptionResult
from aiopki.types import JSONObject
from aiopki.types import Plaintext

from .jweheader import JWEHeader


class Recipient(pydantic.BaseModel):
    header: JSONObject = pydantic.Field(
        default_factory=JSONObject
    )

    encrypted_key: Base64 | None = pydantic.Field(
        default=None
    )

    _claims: JWEHeader = pydantic.PrivateAttr(default_factory=dict)

    @property
    def alg(self) -> IAlgorithm:
        return aiopki.get(self._claims.alg.value)

    @property
    def enc(self) -> IAlgorithm:
        return aiopki.get(self._claims.enc.value)

    @property
    def iv(self) -> bytes | None:
        return self._claims.iv

    @property
    def kid(self) -> str | None:
        return self._claims.kid

    @property
    def tag(self) -> bytes | None:
        return self._claims.tag

    def is_direct(self) -> bool:
        return self._claims.alg.name == 'dir'

    def update_header(self, claims: dict[str, Any]):
        self._claims = JWEHeader.model_validate({**claims, **self.header})
        if self.alg.name == 'dir' and self.encrypted_key:
            raise ValueError("Direct encryption should not provide an encryption key.")
        elif self.alg.name != 'dir' and not self.encrypted_key:
            raise ValueError("Wrapped encryption must provide an encryption key.")

    def can_decrypt(self, decrypter: IDecrypter) -> bool:
        return all([
            decrypter.can_use(self.alg if not self.is_direct() else self.enc)
        ])

    async def decrypt(self, decrypter: IDecrypter, ct: EncryptionResult) -> Plaintext:
        if not isinstance(self.alg, DirectEncryption):
            decrypter = await self.unwrap(decrypter)
        return await decrypter.decrypt(
            ct=ct,
            algorithm=self.enc
        )

    async def unwrap(self, decrypter: IDecrypter) -> IDecrypter:
        return await self.enc.unwrap(
            algorithm=self.alg,
            decrypter=decrypter,
            ct=EncryptionResult.model_validate({
                'alg': self.enc.name,
                'ct': self.encrypted_key
            }),
            factory=JSONWebKey.model_validate
        )