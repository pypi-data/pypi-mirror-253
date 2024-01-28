# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from canonical import ResourceName

import aiopki
from aiopki.tests.signing import *


@pytest.fixture(scope='module')
def key_uri() -> ResourceName:
    return ResourceName('//cloudkms.googleapis.com/projects/unimatrixdev/locations/europe-west4/keyRings/local/cryptoKeys/ec_sign_p256_sha256')

@pytest.fixture
def signing_algorithm() -> IAlgorithm:
    return aiopki.algorithms.get('ES256')