# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic


JOSE_CTY: set[str] = {
    'jose',
    'jose+json',
    'application/jose',
    'application/jose+json',
}


class Payload(pydantic.BaseModel):
    cty: str | None = None
    value: bytes

    @property
    def typ(self) -> None:
        return None

    def is_compact(self) -> bool:
        return self.cty in {'jose', 'application/json'}

    def is_jose(self) -> bool:
        return self.cty in JOSE_CTY

    def __bytes__(self) -> bytes:
        return self.value