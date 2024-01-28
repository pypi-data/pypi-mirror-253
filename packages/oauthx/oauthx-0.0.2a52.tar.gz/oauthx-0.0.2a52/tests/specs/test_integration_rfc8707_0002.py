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
@pytest.mark.parametrize("resource", [
    ['https://example.com', 'https://example.net'],
    'https://example.com',
])
async def test_access_token_must_be_restricted_to_the_audience(
    agent: httpx.AsyncClient,
    client: ConsumingClient,
    resource: str | list[str],
    authorize_request: AuthorizeFactory
):
    _, response, state = await authorize_request(resource=resource)
    assert not response.is_error()
    grant = await client.authorization_code(response, state, http=agent)
    jws = jose.parse(grant.access_token)
    at = jws.payload(RFC9068AccessToken.model_validate)
    if not isinstance(resource, list):
        resource = [resource]
    assert set(at.aud or []) == set(resource)


@pytest.mark.parametrize("resource", [
    'https://example.com',
    ['https://example.com', 'https://example.net']
])
@pytest.mark.asyncio
async def test_can_not_obtain_token_with_non_consented_resources(
    agent: httpx.AsyncClient,
    client: ConsumingClient,
    resource: str | list[str],
    authorize_request: AuthorizeFactory
):
    _, params, state = await authorize_request(resource=resource)
    assert not params.is_error()
    try:
        await client.authorization_code(
            params=params,
            state=state,
            resources='https://www.foo.com',
            http=agent
        )
        pytest.fail()
    except Error as exc:
        assert exc.error == 'invalid_target'


@pytest.mark.parametrize("resource", [
    'https://example.com',
    ['https://example.com', 'https://example.net']
])
@pytest.mark.asyncio
async def test_can_not_refresh_token_with_non_consented_resources(
    agent: httpx.AsyncClient,
    client: ConsumingClient,
    resource: str | list[str],
    authorize_request: AuthorizeFactory
):
    _, params, state = await authorize_request(resource=resource, scope={'offline_access'})
    assert not params.is_error()
    obtained = await client.authorization_code(
        params=params,
        state=state,
        http=agent
    )
    assert obtained.refresh_token is not None
    try:
        await client.refresh(
            obtained.refresh_token,
            resource='https://example.org',
            http=agent
        )
        pytest.fail()
    except Error as exc:
        assert exc.error == 'invalid_target'