# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.lib.protocols import BaseSettings


class ClientSettings(BaseSettings):
    splash_image: str = 'https://static.webiam.id/shared/splash.jpg'

    def get_splash_image_url(self) -> str:
        return self.splash_image