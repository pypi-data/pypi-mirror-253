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
from .types import AuthorizeFactory


@pytest.mark.asyncio
async def test_authorization_code_can_not_be_used_twice(
    http: httpx.AsyncClient,
    client: oauthx.Client,
    authorize_request: AuthorizeFactory
):
    _, params, state = await authorize_request(response_type='code')
    assert str(params.state) == str(state.params.state)
    await client.authorization_code(params, state, http=http)
    try:
        await client.authorization_code(params, state, http=http)
        assert False
    except oauthx.Error as exc:
        assert exc.error == 'invalid_grant'