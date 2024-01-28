# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import secrets
from typing import Any

import httpx
import pytest
import pytest_asyncio

from aiopki.ext.jose import JWKS
from oauthx.models import Client


@pytest.fixture(scope='function')
def grant_types() -> list[str]:
    return ['urn:ietf:params:oauth:grant-type:jwt-bearer']


@pytest.fixture(scope='function')
def response_types() -> list[str]:
    return ['none']


@pytest_asyncio.fixture(scope='function') # type: ignore
async def client_credential() -> Any:
    return JWKS.model_validate({
        'keys': [{
            'kty': 'oct',
            'use': 'sig',
            'alg': 'HS256',
            'k': secrets.token_urlsafe(32)
        }]
    })


@pytest.mark.asyncio
async def test_jwt_bearer(
    agent: httpx.AsyncClient,
    http: httpx.AsyncClient,
    client: Client
):
    # Authorize the client
    state = await client.authorize(response_type='none')
    response = await agent.get(state.authorize_url, follow_redirects=False)
    assert response.status_code == 302, response.content
    await client.jwt('1', http=http)