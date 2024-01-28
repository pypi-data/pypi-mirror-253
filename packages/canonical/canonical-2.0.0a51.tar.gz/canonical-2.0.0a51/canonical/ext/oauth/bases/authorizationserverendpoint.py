# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from canonical.ext.oauth.protocols import IRegisteredClient
from .baseendpoint import BaseEndpoint


class AuthorizationServerEndpoint(BaseEndpoint):
    _client: IRegisteredClient | None

    async def get_client(self) -> IRegisteredClient:
        raise NotImplementedError

    async def setup(self):
        self._client = await self.get_client()
        setattr(self.request.state, 'oauth_client', self._client)