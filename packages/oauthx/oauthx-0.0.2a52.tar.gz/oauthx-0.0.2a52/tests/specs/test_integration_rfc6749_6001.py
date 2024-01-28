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
from aiopki.ext import jose

from oauthx.client import Client as ConsumingClient
from oauthx.lib import RFC9068AccessToken
from oauthx.lib.exceptions import Error
from .types import AuthorizeFactory


@pytest.fixture(scope='function')
def grant_types() -> list[str]:
    return ['authorization_code', 'refresh_token']


@pytest.fixture(scope='function')
def scope() -> list[str]:
    return ['offline_access', 'email', 'profile']


@pytest.mark.asyncio
async def test_excessive_scope_raises_invalid_scope(
    agent: httpx.AsyncClient,
    client: ConsumingClient,
    authorize_request: AuthorizeFactory
):
    _, response, state = await authorize_request(
        scope={'offline_access', 'email'}
    )
    assert response
    assert state
    grant = await client.authorization_code(response, state, http=agent)
    assert grant.refresh_token is not None
    try:
        await client.refresh(grant.refresh_token, scope={'email', 'profile'}, http=agent)
        assert False
    except Error as exc:
        assert exc.error == 'invalid_scope'


@pytest.mark.asyncio
async def test_omitted_scope_grants_original_scope(
    agent: httpx.AsyncClient,
    client: ConsumingClient,
    authorize_request: AuthorizeFactory
):
    _, response, state = await authorize_request(
        scope={'offline_access', 'email'}
    )
    assert response
    assert state
    grant = await client.authorization_code(response, state, http=agent)
    assert grant.refresh_token is not None
    refreshed = await client.refresh(grant.refresh_token, http=agent)
    jws = jose.parse(refreshed.access_token)
    at = jws.payload(RFC9068AccessToken.model_validate)
    assert set(at.scope) == {'offline_access', 'email'}


@pytest.mark.asyncio
async def test_original_scope_subset(
    agent: httpx.AsyncClient,
    client: ConsumingClient,
    authorize_request: AuthorizeFactory
):
    _, response, state = await authorize_request(
        scope={'offline_access', 'email'}
    )
    assert response
    assert state
    grant = await client.authorization_code(response, state, http=agent)
    assert grant.refresh_token is not None
    refreshed = await client.refresh(grant.refresh_token, scope={'email'}, http=agent)
    jws = jose.parse(refreshed.access_token)
    at = jws.payload(RFC9068AccessToken.model_validate)
    assert set(at.scope) == {'email'}