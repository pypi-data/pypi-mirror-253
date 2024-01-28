# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import urllib.parse
from typing import Any

from .stringtype import StringType


class HTTPResourceLocator(StringType):
    max_length = 2048

    @classmethod
    def validate(cls, v: str, _: Any = None):
        p = urllib.parse.urlparse(v)
        if p.scheme not in {'http', 'https'}:
            raise ValueError(f"Not a valid URL: {v[:128]}")
        return cls(v)