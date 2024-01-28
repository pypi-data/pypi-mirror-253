# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import cast
from typing import Any

import fastapi

from canonical.ext.fastapi.params import ResourceRepository
from canonical.ext.oauth.bases import AuthorizationServerEndpoint
from canonical.ext.oauth.params import AuthorizationRequest
from canonical.ext.oauth.types import URLSafeClientID
from canonical.ext.oauth.protocols import IRegisteredClient
from canonical.ext.oauth.clusterclient import ClusterClient


class AuthorizeEndpoint(AuthorizationServerEndpoint):
    cache_ttl: int = 3600
    instance: ClusterClient
    params: AuthorizationRequest
    path = '/authorize'
    response_model = None
    resources: ResourceRepository
    status_code = 302
    summary = 'Authorize Endpoint'

    @property
    def client(self) -> IRegisteredClient:
        assert self._client is not None
        return self._client

    async def discover(self, client: Any):
        pass

    async def get(self) -> fastapi.Response:
        raise NotImplementedError

    async def get_client(self) -> IRegisteredClient:
        if not isinstance(self.params.client_id, URLSafeClientID):
            raise NotImplementedError
        client = await self.cache.get(
            key=self.params.client_id.cache_key,
            decoder=self.params.client_id.model
        )
        if client is None:
            client = await self.resources.get(self.params.client_id.ref)
            await self.cache.set(
                key=self.params.client_id.cache_key,
                value=client,
                encoder=self.params.client_id.model,
                ttl=self.cache_ttl
            )
        self.instance = cast(ClusterClient, client)
        return cast(IRegisteredClient, getattr(client, 'spec'))

    async def setup(self):
        await super().setup()
        await self.discover(self.client)
        await self.validate_client(self.client, self.params)

    async def validate_client(self, client: IRegisteredClient, params: AuthorizationRequest):
        params.validate_client(client)