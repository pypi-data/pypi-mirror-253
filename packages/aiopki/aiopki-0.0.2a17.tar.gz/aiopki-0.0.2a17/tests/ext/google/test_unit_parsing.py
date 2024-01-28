# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pytest

import pydantic
from aiopki import CryptoKeyType


class Model(pydantic.BaseModel):
    key: CryptoKeyType


@pytest.mark.parametrize("name", [
    '//cloudkms.googleapis.com/projects/unimatrixdev/locations/europe-west4/keyRings/local/cryptoKeys/aes256gcm',
    '//cloudkms.googleapis.com/projects/unimatrixdev/locations/europe-west4/keyRings/local/cryptoKeys/aes256gcm/cryptoKeyVersions/3'
])
def test_parse_resource_name(name: str):
    obj = Model.model_validate({'key': name})
    assert isinstance(obj.key, CryptoKeyType)