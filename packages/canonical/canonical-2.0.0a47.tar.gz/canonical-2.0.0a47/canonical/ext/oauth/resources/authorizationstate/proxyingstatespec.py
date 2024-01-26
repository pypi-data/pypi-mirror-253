# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

import pydantic

from canonical.ext.oauth.types import RedirectURI
from .authorizationstatespec import AuthorizationStateSpec


class ProxyingStateSpec(AuthorizationStateSpec[Literal['proxy']]):
    proxy_redirection_endpoint: RedirectURI = pydantic.Field(
        default=...,
        alias='proxyRedirectionEndpoint',
        title="Proxy Redirection Endpoint",
        description=(
            "The redirection endpoint of the intermediate OAuth 2.x/"
            "OpenID Connect proxy."
        )
    )

    def get_redirect_uri(self) -> RedirectURI | None:
        # For proxied requests, the redirect URI that the
        # authorization server has seen is the redirection
        # endpoint of the proxy, and we always include it.
        return self.proxy_redirection_endpoint