# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import copy

from cryptography.hazmat.primitives.asymmetric import ec

from ..types import IAlgorithm
from .aesencryption import AESEncryption
from .directencryption import DirectEncryption
from .edwardscurvedigitalsigning import EdwardsCurveDigitalSigning
from .ellipticcurvesigning import EllipticCurveSigning
from .hmacsigning import HMACSigning
from .notimplemented import NotImplementedAlgorithm
from .rsaalgorithm import RSAAlgorithm
from .rsaencryption import RSAEncryption
from .rsasigning import RSASigning


__all__: list[str] = [
    'curve',
    'get',
    'register',
    'AESEncryption',
    'EdwardsCurveDigitalSigning',
    'EllipticCurveSigning',
    'HMACSigning',
    'RSAAlgorithm',
    'RSAEncryption',
    'RSASigning',
]


_REGISTRY: dict[str, IAlgorithm] = {}

CURVE_MAPPING: dict[str, type[ec.EllipticCurve]] = {
    "P-256": ec.SECP256R1,
    "P-384": ec.SECP384R1,
    "P-521": ec.SECP521R1,
    "P-256K": ec.SECP256K1,
    "P-512": ec.SECP521R1,
    ec.SECP256R1.__name__: ec.SECP256R1, 
    ec.SECP384R1.__name__: ec.SECP384R1, 
    ec.SECP521R1.__name__: ec.SECP521R1, 
    ec.SECP256K1.__name__: ec.SECP256K1, 
}


def curve(name: str) -> ec.EllipticCurve:
    return CURVE_MAPPING[name]()


def register(name: str, alg: IAlgorithm) -> None:
    alg = copy.deepcopy(alg)
    alg.name = name
    _REGISTRY[name] = alg


def get(name: str) -> IAlgorithm:
    return _REGISTRY[name]


register('notimplemented', NotImplementedAlgorithm())
register('HS256', HMACSigning('sha256'))
register('HS384', HMACSigning('sha384'))
register('HS512', HMACSigning('sha512'))
register('RS256', RSASigning('sha256', 'RSASSA-PKCS1-v1_5'))
register('ES256', EllipticCurveSigning('P-256', 'sha256'))
register('ES384', EllipticCurveSigning('P-384', 'sha384'))
register('ES512', EllipticCurveSigning('P-521', 'sha512'))
register('ES256K', EllipticCurveSigning('P-256K', 'sha256'))
register('EdDSA', EdwardsCurveDigitalSigning())

register('dir', DirectEncryption())
register('A128GCM', AESEncryption(16, mode='GCM'))
register('A192GCM', AESEncryption(24, mode='GCM'))
register('A256GCM', AESEncryption(32, mode='GCM'))
register('RSA-OAEP', RSAEncryption('sha1', 'EME-OAEP'))
register('RSA-OAEP-256', RSAEncryption('sha256', 'EME-OAEP'))