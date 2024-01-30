# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any


class ITemplateService:
    __module__: str = 'canonical.protocols'

    async def render_template(
        self,
        templates: list[str] | str,
        context: dict[str, Any]
    ) -> str:
        ...