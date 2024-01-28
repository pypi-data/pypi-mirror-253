# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pytest
from jwcrypto import jwk
from jwcrypto import jwe
from jwcrypto.common import json_encode # type: ignore

from aiopki.ext import jose
from aiopki.lib import JSONWebKey


@pytest.mark.asyncio
async def test_compact_decrypt_bytes(
    alg: str,
    enc: str,
    encrypter: JSONWebKey,
    decrypter: JSONWebKey,
    payload_bytes: bytes
) -> None:
    k = jwk.JWK(**encrypter.model_dump(exclude_none=True, mode='json')) # type: ignore
    protected = json_encode({
        'alg': alg,
        'enc': enc
    })
    o1 = jwe.JWE(payload_bytes, protected)
    o1.add_recipient(k) # type: ignore
    t = o1.serialize(compact=True)
    o2 = jose.parse(t)
    assert o2.is_encrypted()
    await o2.decrypt(decrypter)
    assert not o2.is_encrypted()
    assert bytes(o2) == payload_bytes


@pytest.mark.asyncio
async def test_compact_encrypt_bytes(
    alg: str,
    enc: str,
    encrypter: JSONWebKey,
    decrypter: JSONWebKey,
    payload_bytes: bytes
) -> None:
    k = jwk.JWK(**decrypter.model_dump(exclude_none=True, mode='json')) # type: ignore
    o1 = jose.jwe(payload_bytes, alg=alg, enc=enc)
    await o1.add_recipient(encrypter)
    t = o1.encode(encoder=bytes.decode, compact=True)
    o2 = jwe.JWE()
    o2.deserialize(t, k) # type: ignore
    assert o2.payload == payload_bytes # type: ignore