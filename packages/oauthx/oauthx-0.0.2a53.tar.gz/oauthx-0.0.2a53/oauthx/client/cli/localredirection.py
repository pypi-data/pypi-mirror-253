# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import threading
import time
from typing import Any

import fastapi
import uvicorn

from oauthx.lib.models import ClientAuthorizationState
from oauthx.lib.models import ObtainedGrant
from oauthx.client.models import Client


class LocalRedirection(uvicorn.Server):
    grant: ObtainedGrant | None = None

    def __init__(
        self,
        client: Client,
        state: ClientAuthorizationState,
        port: int
    ):
        self.client = client
        self.state = state
        self.port = port
        self.app = fastapi.FastAPI()
        self.app.add_api_route('/', self.callback, methods=['GET'])
        self.config = uvicorn.Config(
            app=self.app,
            port=self.port,
            access_log=False,
            log_level='error',
        )
        self.event = threading.Event()
        super().__init__(self.config)

    async def callback(self, request: fastapi.Request) -> fastapi.Response:
        self.event.set()
        self.result = await self.client.on_redirected(
            state=self.state,
            params=dict(request.query_params)
        )
        if self.result.is_error():
            return fastapi.responses.PlainTextResponse("An error occurred.")
        self.grant = await self.client.authorization_code(self.result, self.state)
        return fastapi.responses.PlainTextResponse("Hello world!")

    def install_signal_handlers(self):
        pass

    def raise_for_status(self):
        self.result.raise_for_status()

    def __enter__(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
        while not self.started:
            time.sleep(1e-3)
        return self

    def __exit__(self, cls: type[Exception], *args: Any):
        self.event.wait()
        self.should_exit = True
        self.thread.join()
        if cls:
            raise NotImplementedError
