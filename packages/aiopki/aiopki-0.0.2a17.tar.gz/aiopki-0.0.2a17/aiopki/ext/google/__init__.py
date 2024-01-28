# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from canonical import HTTPResourceLocator
from canonical import ResourceName
from google.cloud.kms import KeyManagementServiceClient
from google.cloud.secretmanager import SecretManagerServiceClient

from .googlekey import GoogleKey
from .googlesecret import GoogleSecret


SUPPORTED_SERVICES: set[str] = {
    'cloudkms.googleapis.com',
    'secretmanager.googleapis.com',
}


def parse(name: ResourceName | HTTPResourceLocator) -> GoogleSecret | GoogleKey | None:
    if not isinstance(name, ResourceName):
        return None
    if name.service not in SUPPORTED_SERVICES:
        return None

    match str(name.service):
        case 'cloudkms.googleapis.com':
            params = KeyManagementServiceClient.parse_crypto_key_version_path(name.relname)
            if not params:
                params = KeyManagementServiceClient.parse_crypto_key_path(name.relname)
            if not params:
                return None
            version = params.pop('crypto_key_version', None)
            return GoogleKey.model_validate({ # type: ignore
                'backend': 'cloudkms.googleapis.com',
                'name': KeyManagementServiceClient.crypto_key_path(**params),
                'default_version': version or '__default__',
                'annotations': params
            })
        case 'secretmanager.googleapis.com':
            params = SecretManagerServiceClient.parse_secret_version_path(name.relname)
            if not params:
                params = SecretManagerServiceClient.parse_secret_path(name.relname)
            if not params:
                return None
            version = params.pop('secret_version', None)
            return GoogleSecret.model_validate({
                'backend': 'cloudkms.googleapis.com',
                'name': SecretManagerServiceClient.secret_path(
                    project=params['project'],
                    secret=params['secret']
                ),
                'default_version': version or '__default__',
                'annotations': params
            })
        case _:
            raise NotImplementedError