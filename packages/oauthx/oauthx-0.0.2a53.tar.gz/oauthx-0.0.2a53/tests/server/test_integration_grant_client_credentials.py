# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import httpx
import pytest

from oauthx.models import Client


@pytest.fixture(scope='function')
def grant_types() -> list[str]:
    return ['client_credentials']


@pytest.mark.asyncio
async def test_client_credentials(
    agent: httpx.AsyncClient,
    http: httpx.AsyncClient,
    client: Client
):
    await client.client_credentials({'email'}, http)