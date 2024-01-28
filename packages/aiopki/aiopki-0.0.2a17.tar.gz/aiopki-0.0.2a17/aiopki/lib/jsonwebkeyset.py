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

from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import Plaintext
from .jsonwebkey import JSONWebKey


class JSONWebKeySet(pydantic.BaseModel):
    keys: list[JSONWebKey] = []
    _index: dict[str, JSONWebKey] = {}

    @property
    def crv(self) -> str | None:
        return self.keys[0].crv

    @property
    def public(self) -> 'JSONWebKeySet':
        return JSONWebKeySet.model_validate({
            'keys': filter(bool, [x.public for x in self.keys])
        })

    @property
    def thumbprint(self) -> str:
        return self.keys[0].thumbprint

    def can_decrypt(self) -> bool:
        """Return a boolean indicating if any of the keys in the
        :class:`JSONWebKeySet` can be used to encrypt.
        """
        return any([x.can_decrypt() for x in self.keys])

    def can_encrypt(self) -> bool:
        """Return a boolean indicating if any of the keys in the
        :class:`JSONWebKeySet` can be used to encrypt.
        """
        return any([x.can_encrypt() for x in self.keys])

    def can_use(self, algorithm: IAlgorithm) -> bool:
        return any([k.can_use(algorithm) for k in self.keys])

    def default(self) -> JSONWebKey:
        return self.keys[0]

    def default_algorithm(self) -> IAlgorithm:
        return self.keys[0].default_algorithm()

    def get(self, kid: str) -> JSONWebKey:
        return self._index[kid]

    def model_post_init(self, *args: Any, **kwargs: Any) -> None:
        for jwk in self.keys:
            self._index[jwk.thumbprint] = jwk
            if jwk.kid is not None:
                self._index[jwk.kid] = jwk

    async def decrypt(
        self,
        ct: EncryptionResult,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> Plaintext:
        keys = [x for x in self.keys if x.root.use == 'enc']
        if not keys:
            raise NotImplementedError
        if using:
            key = self.get(using)
        else:
            key = keys[0]
        return await key.decrypt(ct, algorithm)

    async def encrypt(
        self,
        pt: bytes | Plaintext,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> EncryptionResult:
        keys = [x for x in self.keys if x.root.use == 'enc']
        if not keys:
            raise NotImplementedError
        if using:
            key = self.get(using)
        else:
            key = keys[0]
        return await key.encrypt(pt, algorithm)

    async def sign(
        self,
        message: bytes,
        algorithm: IAlgorithm | None = None,
        using: str | None = None
    ) -> bytes:
        return await (self.get(using) if using else self.default()).sign(
            message=message,
            algorithm=algorithm,
            using=using
        )

    async def verify(
        self,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm,
        using: str | None = None
    ) -> bool:
        """Verify the given signature and return a boolean indicating
        if the signature is valid.
        
        If the `using` parameter is not ``None``, then it must point
        to a known `kid` in the JSONWebKeySet. An unknown value in the `kid`
        parameter immediately returns ``False``. Otherwise, all keys
        in the JSONWebKeySet are attempted.
        """
        if using is not None and using not in self._index:
            return False

        if using is not None:
            return await self._index[using].verify(signature, message, algorithm)

        return any([
            await k.verify(signature, message, algorithm)
            for k in self.keys if k.can_use(algorithm)
        ])