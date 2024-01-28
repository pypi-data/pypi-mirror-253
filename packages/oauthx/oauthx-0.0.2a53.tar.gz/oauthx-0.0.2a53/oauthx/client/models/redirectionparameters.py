# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic



class RedirectionParameters(pydantic.BaseModel):
    code: str
    state: str | None = None
    iss: str | None = None

    @property
    def error(self) -> str:
        raise NotImplementedError

    @property
    def error_description(self) -> str:
        raise NotImplementedError

    @property
    def error_uri(self) -> str:
        raise NotImplementedError

    def is_error(self) -> bool:
        return False

    def raise_for_status(self):
        pass