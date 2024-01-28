# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os

from aiopki.tests.compat.jwe import *
from aiopki.utils import b64encode


@pytest.fixture(scope='module')
def alg() -> str:
    return 'dir'


@pytest.fixture(scope='module')
def enc() -> str:
    return 'A192GCM'


@pytest.fixture(scope='module')
def encrypter(alg: str) -> JSONWebKey:
    return JSONWebKey.model_validate({
        'kty': 'oct',
        'use': 'enc',
        'alg': alg,
        'k': b64encode(os.urandom(24))
    })


@pytest.fixture(scope='module')
def decrypter(encrypter: JSONWebKey) -> JSONWebKey:
    return encrypter