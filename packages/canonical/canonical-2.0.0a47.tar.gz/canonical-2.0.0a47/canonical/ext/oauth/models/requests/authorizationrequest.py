# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import secrets
from typing import Any

from canonical.ext.fastapi.mixins import QueryModelMixin
from canonical.lib import FormDataModel

from ...types import ResponseTypeLiteral
from ...types import RedirectURI


class AuthorizationRequest(FormDataModel, QueryModelMixin):
    model_config = {'extra': 'forbid'}
    client_id: str
    response_type: ResponseTypeLiteral
    redirect_uri: RedirectURI | None = None
    state: str | None = None

    @classmethod
    def new(cls, **kwargs: Any):
        kwargs.setdefault('state', secrets.token_hex(32))
        return cls.model_validate(kwargs)

    def proxy(self, endpoint: str, client_id: str, redirect_uri: str, state: str) -> str:
        """Proxies the authorization request. Return a string containing the
        full authorization URL, with the `client_id`,  `redirect_uri` and
        `state` parameters replaced by the given values.
        """
        clone = self.model_validate({
            **self.model_dump(mode='json'),
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'state': state
        })
        return str(clone.with_endpoint('GET', endpoint))
        