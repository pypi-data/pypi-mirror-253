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

from oauthx.client import  Client
from .types import AuthorizeFactory



@pytest.mark.skip("Needs implementation of SQL storage.")
@pytest.mark.asyncio
@pytest.mark.parametrize("scope", [
    {"email"}
])
async def test_userinfo_contains_scope_claims(
    authorize_request: AuthorizeFactory,
    agent: httpx.AsyncClient,
    client: Client,
    scope: set[str]
):
    _, response, state = await authorize_request(scope=scope)
    grant = await client.authorization_code(response, state, http=agent)
    response = await grant.access_token.userinfo(client, http=agent)
    assert hasattr(response, 'sub')


@pytest.mark.skip("Needs implementation of SQL storage.")
@pytest.mark.asyncio
async def test_userinfo_uses_get(
    authorize_request: AuthorizeFactory,
    agent: httpx.AsyncClient,
    client: Client
):
    _, response, state = await authorize_request()
    grant = await client.authorization_code(response, state, http=agent)
    await grant.access_token.userinfo(client, http=agent)


@pytest.mark.skip("Needs implementation of SQL storage.")
@pytest.mark.asyncio
async def test_userinfo_contains_sub(
    authorize_request: AuthorizeFactory,
    agent: httpx.AsyncClient,
    client: Client
):
    _, response, state = await authorize_request()
    grant = await client.authorization_code(response, state, http=agent)
    response = await grant.access_token.userinfo(client, http=agent)
    assert hasattr(response, 'sub')