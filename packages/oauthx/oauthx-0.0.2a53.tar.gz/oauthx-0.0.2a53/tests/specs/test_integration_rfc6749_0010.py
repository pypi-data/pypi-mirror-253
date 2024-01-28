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

import oauthx
from .types import AuthorizeFactory


@pytest.mark.asyncio
async def test_client_id_must_match(
    client: oauthx.Client,
    authorize_request: AuthorizeFactory
):
    client.client_id = bytes.hex(os.urandom(16))
    await authorize_request(
        response_type='code',
        status_code=400,
        expect_media_type='text/html; charset=utf-8'
    )