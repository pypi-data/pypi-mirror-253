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


@pytest.mark.skip("Not implemented")
@pytest.mark.asyncio
@pytest.mark.parametrize("redirect_uri", [
    "http://localhost", # May not be localhost
    "http://example.com", # Must use TLS
])
async def test_invalid_redirect_uri_does_not_redirect(
    http: httpx.AsyncClient,
    client: oauthx.Client,
    redirect_uri: str,
):
    response = await http.get(
        url='https://127.0.0.1/oauth/v2/authorize',
        params={
            'client_id': client.client_id,
            'response_type': 'code',
            'redirect_uri': redirect_uri
        }
    )
    assert response.status_code == 403