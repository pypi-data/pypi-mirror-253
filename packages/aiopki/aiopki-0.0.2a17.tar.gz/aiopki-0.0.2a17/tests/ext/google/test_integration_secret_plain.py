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
from canonical import ResourceName

import aiopki


@pytest.fixture(scope='module')
def secret_name() -> ResourceName:
    return ResourceName('//secretmanager.googleapis.com/projects/641438517445/secrets/test-plain/versions/2')


@pytest_asyncio.fixture(scope='module') # type: ignore
async def secret(secret_name: Any) -> aiopki.Secret[str]:
    return aiopki.StringSecret.parse(secret_name)


@pytest.mark.asyncio
async def test_secret_content(
    secret: aiopki.Secret[str]
):
    assert await secret == 'Hello world 2!'