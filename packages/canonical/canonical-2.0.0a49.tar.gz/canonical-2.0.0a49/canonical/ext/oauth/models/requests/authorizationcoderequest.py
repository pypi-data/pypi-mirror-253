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

from canonical.ext.oauth.types import AuthenticationMethod
from canonical.ext.oauth.types import RedirectURI
from .grantmodel import GrantModel


class AuthorizationCodeRequest(GrantModel):
    grant_type: Literal['authorization_code'] = pydantic.Field(
        default='authorization_code',
        title="Grant Type",
        description=(
            "Value **must** be set to `authorization_code`."
        )
    )

    code: str = pydantic.Field(
        default=...,
        title="Authorization Code",
        description=(
            "The authorization code received from the authorization server."
        )
    )

    redirect_uri: RedirectURI | None = pydantic.Field(
        default=None,
        title="Redirect URI",
        description=(
            "Required, if the `redirect_uri` parameter was included in the "
            "authorization request, and their values **must** be identical."
        )
    )

    client_id: str | None = pydantic.Field(
        default=None,
        title="Client ID",
        description=(
            "Required, if the client is not authenticating with "
            "the authorization serve"
        )
    )

    def identify(self, client_id: str) -> None:
        self.client_id = client_id

    def set_client_secret(self, mode: AuthenticationMethod, secret: str) -> None:
        if mode != 'client_secret_post':
            raise NotImplementedError
        self.client_secret = secret