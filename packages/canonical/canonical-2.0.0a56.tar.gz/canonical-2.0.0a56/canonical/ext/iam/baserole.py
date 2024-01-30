# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from canonical.ext.api import APIResourceModel
from .types import Permission
from .types import PermissionWildcard


class BaseRole(APIResourceModel[str], abstract=True):
    permissions: set[PermissionWildcard | Permission] = pydantic.Field(
        default_factory=set,
        description=(
            "The set of permissions granted to this role. May contain "
            "wildcard permissions."
        )
    )

    def is_global(self) -> bool:
        return self.kind == 'ClusterRole'