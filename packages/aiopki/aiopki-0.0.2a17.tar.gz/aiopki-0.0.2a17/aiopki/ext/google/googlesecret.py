# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from google.cloud.secretmanager import ListSecretVersionsRequest
from google.cloud.secretmanager import SecretManagerServiceAsyncClient
from google.cloud.secretmanager import SecretVersion

from aiopki import VersionedSecret
from .client import get_credential


class GoogleSecret(VersionedSecret):

    async def default(self) -> Any:
        client = SecretManagerServiceAsyncClient(
            credentials=await get_credential()
        )
        response = await client.access_secret_version( # type: ignore
            name=client.secret_version_path(
                secret_version=self.default_version,
                **client.parse_secret_path(self.name),
            )
        )
        return response.payload.data

    async def discover(self) -> None:
        client = SecretManagerServiceAsyncClient(
            credentials=await get_credential()
        )
        request = ListSecretVersionsRequest(parent=self.name)
        result = await client.list_secret_versions(request) # type: ignore
        async for version in result:
            if version.state != SecretVersion.State.ENABLED:
                continue
            params = client.parse_secret_version_path(version.name)
            if not self.has_default():
                self.default_version = params['secret_version']