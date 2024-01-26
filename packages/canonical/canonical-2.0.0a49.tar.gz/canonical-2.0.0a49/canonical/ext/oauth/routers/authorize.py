# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

from canonical.ext.fastapi import params
from canonical.ext.fastapi import verbs
from ..clusterclient import ClusterClient
from ..clusterprovider import ClusterProvider
from ..models.requests import AuthorizationRequest
from ..protocols import IRegisteredClient
from ..resources import AuthorizationStateBuilder


class Authorize(verbs.Get[ClusterClient]):
    detail = True
    existing = True
    include_in_schema = True
    path = '/authorize'
    status_code = 302
    verb = 'authorize'

    def get_endpoint_summary(self) -> str:
        return (
            "Authorization endpoint"
        )

    def get_response_description(self) -> str:
        return (
            "Succesful authorization by the resource owner."
        )

    def validate_request(
        self,
        client: IRegisteredClient,
        params: AuthorizationRequest
    ) -> None:
        if not client.allows_redirect(params.redirect_uri):
            self.fail(403, f"Redirection to {params.redirect_uri} is not allowed.")
        if not client.allows_response_type(params.response_type):
            self.fail(403, (
                    "The response_type parameter must match the default response type "
                    "specified by the local client."
                )
            )

    async def handle(
        self,
        http: params.HTTPClient,
        request: fastapi.Request,
        repo: params.ResourceRepository,
        obj: ClusterClient,
        builder: AuthorizationStateBuilder = fastapi.Depends(AuthorizationStateBuilder),
        params: AuthorizationRequest = AuthorizationRequest.as_query()
    ):
        if params.client_id != obj.name:
            self.fail(403, "The client_id parameter must match the client specified in the path.")
        self.validate_request(obj.spec, params)
        provider = await repo.get(
            obj.spec.provider.with_model(ClusterProvider),
            model=ClusterProvider
        )
        meta = await provider.discover(http)
        assert meta.authorization_endpoint is not None
        assert meta.token_endpoint is not None

        builder.with_authorization_endpoint(meta.authorization_endpoint)
        builder.with_token_endpoint(meta.token_endpoint)
        builder.own(obj, controller=True)
        builder.proxy(str(request.url_for('oauth2.callback')))
        builder.with_client(obj.spec)
        builder.with_params(params)
        if not params.redirect_uri:
            builder.with_redirect_uri(obj.spec.default_redirect())
        state = await builder
        await repo.persist(type(state), state)
        return fastapi.responses.RedirectResponse(
            status_code=302,
            url=state.proxy(params)
        )