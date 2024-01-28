# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from urllib.parse import parse_qsl
from urllib.parse import urlunparse
from urllib.parse import ParseResult

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key

from aiopki.lib import JSONWebKey
from aiopki.types import CryptoKeySpecification
from .cryptokey import LocalKey


def parse(name: CryptoKeySpecification) -> LocalKey | None:
    if isinstance(name, dict):
        jwk = JSONWebKey.model_validate(name)
        if jwk.alg is None:
            raise ValueError("JWK input must specify the `alg` claim.")
        obj = LocalKey(
            backend='localhost',
            name=jwk.thumbprint,
            default_version=jwk.thumbprint
        )
        obj.add_version(
            name=jwk.thumbprint,
            alg=jwk.alg,
            thumbprint=jwk.thumbprint,
            public=jwk.public,
            key=jwk
        )
        return obj
    elif not isinstance(name, ParseResult) or name.scheme != 'file':
        return
    path = name.path[1:]
    if not path:
        raise ValueError(f"Invalid DSN: {urlunparse(name)}")
    with open(path, 'rb') as f:
        buf = f.read()
    is_pem = buf.startswith(b'-----')
    if not is_pem:
        raise NotImplementedError

    # TODO
    try:
        key = load_pem_public_key(buf)
    except ValueError:
        key = load_pem_private_key(buf, None)

    jwk = JSONWebKey.model_validate({
        **dict(parse_qsl(name.query)),
        'key': key
    })

    assert jwk.alg is not None

    obj = LocalKey(
        backend='localhost',
        name=path,
        default_version=jwk.thumbprint
    )
    obj.add_version(
        name=jwk.thumbprint,
        alg=jwk.alg,
        thumbprint=jwk.thumbprint,
        public=jwk.public,
        key=jwk
    )
    return obj