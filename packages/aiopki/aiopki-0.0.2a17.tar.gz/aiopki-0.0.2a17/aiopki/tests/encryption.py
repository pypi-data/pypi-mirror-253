# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pytest

import aiopki


@pytest.mark.asyncio
async def test_encrypt_decrypt_bytes(
    encryption_key: aiopki.CryptoKeyType
):
    ct = await encryption_key.encrypt(b'Hello world!')
    pt = await encryption_key.decrypt(ct)
    assert bytes(pt) == b'Hello world!'