# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import AsyncIterator
from typing import Protocol
from typing import Self
from typing import TypeVar


T = TypeVar('T', covariant=True)


class ITransaction(Protocol):
    __module__: str = 'canonical.protocols'

    async def transaction(
        self,
        transaction: Self | None = None
    ) -> AsyncIterator[Self]:
        ...