# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pytest

import oauthx
from .types import AuthorizeFactory


@pytest.fixture(scope='function')
def grant_types() -> list[str]:
    return []


@pytest.mark.asyncio
async def test_client_must_allow_authorization_code(
    client: oauthx.Client,
    authorize_request: AuthorizeFactory
):
    _, params, _ = await authorize_request(
        status_code=302,
        expect_error='unauthorized_client',
        response_type='code'
    )
    assert params.is_error()
    assert params.error == 'unauthorized_client'