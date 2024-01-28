# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pytest
import pytest_asyncio

import aiopki


aiopki.install_backend('aiopki.ext.azure')


@pytest.fixture(scope='module')
def vault_url() -> str:
    return 'https://python-oauthx.vault.azure.net/'


@pytest_asyncio.fixture(scope='module') # type: ignore
async def verifier(signing_key: Any):
    return signing_key