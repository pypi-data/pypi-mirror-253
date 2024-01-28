# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

from .symmetricencryptionkey import SymmetricEncryptionKey


class SymmetricWrappingKey(SymmetricEncryptionKey):
    alg: Literal['A128CBC-HS256', 'A192CBC-HS384', 'A256CBC-HS512', 'A128GCM', 'A192GCM', 'A256GCM'] # type: ignore
    key_ops: list[Literal['wrapKey', 'unwrapKey']] = ['wrapKey', 'unwrapKey'] # type: ignore