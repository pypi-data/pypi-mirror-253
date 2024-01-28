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

from oauthx.client import Client as ConsumingClient
from .types import AuthorizeFactory


@pytest.fixture(scope='function')
def scope() -> list[str]:
    return ['offline_access']


@pytest.mark.asyncio
async def test_refresh_token_is_not_issued_without_offline_access(
    agent: httpx.AsyncClient,
    client: ConsumingClient,
    authorize_request: AuthorizeFactory
):
    _, response, state = await authorize_request()
    assert response
    assert state
    grant = await client.authorization_code(response, state, http=agent)
    assert grant.refresh_token is None


@pytest.mark.asyncio
async def test_refresh_token_is_issued_with_offline_access(
    agent: httpx.AsyncClient,
    client: ConsumingClient,
    authorize_request: AuthorizeFactory
):
    _, response, state = await authorize_request(
        scope={'offline_access'}
    )
    assert response
    assert state
    grant = await client.authorization_code(response, state, http=agent)
    assert grant.refresh_token is not None