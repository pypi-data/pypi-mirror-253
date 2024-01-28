# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Callable
from typing import TypeVar

import pydantic


T = TypeVar('T')


class SubjectID(pydantic.BaseModel):
    iss: str
    sub: str

    @property
    def maskable(self) -> bytes:
        return str.encode(f'subject:{self.iss}/{self.sub}', 'utf-8')

    def mask(self, masker: Callable[[bytes], T]) -> T:
        return masker(self.maskable)

    def __hash__(self) -> int:
        return hash((self.iss, self.sub))