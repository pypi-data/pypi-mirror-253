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
from typing import ClassVar
from typing import Literal

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature

import aiopki
from aiopki.algorithms import EllipticCurveSigning
from aiopki.types import IAlgorithm
from aiopki.utils import b64decode_int
from aiopki.utils import b64encode
from aiopki.utils import b64encode_int
from aiopki.utils import bytes_to_number
from aiopki.utils import normalize_ec_signature
from .basejwk import BaseJWK


class EllipticCurvePublicKey(BaseJWK):
    curves: ClassVar[dict[str, str]] = {
        'secp256k1': 'P-256K',
        'secp256r1': 'P-256',
        'secp384r1': 'P-384',
        'secp521r1': 'P-512',
    }
    kty: Literal['EC']
    crv: str # type: ignore
    x: str
    y: str
    _public_numbers: ec.EllipticCurvePublicNumbers

    @property
    def public(self): # pragma: no cover
        return self

    @property
    def public_key(self) -> ec.EllipticCurvePublicKey:
        return self._public_numbers.public_key()

    @property
    def thumbprint(self) -> str:
        message = self.public.model_dump_json(include={'crv', 'kty', 'x', 'y'})
        return b64encode(hashlib.sha256(str.encode(message)).digest(), encoder=bytes.decode)

    @classmethod
    def preprocess_key(cls, key: ec.EllipticCurvePublicKey | Any, **values: Any) -> dict[str, Any]:
        if not isinstance(key, ec.EllipticCurvePublicKey):
            raise NotImplementedError
        numbers = key.public_numbers()
        return {
            'kty': 'EC',
            'use': 'sig',
            'crv': EllipticCurvePublicKey.curves[key.curve.name],
            'x': b64encode_int(numbers.x),
            'y': b64encode_int(numbers.y),
        }

    def can_use(self, algorithm: IAlgorithm) -> bool:
        if not isinstance(algorithm, EllipticCurveSigning):
            return False
        return algorithm.curve == self.crv

    def model_post_init(self, *args: Any, **kwargs: Any) -> None:
        self._public_numbers = ec.EllipticCurvePublicNumbers(
            curve=aiopki.curve(self.crv),
            x=b64decode_int(self.x),
            y=b64decode_int(self.y)
        )

    async def verify(
        self,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm,
        using: str | None = None
    ) -> bool:
        n = (self.public_key.curve.key_size + 7) // 8
        try:
            self.public_key.verify(
                signature=encode_dss_signature(
                    bytes_to_number(signature[:n]),
                    bytes_to_number(signature[n:]),
                ),
                data=message,
                signature_algorithm=ec.ECDSA(algorithm.get_digest_algorithm())
            )
            return True
        except InvalidSignature:
            return False

    def process_signature(self, signature: bytes) -> bytes:
        return normalize_ec_signature(
            l=(self.public_key.curve.key_size + 7) // 8,
            sig=signature
        )