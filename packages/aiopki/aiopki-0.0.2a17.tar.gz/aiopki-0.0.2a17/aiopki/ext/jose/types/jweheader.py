# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import json
from typing import Any
from typing import Literal

import pydantic

from aiopki.types import Base64
from aiopki.utils import b64encode
from aiopki.utils import b64decode_json
from .jwa import JWA
from .jwk import JWK


EncryptionAlgorithm = Literal[
    JWA.a128gcm,
    JWA.a192gcm,
    JWA.a256gcm,
]


class JWEHeader(pydantic.BaseModel):
    alg: JWA
    cty: str | None = None
    crit: list[str] = []
    jku: str | None = None
    jwk: JWK | None = None
    kid: str | None = None
    typ: str | None = None
    x5c: str | None = None
    x5t: str | None = None
    x5t_sha256: str | None = pydantic.Field(default=None, alias='x5t#S256')
    x5u: str | None = None
    claims: dict[str, Any] = {}

    enc: Literal[EncryptionAlgorithm]
    tag: Base64 | None = None
    iv: Base64 | None = None
    zip: str | None = None

    @pydantic.model_validator(mode='before')
    def preprocess(cls, values: dict[str, Any] | str) -> dict[str, Any]:
        if isinstance(values, str):
            result = b64decode_json(values)
            if not isinstance(result, dict):
                raise ValueError("The JWE Protected Header must be a JSON object.")
            values = result
        return {
            **{
                name: values[name] for name in cls.model_fields.keys()
                if name in values and name != 'claims'
            },
            **(values.get('claims') or {})
        }

    def encode(self, **kwargs: Any) -> bytes:
        kwargs.setdefault('exclude_none', True)
        kwargs.setdefault('exclude_defaults', True)
        kwargs.setdefault('exclude_unset', True)
        exclude = kwargs.setdefault('exclude', set())
        exclude.add('claims')
        claims = self.model_dump(**kwargs)
        claims.update(self.claims)
        return b64encode(json.dumps(claims))