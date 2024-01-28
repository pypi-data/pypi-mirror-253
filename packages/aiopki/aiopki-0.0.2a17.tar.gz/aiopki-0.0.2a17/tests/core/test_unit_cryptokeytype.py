# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os
from typing import Any

import pytest
from pydantic import TypeAdapter

from aiopki import CryptoKeyType
from aiopki.utils import b64encode


CryptoKeyAdapter = TypeAdapter(CryptoKeyType)


@pytest.mark.parametrize("v", [
    {'kty': 'oct', 'alg': 'HS256', 'use': 'sig', 'k': b64encode(os.urandom(16))},
    'file:///pki/enc.key?kty=RSA&use=enc&alg=RSA-OAEP-256',
])
def test_parse_specification(v: Any):
    CryptoKeyAdapter.validate_python(v)