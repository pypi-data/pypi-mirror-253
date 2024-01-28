# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import hashlib
import os
from typing import Any

from google.cloud.kms import KeyManagementServiceAsyncClient
from google.cloud.kms import CryptoKeyVersion as GoogleCryptoKeyVersion
from google.cloud.kms import CryptoKey
from cryptography.hazmat.primitives.serialization import load_pem_public_key

from aiopki import CryptoKeyVersion
from aiopki import VersionedCryptoKey
from aiopki.lib import JSONWebKey
from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import Plaintext
from aiopki.utils import b64encode
from aiopki.utils import crc32c
from aiopki.utils import crc32c_check
from .client import get_credential


AlgorithmEnum = GoogleCryptoKeyVersion.CryptoKeyVersionAlgorithm
PurposeEnum = CryptoKey.CryptoKeyPurpose
VersionStateEnum = GoogleCryptoKeyVersion.CryptoKeyVersionState


ALGORITHM_MAPPING: dict[AlgorithmEnum, str] = {
    AlgorithmEnum.HMAC_SHA1                     : 'HS1',
    AlgorithmEnum.HMAC_SHA224                   : 'HS224',
    AlgorithmEnum.HMAC_SHA256                   : 'HS256',
    AlgorithmEnum.HMAC_SHA384                   : 'HS384',
    AlgorithmEnum.HMAC_SHA512                   : 'HS512',
    AlgorithmEnum.EC_SIGN_P256_SHA256           : 'ES256',
    AlgorithmEnum.RSA_SIGN_PKCS1_4096_SHA256    : 'RS256',
    AlgorithmEnum.GOOGLE_SYMMETRIC_ENCRYPTION   : 'A256GCM',
    AlgorithmEnum.RSA_DECRYPT_OAEP_4096_SHA256  : 'RSA-OAEP-256',
}


class GoogleKey(VersionedCryptoKey):

    def model_post_init(self, _: Any) -> None:
        super().model_post_init(_)
        if self.backend != 'cloudkms.googleapis.com':
            raise ValueError(f"Invalid backend: {self.backend}")

    async def discover(self):
        client = KeyManagementServiceAsyncClient(credentials=await get_credential())
        key = await client.get_crypto_key(name=self.name) # type: ignore
        async for version in await client.list_crypto_key_versions(parent=self.name): # type: ignore
            is_enabled = version.state == VersionStateEnum.ENABLED
            thumbprint = None
            public = None
            if key.purpose in {PurposeEnum.MAC, PurposeEnum.ENCRYPT_DECRYPT}:
                thumbprint = b64encode(
                    hashlib.sha256(str.encode(version.name)).digest(),
                    encoder=bytes.decode
                )
            else:
                response = await client.get_public_key(name=version.name) # type: ignore
                if not response.name == version.name:
                    raise ValueError(
                        f"Version mismatch: {response.name} != {version.name}"
                    )
                if not crc32c_check(int(response.pem_crc32c), response.pem.encode('utf-8')): # type: ignore
                    raise ValueError("Invalid response checksum")
                public = JSONWebKey.model_validate({
                    'alg': ALGORITHM_MAPPING[version.algorithm],
                    'key': load_pem_public_key(str.encode(response.pem, 'utf-8')) # type: ignore
                })
                thumbprint = public.thumbprint
            params = client.parse_crypto_key_version_path(version.name)
            self.add_version(
                name=params['crypto_key_version'],
                alg=ALGORITHM_MAPPING[version.algorithm],
                enabled=is_enabled,
                thumbprint=thumbprint,
                public=public
            )
            if not self.has_default():
                self.default_version = thumbprint

    async def decrypt(
        self,
        version: CryptoKeyVersion,
        ct: EncryptionResult,
        algorithm: IAlgorithm
    ) -> Plaintext:
        client, name = await self.client(version)
        func = client.asymmetric_decrypt # type: ignore
        if not version.is_asymmetric():
            func = client.decrypt # type: ignore
            name = self.name
        params: dict[str, int | str| bytes] = {
            "name": name,
            "ciphertext": bytes(ct),
            "ciphertext_crc32c": crc32c(bytes(ct)),
        }
        if ct.aad:
            params['additional_authenticated_data'] = ct.aad
        response = await func(request=params)
        if version.is_asymmetric() and not response.verified_ciphertext_crc32c: # type: ignore
            raise ValueError("The request sent to the server was corrupted in-transit.")
        if not response.plaintext_crc32c == crc32c(response.plaintext):
            raise ValueError(
                "The response received from the server was corrupted in-transit."
            )
        return Plaintext.model_validate({
            'aad': ct.aad,
            'pt': response.plaintext
        })

    async def encrypt(
        self,
        version: CryptoKeyVersion,
        pt: Plaintext,
        algorithm: IAlgorithm
    ) -> EncryptionResult:
        client, name = await self.client(version)
        params: dict[str, int | str | bytes] = {
            "name": name,
            "plaintext": bytes(pt),
            "plaintext_crc32c": crc32c(bytes(pt)),    
        }
        if pt.aad:
            params['additional_authenticated_data'] = pt.aad
        response = await client.encrypt(request=params) # type: ignore
        if not response.verified_plaintext_crc32c:
            raise Exception("The request sent to the server was corrupted in-transit.")
        if not response.ciphertext_crc32c == crc32c(response.ciphertext):
            raise Exception(
                "The response received from the server was corrupted in-transit."
            )
        return EncryptionResult.model_validate({
            'alg': algorithm.name,
            'kid': version.kid,
            'ct': response.ciphertext,
            'iv': os.urandom(12)
        })

    async def sign(
        self,
        version: CryptoKeyVersion,
        message: bytes,
        algorithm: IAlgorithm,
    ) -> bytes:
        client, name = await self.client(version)
        if version.alg in {'HS1','HS224', 'HS256', 'HS384', 'HS512'}:
            response = await client.mac_sign(name=name, data=message) # type: ignore
            sig = response.mac
        else:
            digest = algorithm.digest(message)
            response = await client.asymmetric_sign( # type: ignore
                request={
                    'name': name,
                    'digest': {algorithm.get_digest_name(): digest},
                    'digest_crc32c': crc32c(digest)
                }
            )
            if not response.verified_digest_crc32c:
                raise ValueError("The request sent to the server was corrupted in-transit.")
            if not response.name == name:
                raise ValueError("The request sent to the server was corrupted in-transit.")
            if not response.signature_crc32c == crc32c(response.signature):
                raise ValueError(
                    "The response received from the server was "
                    "corrupted in-transit."
                )
            sig = version.process_signature(response.signature)

        return sig

    async def verify(
        self,
        version: CryptoKeyVersion,
        signature: bytes,
        message: bytes,
        algorithm: IAlgorithm
    ) -> bool:
        client, name = await self.client(version)
        if version.alg in {'HS1','HS224', 'HS256', 'HS384', 'HS512'}:
            response = await client.mac_verify( # type: ignore
                name=name,
                data=message,
                mac=signature
            )
            result = response.success
        elif version.public is not None:
            result = await version.public.verify(
                signature=signature,
                message=message,
                algorithm=algorithm,
            )
        else:
            raise NotImplementedError
        return result

    async def client(self, version: CryptoKeyVersion) -> tuple[KeyManagementServiceAsyncClient, str]:
        client = KeyManagementServiceAsyncClient(credentials=await get_credential())
        return client, client.crypto_key_version_path(
            crypto_key_version=version.name,
            **self.annotations # type: ignore
        )
        