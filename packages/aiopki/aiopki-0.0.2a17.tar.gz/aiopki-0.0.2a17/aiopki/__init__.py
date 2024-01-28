# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .algorithms import *
from .backends import install_backend
from .backends import parse
from .basecryptokey import BaseCryptoKey
from .cryptokeyspecification import CryptoKeySpecification
from .cryptokeytype import CryptoKeyType
from .cryptokeyversion import CryptoKeyVersion
from .cryptokeyuri import CryptoKeyURI
from .secreturi import SecretURI
from .secret import Secret
from .stringsecret import StringSecret
from .versionedcryptokey import VersionedCryptoKey
from .versionedsecret import VersionedSecret
from . import types


__all__: list[str] = [
    'curve',
    'get',
    'register',
    'AESEncryption',
    'EdwardsCurveDigitalSigning',
    'EllipticCurveSigning',
    'HMACSigning',
    'RSAEncryption',
    'RSASigning',
    'curve',
    'install_backend',
    'parse',
    'register',
    'types',
    'BaseCryptoKey',
    'CryptoKeySpecification',
    'CryptoKeyType',
    'CryptoKeyURI',
    'CryptoKeyVersion',
    'Secret',
    'SecretURI',
    'StringSecret',
    'VersionedCryptoKey',
    'VersionedSecret',
]


#def secret(name: str) -> Secret[Any]:
#    return Secret.parse(name)