# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from .responsemodel import ResponseModel


class Error(ResponseModel):
    error: str = pydantic.Field(
        default=...,
        title="Error Code",
        description=(
            "Error code received from the authorization server."
        )
    )

    def is_error(self) -> bool:
        return True