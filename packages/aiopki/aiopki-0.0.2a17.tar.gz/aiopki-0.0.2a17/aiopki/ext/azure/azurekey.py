# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import re
from typing import Any

from azure.identity.aio import DefaultAzureCredential
from azure.keyvault.keys.crypto.aio import CryptographyClient

from aiopki import VersionedCryptoKey
from aiopki import CryptoKeyVersion
from aiopki.lib import JSONWebKey
from aiopki.types import IAlgorithm
from aiopki.utils import b64encode
from .client import get_credential
from .client import get_key_client


EC_ALGORITHMS = {
    'P-256': 'ES256',
    'P-384': 'ES384'
}

DEFAULT_ALGORITHMS: dict[str, dict[str, str]] = {
    'RSA': {
        'encrypt': 'RSA-OAEP-256',
        'verify' : 'RS256',
    }
}


class AzureKey(VersionedCryptoKey):

    def model_post_init(self, _: Any) -> None:
        super().model_post_init(_)
        if self.backend != 'vault.azure.net':
            raise ValueError(f"Invalid backend: {self.backend}")

    async def discover(self):
        client = await get_key_client(str(self.annotations['vault_url']))
        async for props in client.list_properties_of_key_versions(self.name): # type: ignore
            assert props.created_on is not None
            if props.version is None:
                continue
            version = await client.get_key(props.name, version=props.version) # type: ignore
            public = None
            is_enabled = props.enabled if props.enabled is not None else True
            if str(version.key_type or '') not in {'EC', 'EC-HSM', 'RSA', 'RSA-HSM'}:
                raise NotImplementedError
            kty = re.sub(r'^(oct|EC|RSA)(\-HSM)?$', r'\1', str(version.key_type))
            public = {}
            if version.key.crv: # type: ignore
                public['alg'] = EC_ALGORITHMS[version.key.crv] # type: ignore
            key_ops: set[str] = set()
            for attname in version.key._FIELDS: # type: ignore
                v = getattr(version.key, attname)
                if isinstance(v, bytes):
                    v = b64encode(v)
                if attname == 'key_ops':
                    key_ops = v = set([str(x) for x in v])
                public[attname] = v
            public = JSONWebKey.model_validate({
                **public,
                'kty': kty,
                'key_ops': key_ops & {'verify', 'encrypt', 'wrapKey'}
            })
            if public.alg is None:
                public.root.alg = DEFAULT_ALGORITHMS[public.kty][public.key_ops[0]] # type: ignore
            
            # Do not expose the key URI to outside consumers.
            public.root.kid = public.thumbprint
            assert public.alg is not None
            self.add_version(
                name=props.version,
                alg=public.alg,
                enabled=is_enabled,
                thumbprint=public.thumbprint,
                public=public
            )
            if not self.has_default() and is_enabled:
                self.default_version = public.thumbprint

    async def sign(
        self,
        version: CryptoKeyVersion,
        message: bytes,
        algorithm: IAlgorithm,
    ) -> bytes:
        message = algorithm.digest(message)
        async with self.client(version, await get_credential()) as client:
            result = await client.sign(version.public.alg, message) # type: ignore
        return result.signature # type: ignore

    async def verify(
        self,
        version: CryptoKeyVersion,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm
    ) -> bool:
        assert version.public is not None
        return await version.public.verify(signature, message, algorithm)

    def client(self, version: CryptoKeyVersion, credential: DefaultAzureCredential) -> CryptographyClient:
        return CryptographyClient(
            f"{self.annotations['vault_url']}/keys/{self.name}/{version.name}",
            credential=credential
        )