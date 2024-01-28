# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio_atexit
from azure.identity.aio import DefaultAzureCredential
from azure.keyvault.keys.aio import KeyClient


credential: DefaultAzureCredential | None = None
key_clients: dict[str, KeyClient] = {}


async def get_credential() -> DefaultAzureCredential:
    global credential
    if credential is None:
        credential = DefaultAzureCredential()
        await credential.__aenter__()
        asyncio_atexit.register(close) # type: ignore
    return credential


async def get_key_client(vault_url: str) -> KeyClient:
    global key_clients
    if vault_url not in key_clients:
        key_clients[vault_url] = client = KeyClient(
            vault_url=vault_url,
            credential=await get_credential()
        )
        await client.__aenter__()
    return key_clients[vault_url]


async def close():
    global credential
    global key_clients
    for client in key_clients.values():
        await client.__aexit__(None, None, None)
    if credential is not None:
        await credential.close()

