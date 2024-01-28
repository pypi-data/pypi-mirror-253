# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .useragentexception import UserAgentException


class InvalidAuthorizationResponse(UserAgentException):
    __module__: str = 'oauthx.types'
    template_name: str = 'oauthx/errors/invalid-redirect-parameters.html.j2'
    
    def get_template_names(self) -> list[str] | str:
        return [
            f'oauthx/errors/upstream.{self.error}.html.j2',
            'oauthx/errors/upstream.html.j2',
            self.template_name
        ]