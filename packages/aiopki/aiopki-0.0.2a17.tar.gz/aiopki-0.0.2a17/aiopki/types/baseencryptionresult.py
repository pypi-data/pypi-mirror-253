# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from aiopki.types import Base64


class BaseEncryptionResult(pydantic.BaseModel):
    alg: str = pydantic.Field(
        default=...
    )

    kid: str | None = pydantic.Field(
        default=None
    )
    ct: Base64 = pydantic.Field(
        default=...
    )

    def __bytes__(self) -> bytes:
        return self.ct