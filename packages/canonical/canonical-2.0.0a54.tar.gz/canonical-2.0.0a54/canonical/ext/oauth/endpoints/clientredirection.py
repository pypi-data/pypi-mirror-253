# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from canonical.ext.oauth.bases import AuthorizationServerEndpoint
from canonical.ext.oauth.params import AuthorizationResponse
from canonical.ext.oauth.params import RedirectedState
from .useragentroutehandler import UserAgentRouteHandler


class ClientRedirectionEndpoint(AuthorizationServerEndpoint):
    cache_ttl: int = 3600
    name = 'oauth2.callback'
    params: AuthorizationResponse
    path = '/callback'
    route_class = UserAgentRouteHandler
    response_model = None
    status_code = 302
    state: RedirectedState
    summary = 'Redirection Endpoint'

    async def get(self):
        print(self.params.model_dump_json(indent=2))

    async def setup(self):
        raise Exception(self.state)