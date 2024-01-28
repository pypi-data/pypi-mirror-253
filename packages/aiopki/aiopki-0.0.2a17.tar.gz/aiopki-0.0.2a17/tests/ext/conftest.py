# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pytest
import pytest_asyncio

import aiopki
from canonical import HTTPResourceLocator
from canonical import ResourceName
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key


@pytest_asyncio.fixture(scope='module') # type: ignore
async def signing_key(key_uri: HTTPResourceLocator | ResourceName | str) -> aiopki.types.ICryptoKey:
    return await aiopki.CryptoKeyType.parse(key_uri) # type: ignore


@pytest_asyncio.fixture(scope='module') # type: ignore
async def encryption_key(key_uri: HTTPResourceLocator | ResourceName | str) -> aiopki.types.ICryptoKey:
    return await aiopki.CryptoKeyType.parse(key_uri) # type: ignore


@pytest.fixture(scope='session')
def rsa_key() -> RSAPrivateKey:
    return generate_private_key(65537, 2048)