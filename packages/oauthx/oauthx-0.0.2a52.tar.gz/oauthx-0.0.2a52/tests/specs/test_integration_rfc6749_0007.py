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

import oauthx


@pytest.fixture
def grant_types() -> list[str]:
    return []


@pytest.fixture
def redirect_uris() -> list[str]:
    return []


@pytest.mark.asyncio
async def test_missing_redirect_uri_does_not_redirect(
    agent: httpx.AsyncClient,
    client: oauthx.Client,
):
    response = await agent.get(
        url='https://127.0.0.1/oauth/v2/authorize',
        params={
            'client_id': client.client_id,
            'response_type': 'code',
        }
    )
    assert response.status_code == 400, response.headers