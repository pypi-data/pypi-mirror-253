# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import json
import operator
import secrets
from typing import Any
from typing import Callable
from typing import Iterable

import pydantic
from canonical import UnixTimestamp

from aiopki.utils import b64encode_json
from .audiencetype import AudienceType


class BaseJWT(pydantic.BaseModel):
    claims: dict[str, Any] = pydantic.Field(default={}, alias='__claims__')

    @classmethod
    def new(cls, ttl: int, **kwargs: Any):
        """Create a new :class:`JWT`."""
        now = datetime.datetime.now(datetime.timezone.utc)
        return cls.model_validate({
            'jti': secrets.token_urlsafe(48),
            **kwargs,
            'exp': (now + datetime.timedelta(seconds=ttl)),
            'iat': now,
            'nbf': now,
        })

    @pydantic.model_validator(mode='before')
    def preprocess(cls, values: bytes | str | dict[str, Any]) -> dict[str, Any]:
        if isinstance(values, (bytes, str)):
            values = json.loads(values)
        assert isinstance(values, dict)
        return {
            **values,
            '__claims__': {
                k: v
                for k, v in values.items()
                if k not in cls.model_fields
            }
        }

    @pydantic.model_serializer(mode='wrap', when_used='always')
    def serialize_model(
        self,
        info: Callable[['BaseJWT'], dict[str, Any]]
    ):
        values = info(self)
        if 'claims' in values:
            values = {**values.pop('claims'), **values}
        return values

    def model_dump_json(self, **kwargs: Any) -> str:
        kwargs.setdefault('exclude_none', True)
        kwargs.setdefault('exclude_defaults', True)
        kwargs.setdefault('exclude_unset', True)
        return super().model_dump_json(**kwargs)

    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        kwargs.setdefault('exclude_none', True)
        kwargs.setdefault('exclude_defaults', True)
        kwargs.setdefault('exclude_unset', True)
        return super().model_dump(**kwargs)

    def encode(self, **kwargs: Any) -> bytes:
        """Encode the payload of the JWT."""
        kwargs.setdefault('exclude_defaults', True)
        kwargs.setdefault('exclude_none', True)
        return b64encode_json({
            **self.claims,
            **self.model_dump(**kwargs)
        })

    def has_claims(self, claims: Iterable[str]) -> bool:
        """Return a boolean indicating if the token has the given claims."""
        return set(claims) <= set(self.model_dump(exclude_none=True))


class JWT(BaseJWT):
    aud: AudienceType | None = None
    exp: UnixTimestamp | None = None
    iat: UnixTimestamp | None = None
    iss: str | None = None
    jti: str | None = None
    nbf: UnixTimestamp | None = None
    sub: str | None = None
    _now: datetime.datetime = pydantic.PrivateAttr()

    def model_post_init(self, _: Any) -> None:
        self._now = datetime.datetime.now(datetime.timezone.utc)

    def has_audience(self, value: str) -> bool:
        return self.aud is not None and value in self.aud

    def validate_aud(self, aud: str | set[str]):
        return self.aud is not None and any([
            isinstance(aud, str) and aud in self.aud,
            isinstance(aud, set) and  bool(aud & self.aud),
        ])

    def validate_exp(self, now: datetime.datetime | None = None):
        return self._validate_timestamp(self.exp, operator.ge, now)

    def validate_iat(
        self,
        max_age: int,
        now: datetime.datetime | None = None,
        required: bool = True
    ):
        if self.iat is None:
            return not required
        exp = (now or self._now) - datetime.timedelta(seconds=max_age)
        return self.iat > exp

    def validate_iss(self, iss: str) -> bool:
        return all([
            self.iss is not None,
            self.iss == iss
        ])

    def validate_nbf(
        self,
        now: datetime.datetime | None = None,
        required: bool = True
    ):
        return any([
            self.nbf is None and not required,
            self._validate_timestamp(self.nbf, operator.le, now)
        ])

    def _validate_timestamp(
        self,
        value: datetime.datetime | None,
        op: Callable[[datetime.datetime, datetime.datetime], bool],
        now: datetime.datetime | None = None
    ) -> bool:
        if value is None:
            return False
        return op(value, (now or self._now))