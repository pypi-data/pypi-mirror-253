# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import NotRequired
from typing import TypedDict

import pydantic

from .base import BaseOperation as Verb
from .command import Command
from .create import Create
from .defaultcreate import DefaultCreate
from .defaultreplace import DefaultReplace
from .exists import Exists
from .get import Get
from .proxy import Proxy
from .replace import Replace
from .retrieve import Retrieve
from .validator import Validator


__all__: list[str] = [
    'Command',
    'Create',
    'DefaultCreate',
    'DefaultReplace',
    'Exists',
    'Get',
    'Proxy',
    'Replace',
    'Retrieve',
    'Validator',
    'Verb'
]


class VerbParameters(TypedDict):
    description: NotRequired[str]
    method: NotRequired[str]
    path: NotRequired[str]
    permissions: NotRequired[set[str]]
    response_model: NotRequired[type[pydantic.BaseModel]]
    summary: NotRequired[str]
    validator: NotRequired[type[Validator[Any]]]