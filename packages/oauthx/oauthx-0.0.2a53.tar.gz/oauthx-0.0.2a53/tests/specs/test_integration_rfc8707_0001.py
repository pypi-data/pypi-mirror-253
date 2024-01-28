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


@pytest.mark.asyncio
@pytest.mark.parametrize("resource", [
    'foo/bar/baz',
    ['foo/bar/baz'],
    ['foo/bar/baz', 'baz/bar/foo']
])
async def test_resource_must_be_absolute_uri(
    resource: str | list[str],
    authorize_request: AuthorizeFactory
):
    _, response, _ = await authorize_request(
        resource=resource,
        expect_error='invalid_target',
        expect_status=302
    )
    assert response.is_error()