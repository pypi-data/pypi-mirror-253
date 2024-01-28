# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Callable
from typing import Literal
from typing import TypeVar

import pydantic

from aiopki.algorithms import get as get_algorithm
from aiopki.lib import JSONWebKey
from aiopki.types import Base64
from aiopki.types import Base64JSON
from aiopki.types import EncryptionResult
from aiopki.types import IAlgorithm
from aiopki.types import IDecrypter
from aiopki.types import IEncrypter
from aiopki.types import IVerifier
from aiopki.types import JSONObject
from aiopki.types import Plaintext
from aiopki.types import Undecryptable
from aiopki.utils import b64encode
from aiopki.utils import b64encode_json
from .jws import JWS
from .payload import Payload
from .recipient import Recipient


T = TypeVar('T')


class JWE(pydantic.BaseModel):
    protected: Base64JSON = pydantic.Field(
        default_factory=Base64JSON
    )

    unprotected: JSONObject = pydantic.Field(
        default_factory=JSONObject
    )

    ciphertext: Base64

    # TODO: differs based on compact or json encoding
    aad: Base64 = pydantic.Field(
        default_factory=Base64
    )

    mode: Literal['compact', 'json', 'unset'] = pydantic.Field(
        default=...
    )

    iv: Base64 = pydantic.Field(
        default_factory=Base64
    )
    tag: Base64 = pydantic.Field(
        default_factory=Base64
    )

    payload: Base64 | None = None

    recipients: list[Recipient] = pydantic.Field(
        default=...
    )

    _cek: JSONWebKey | None = pydantic.PrivateAttr(default=None)

    @property
    def alg(self) -> IAlgorithm | None:
        if self.claims.get('alg'):
            return get_algorithm(self.claims['alg'])

    @property
    def claims(self) -> dict[str, Any]:
        return {
            **(self.unprotected or {}),
            **(self.protected or {})
        }

    @property
    def cty(self) -> str | None:
        return self.claims.get('cty')

    @property
    def typ(self) -> str | None:
        return self.claims.get('typ')

    @property
    def enc(self) -> IAlgorithm:
        return get_algorithm(self.claims['enc'])

    def encode(
        self,
        compact: bool = False,
        encoder: Callable[[bytes], T] = bytes
    ) -> T:
        """Encodes the JWS/JWE."""
        if self.mode != 'compact' or not compact:
            raise NotImplementedError
        recipient, *recipients = self.recipients
        kwargs: dict[str, Any] = {
            'mode': 'json'
        }
        exclude = kwargs.setdefault('exclude', {
            'mode',
            'payload'
        })
        
        # If there is only one recipient, add its algorithm
        # to the protected header.
        if not recipients and recipient.header.get('alg'):
            self.protected['alg'] = recipient.header['alg']

        if self.mode == 'compact':
            # In Compact Serialization there are no recipients included
            # in the encoded result. There is also no unprotected header.
            assert not self.unprotected
            exclude.update({'unprotected', 'recipients'})

        if not self.ciphertext:
            self._encrypt()
        params = {k: v for k, v in self.model_dump(**kwargs).items() if v}
        params.setdefault('key', '')
    
        if self.recipients and self._cek:
            assert self.recipients[0].encrypted_key is not None
            params['key'] = b64encode(self.recipients[0].encrypted_key, encoder=bytes.decode)
        result = '{protected}.{key}.{iv}.{ciphertext}.{tag}'.format(**params)
        return encoder(str.encode(result, 'ascii'))

    def model_post_init(self, _: Any) -> None:
        protected = self.protected or {}
        unprotected = self.unprotected or {}
        if bool(set(protected) & set(unprotected)):
            raise ValueError(
                "The claims in the protected and unprotected "
                "header must be disjoint."
            )
        for recipient in self.recipients:
            recipient.update_header(self.claims)

        # If there are no recipients, then we are creating a new
        # JWE. Generate a Content Encryption Key (CEK). For each
        # recipient we will add this key. If Direct Encryption is
        # used, then the CEK is not used (because the recipient
        # key is the CEK).
        if self.alg and self.alg.name != 'dir':
            self._cek = self.enc.cek(factory=JSONWebKey.model_validate)

    def get_ciphertext(self, recipient: Recipient) -> EncryptionResult:
        return EncryptionResult.model_validate({
            'alg': recipient.alg.name,
            'ct': self.ciphertext,
            'aad': self.aad,
            'iv': recipient.iv or self.iv,
            'tag': self.tag
        })

    async def add_recipient(
        self,
        encrypter: IEncrypter,
        enc: IAlgorithm | None = None,
        alg: IAlgorithm | None = None
    ):
        alg = alg or encrypter.default_algorithm()
        enc = self.enc or get_algorithm('A128GCM')
        params: dict[str, Any] = {}
        if self.payload is None:
            raise ValueError("Cannot encrypt without a payload.")
        if alg and self.alg and self.alg.name != alg.name:
            raise TypeError(f'Algorithm {alg.name} can not be used with this JWE.')
        if enc and self.enc and self.enc.name != enc.name:
            raise TypeError(f'Algorithm {enc.name} can not be used with this JWE.')
        if alg.name == 'dir' and self.recipients:
            raise TypeError(
                "Multiple recipients are not allowed in Direct Encryption "
                "mode."
            )
        if alg.name == 'dir':
            self.protected['alg'] = alg.name
        elif not self._cek:
            self._cek = self.enc.cek(factory=JSONWebKey.model_validate)
        if not alg.is_direct():
            assert self._cek is not None
            ct = await encrypter.encrypt(
                pt=bytes(self._cek),
                algorithm=alg
            )
            assert not ct.aad
            assert not ct.iv
            assert not ct.tag
            params['header'] = {'alg': alg.name}
            params['encrypted_key'] = bytes(ct)

        self.recipients.append(Recipient.model_validate(params))
        if len(self.recipients) > 1:
            self.mode = 'json'

        # If Direct Encryption is used, then the encrypter is the CEK
        # and thus must the payload be encrypted.
        if alg.name == 'dir':
            await self._encrypt_direct(encrypter)
        self.mode = 'compact'

    async def decrypt(self, decrypter: IDecrypter) -> JWS | Payload:
        candidates: list[Recipient] = []
        for recipient in self.recipients:
            if not recipient.can_decrypt(decrypter):
                continue
            candidates.append(recipient)
        if not candidates:
            raise Undecryptable(
                "The provided decrypter is not usable with "
                "any of the recipients."
            )
        payload = None
        for recipient in candidates:
            ct = self.get_ciphertext(recipient)
            try:
                payload = await recipient.decrypt(decrypter, ct)
            except Undecryptable:
                continue
        if payload is None:
            raise Undecryptable
        return Payload(cty=self.cty, value=bytes(payload))

    async def verify(self, verifier: IVerifier) -> bool:
        raise NotImplementedError("JWE does not have a signature.")

    async def _encrypt_direct(self, cek: IEncrypter) -> None:
        assert self.payload is not None
        ct = await cek.encrypt(
            pt=Plaintext(
                pt=bytes(self.payload),
                aad=b64encode_json(self.protected)
            ),
            algorithm=None
        )
        self._update_cek_encryption_result(ct)

    def _encrypt(self) -> None:
        assert self._cek is not None
        assert self.payload is not None
        ct = self._cek.encrypt_sync(
            pt=Plaintext(
                pt=bytes(self.payload),
                aad=b64encode_json(self.protected)
            ),
            algorithm=None
        )
        self._update_cek_encryption_result(ct)

    def _update_cek_encryption_result(self, ct: EncryptionResult) -> None:
        assert ct.aad
        assert ct.iv
        assert ct.tag
        self.aad, self.ciphertext, self.iv, self.tag = (
            Base64(ct.aad),
            Base64(bytes(ct)),
            Base64(ct.iv),
            Base64(ct.tag)
        )