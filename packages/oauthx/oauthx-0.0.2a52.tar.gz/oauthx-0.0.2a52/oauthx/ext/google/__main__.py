# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

import aiopki
import oauthx
from oauthx.lib import MemoryCache
from oauthx.lib.params import ApplicationCache
from oauthx.resource import ResourceRouter
from oauthx.resource.params import RequestSubject


aiopki.install_backend('aiopki.ext.azure')
aiopki.install_backend('aiopki.ext.google')


app: fastapi.FastAPI = oauthx.create_server(
    config='etc/oidc.conf',
    dependencies=[
        ApplicationCache(MemoryCache),
    ]
)


router = ResourceRouter(
    issuers={"https://checkpoint.localhost.webiam.id"},
    scope={'telegram'},
    audience='any'
)


@router.get('/')
async def f(subject: RequestSubject):
    return subject.model_dump()


app.include_router(router=router)