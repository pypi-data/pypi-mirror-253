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


@pytest.mark.asyncio
@pytest.mark.parametrize("redirect_uri", [
    f'http://127.0.0.1:23390/{os.urandom(16).hex()}'
])
async def test_invalid_redirect_uri_does_not_redirect(
    redirect_uri: str,
    authorize_request: AuthorizeFactory
):
    await authorize_request(
        redirect_uri=redirect_uri,
        status_code=403
    )