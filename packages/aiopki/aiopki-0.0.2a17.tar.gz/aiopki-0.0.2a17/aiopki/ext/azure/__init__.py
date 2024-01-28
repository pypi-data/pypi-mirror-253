# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import re
import urllib.parse

from canonical import HTTPResourceLocator
from canonical import ResourceName

from aiopki.types import ICryptoKey

from .azurekey import AzureKey


def parse(name: ResourceName | HTTPResourceLocator) -> ICryptoKey | None:
    if not isinstance(name, HTTPResourceLocator):
        return None
    uri = urllib.parse.urlparse(str(name))
    if uri.hostname is None: # pragma: no cover
        return None
    if not re.match(r'^.*\.vault\.azure\.net', uri.hostname):
        return None
    m = re.match(r'^/keys/([^/]+)(/[0-9a-z]+)?$', uri.path)
    if m is None:
        return None
    key, version = m.groups()
    if version:
        version = re.sub(r'[^a-z0-9]+', '', version)
    return AzureKey.model_validate({ # type: ignore
        'backend': 'vault.azure.net',
        'name': key,
        'default_version': version or '__default__',
        'annotations': {
            'vault_url': f'{uri.scheme}://{uri.netloc}'
        }
    })