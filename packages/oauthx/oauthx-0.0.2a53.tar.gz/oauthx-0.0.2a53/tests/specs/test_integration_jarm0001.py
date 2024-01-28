# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pytest

from .types import AuthorizeFactory


@pytest.fixture
def response_mode() -> str:
    return 'query.jwt'


@pytest.mark.asyncio
@pytest.mark.parametrize("claim", ["iss", "aud", "exp"])
async def test_jarm_response_contains_required_claims(
    claim: str,
    authorize_request: AuthorizeFactory
):
    _, response, _ = await authorize_request(
        expect_params={'response'}
    )
    assert getattr(response, claim) is not None