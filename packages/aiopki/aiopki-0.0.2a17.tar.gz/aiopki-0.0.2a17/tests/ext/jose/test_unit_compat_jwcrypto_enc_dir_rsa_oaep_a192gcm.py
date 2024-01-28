# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from aiopki.tests.compat.jwe import *


@pytest.fixture(scope='module')
def alg() -> str:
    return 'RSA-OAEP'


@pytest.fixture(scope='module')
def enc() -> str:
    return 'A192GCM'


@pytest.fixture(scope='module')
def encrypter(decrypter: JSONWebKey) -> JSONWebKey:
    assert decrypter.public is not None
    return decrypter.public


@pytest.fixture(scope='module')
def decrypter(alg: str, rsa_key: RSAPrivateKey) -> JSONWebKey:
    return JSONWebKey.model_validate({
        'kty': 'RSA',
        'use': 'enc',
        'alg': alg,
        'key': rsa_key,
        'key_ops': ['wrapKey', 'unwrapKey']
    })
