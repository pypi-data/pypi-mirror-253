# Copyright (C) 2023-2024 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import secrets
from typing import Any

import fastapi

from canonical.ext.api.bases import BaseResourceBuilder
from canonical.ext.fastapi.params import ResourceRepository
from canonical.ext.oauth.models import AuthorizationRequest
from canonical.ext.oauth.protocols import IRegisteredClient
from .authorizationstate import AuthorizationState


class AuthorizationStateBuilder(BaseResourceBuilder[AuthorizationState]):
    client: IRegisteredClient | None = None
    mode: str
    model = AuthorizationState

    def __init__(self, request: fastapi.Request, repo: ResourceRepository):
        super().__init__(repo)
        self.request = request
        self.mode = 'proxy'

    def get_model_input(self) -> dict[str, Any]:
        return {
            **super().get_model_input(),
            'status': {
                'changed': self.now,
                'version': 1,
                'message': '',
                'current': 'Created'
            }
        }

    def proxy(self, callback_uri: str):
        self.mode = self.spec['redirect_mode'] = 'proxy'
        self.spec['proxy_redirection_endpoint'] = callback_uri

    def with_authorization_endpoint(self, url: str):
        self.spec['authorization_endpoint'] = url

    def with_client(self, client: IRegisteredClient):
        self.spec['client_id'] = client.id

    def with_issuer(self, issuer: str):
        self.spec['issuer'] = issuer

    def with_params(self, params: AuthorizationRequest, **override: Any):
        self.spec['params'] = params

    def with_redirect_uri(self, uri: str):
        self.spec['redirect_uri'] = uri

    def with_token_endpoint(self, url: str):
        self.spec['token_endpoint'] = url

    async def prepare(self):
        assert self.mode == 'proxy'
        if self.mode == 'proxy':
            self.metadata['name'] = secrets.token_hex(32)