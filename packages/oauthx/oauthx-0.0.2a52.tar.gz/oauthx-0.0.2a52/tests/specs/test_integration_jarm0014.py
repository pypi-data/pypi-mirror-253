# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pytest
import pytest_asyncio
from aiopki.lib import JSONWebKey
from aiopki.lib import JSONWebKeySet
from aiopki.ext.jose import JWE

from oauthx.lib import JARMToken
from .types import AuthorizeFactory


@pytest_asyncio.fixture(scope='function') # type: ignore
async def client_credential(
    rsa_enc: JSONWebKey
) -> Any:
    return JSONWebKeySet(keys=[rsa_enc])


@pytest.fixture(scope='function')
def client_params() -> dict[str, Any]:
    return {
        'authorization_encrypted_response_alg': 'RSA-OAEP-256',
        'authorization_encrypted_response_enc': 'A256GCM'
    }


@pytest.fixture
def response_mode() -> str:
    return 'query.jwt'


@pytest.mark.asyncio
async def test_jarm_uses_client_preferences(authorize_request: AuthorizeFactory):
    raw, *_ = await authorize_request()
    assert isinstance(raw.root, JARMToken)
    assert isinstance(raw.root.response.root, JWE)
    assert raw.root.response.root.alg is not None
    assert raw.root.response.root.enc is not None
    assert raw.root.response.root.alg.name == 'RSA-OAEP-256'
    assert raw.root.response.root.enc.name == 'A256GCM'