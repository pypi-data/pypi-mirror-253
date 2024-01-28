# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime

from canonical import EmailAddress
from canonical import Phonenumber
from canonical import UnixTimestamp

from aiopki.types import SubjectID
from .audiencetype import AudienceType
from .jwt import BaseJWT


class OIDCToken(BaseJWT):
    aud: AudienceType
    exp: UnixTimestamp
    iat: UnixTimestamp
    iss: str
    sub: str
    auth_time: UnixTimestamp | None = None
    nonce: str | None = None
    acr: str = '0'
    amr: list[str] | None = None
    azp: str | None = None
    at_hash: str | None = None
    c_hash: str | None = None
    nbf: UnixTimestamp | None = None
    name: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    middle_name: str | None = None
    nickname: str | None = None
    preferred_username: str | None = None
    profile: str | None = None
    picture: str | None = None
    website: str | None = None
    email: EmailAddress | None = None
    email_verified: bool = False
    gender: str | None = None
    birthdate: str | None = None
    zoneinfo: str | None = None
    locale: str | None = None
    phone_number: Phonenumber | str | None = None
    phone_number_verified: bool = False
    updated_at: datetime.datetime | None = None
    
    @property
    def subject_id(self) -> SubjectID:
        return SubjectID(iss=self.iss, sub=self.sub)