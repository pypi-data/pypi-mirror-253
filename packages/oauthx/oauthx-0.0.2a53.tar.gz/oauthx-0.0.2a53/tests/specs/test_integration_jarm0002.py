# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os

import pytest

from .types import AuthorizeFactory


@pytest.fixture
def response_mode() -> str:
    return 'query.jwt'


@pytest.mark.asyncio
async def test_jarm_response_contains_error_parameters(authorize_request: AuthorizeFactory):
    # Use an invalid scope to trigger an error.
    _, response, _ = await authorize_request(
        scope=bytes.hex(os.urandom(16)),
        expect_error='invalid_scope',
        expect_params={'response'}
    )
    assert response.is_error()