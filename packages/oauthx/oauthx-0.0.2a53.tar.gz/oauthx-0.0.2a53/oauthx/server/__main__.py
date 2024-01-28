# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi
import uvicorn

from .ref import LoginRequestHandler
from .oidcrouter import OIDCRouter


app: fastapi.FastAPI = fastapi.FastAPI()
app.include_router(
    router=OIDCRouter.from_config(
        app=app,
        config='etc/oidc.conf',
        login_handler=LoginRequestHandler
    )
)


if __name__ == '__main__':
    uvicorn.run('oauthx.server.__main__:app', reload=True) # type: ignore