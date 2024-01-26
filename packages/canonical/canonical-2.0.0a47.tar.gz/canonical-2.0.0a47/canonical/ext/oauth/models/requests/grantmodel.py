# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from .requestmodel import RequestModel


class GrantModel(RequestModel):
    client_secret: str | None = pydantic.Field(
        default=None,
        title="Client Secret",
        description=(
            "Required if the client is authenticating with the "
            "`client_secret_post` method. The client may omit "
            "the parameter if the client secret is an empty "
            "string"
        )
    )