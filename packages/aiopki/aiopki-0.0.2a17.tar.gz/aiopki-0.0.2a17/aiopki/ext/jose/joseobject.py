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

import aiopki
from aiopki.types import IAlgorithm
from aiopki.types import IDecrypter
from aiopki.types import IEncrypter
from aiopki.types import ISigner
from aiopki.types import IVerifier
from aiopki.utils import b64decode
from .types import JWE
from .types import JWS
from .types import JWT
from .types import Payload


T = TypeVar('T')


class JOSEObject(pydantic.RootModel[JWS | JWE | Payload]):

    @property
    def typ(self) -> str | None:
        return str.lower(self.root.typ) if self.root.typ else None

    @staticmethod
    def deserialize(value: str | bytes) -> dict[str, Any]:
        if isinstance(value, bytes):
            value = bytes.decode(value, 'ascii')
        params: dict[str, Any] = {}
        if value.count('.') == 2:
            protected, payload, signature = str.split(value, '.')
            params.update({
                'payload': payload,
                'signatures': [{
                    'protected': protected,
                    'signature': b64decode(signature)
                }]
            })
        if value.count('.') == 4:
            protected, key, iv, ct, tag = str.split(value, '.')
            
            params.update({
                'aad': str.encode(protected, 'ascii'),
                'ciphertext': ct,
                'iv': iv,
                'mode': 'compact',
                'protected': protected,
                'recipients': [{'encrypted_key': key}],
                'tag': tag,
            })
        return params

    @classmethod
    def jwe(
        cls,
        payload: JWS | dict[str, Any] | bytes,
        enc: str | IAlgorithm, 
        alg: str | IAlgorithm | None = None,
        cty: str | None = None,
        protected: dict[str, Any] | None = None,
        mode: Literal['compact', 'json', 'unset'] = 'unset',
    ) -> JWE:
        """Create a new JSON Web Encryption (JWE) instance.

        Args:
            payload: the payload of the JWE. Can be either a byte-sequences
                or dictionary.
            enc (:class:`aiopki.types.IAlgorithm`): specifies the algorithm that is
                used to encrypt content using the CEK.
            alg (:class:`aiopki.types.IAlgorithm`): specifies the algorithm that is
                used to encrypt the Content Encryption Key (CEK). If the `alg`
                parameter is provided, then all recipients are required to use this
                algorithm; otherwise each recipient must specify its own.
                See also :meth:`aiopki.ext.jose.types.JWE.add_recipient()`
            cty (str): optionally specifies the content type (``cty`` header),
                if it can not be inferred from the payload type.

        Returns:
            :class:`aiopki.ext.jose.JOSEObject`
        """
        protected = protected or {}
        if isinstance(alg, str):
            alg = aiopki.get(alg)
        if isinstance(enc, str):
            enc = aiopki.get(enc)
        if alg is not None:
            protected['alg'] = alg.name
        protected['enc'] = enc.name
        if cty:
            protected['cty'] = cty
        if isinstance(payload, JWS):
            payload, protected['cty'] = payload.serialize()
        obj = cls.model_validate({
            'ciphertext': b'',
            'mode': mode,
            'payload': payload,
            'protected': protected or b'',
            'recipients': [],
            'mode': mode
        })
        assert isinstance(obj.root, JWE)
        return obj.root

    @classmethod
    def parse_compact(cls, value: str | bytes):
        return cls.model_validate(cls.deserialize(value))

    @pydantic.model_validator(mode='before')
    def preprocess(cls, value: Any) -> Any:
        if isinstance(value, str):
            value = cls.deserialize(value)
        return value

    def payload(
        self,
        factory: Callable[[bytes], T] = JWT.model_validate
    ) -> T:
        assert not isinstance(self.root, Payload)
        obj = self.root
        if isinstance(obj, JWE):
            raise NotImplementedError
        assert obj.payload is not None
        return factory(b64decode(obj.payload))

    def encode(self, encoder: Callable[[bytes], T] = bytes, compact: bool = False) -> T:
        """Encodes the JWS/JWE.

        Args:
            encoder: encodes the result, if an encoding other than bytes
                is needed.
            compact (bool): indicates if compact encoding is required.
                Using ``compact=True`` with a JOSE object that has
                multiple recipients or signers, raises an :exc:`ValueError`.

        Returns:
            bytes
        """
        assert not isinstance(self.root, Payload)
        return encoder(self.root.encode(compact=compact))

    def is_encrypted(self) -> bool:
        return isinstance(self.root, JWE)

    async def add_recipient(
        self,
        encrypter: IEncrypter,
        enc: IAlgorithm | str = 'A128GCM',
        alg: IAlgorithm | str | None = None,
    ):
        if not isinstance(self.root, JWE):
            raise TypeError(f"Can not add recipients to {type(self.root).__name__}")
        if isinstance(alg, str):
            alg = aiopki.get(alg)
        if isinstance(enc, str):
            enc = aiopki.get(enc)
        return await self.root.add_recipient(
            encrypter=encrypter,
            alg=alg,
            enc=enc
        )

    async def decrypt(self, decrypter: IDecrypter) -> None:
        assert isinstance(self.root, JWE)
        self.root = await self.root.decrypt(decrypter)

        assert isinstance(self.root, Payload)
        if self.root.is_jose():
            assert self.root.is_compact()
            self.root = self.parse_compact(bytes(self.root)).root

    async def encrypt(
        self,
        encrypter: IEncrypter | None = None,
        alg: IAlgorithm | None = None,
        enc: IAlgorithm | None = None,
    ) -> None:
        """Encrypt the :class:`JOSEObject` using the appropriate means.

        If the object is JSON Web Encryption (JWE), use the Content Encryption
        Key (CEK) to encrypt the payload if Key Encryption, Key Agreement or
        Key Wrapping is used.

        Args:
            encrypter (:class:`aiopki.types.IEncrypter`): the encrypter used to
                encrypt the payload, or ``None`` if the payload knows how to
                encrypt itself.

        Returns:
            None

        Raises:
            :exc:`TypeError`: the `encrypter` parameter is ``None`` and the
                payload can not encrypt itself.
            :exc:`TypeError`: the object is a JWE with multiple recipients
                and `compact` is ``True``.
        """
        if isinstance(self.root, JWE):
            pass
        elif isinstance(self.root, JWS):
            if encrypter is None:
                raise TypeError("The `encrypter` argument is required.")
            self.root = self.jwe(
                payload=self.root,
                alg=alg,
                enc=enc or 'A256GCM'
            )
            await self.root.add_recipient(encrypter)
        else:
            raise NotImplementedError

    async def sign(
        self,
        algorithm: str | IAlgorithm,
        signer: ISigner,
        protected: dict[str, Any] | None = None,
        header: dict[str, Any] | None = None
    ) -> None:
        """Add a signature to a JWS object."""
        if not isinstance(self.root, JWS):
            raise NotImplementedError
        if isinstance(algorithm, str):
            algorithm = aiopki.get(algorithm)
        await self.root.sign(algorithm, signer, protected or {}, header or {})

    async def verify(self, verifier: IVerifier) -> bool:
        """Return a boolean indicating if at least one signature
        validated using the given verifier. Raise an exception if
        the object does not have signatures (i.e. is JWE).
        """
        if not isinstance(self.root, JWS):
            raise NotImplementedError
        return await self.root.verify(verifier)

    def __bytes__(self) -> bytes:
        if not isinstance(self.root, Payload):
            raise TypeError(f'Can not cast {type(self).__name__} to bytes')
        return bytes(self.root)