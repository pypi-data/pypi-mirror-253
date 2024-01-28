# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os
from typing import Any

import httpx
import pytest
from aiopki.ext import jose
from aiopki.types import ISigner

import oauthx
from .types import AuthorizeFactory


async def validate(
    agent: httpx.AsyncClient,
    http: httpx.AsyncClient,
    client: oauthx.Client,
    authorize_request: AuthorizeFactory,
    code: str,
    error: str
):
    _, params, state = await authorize_request(response_type='code')
    try:
        params.code = code # type: ignore
        await client.authorization_code(params, state, http=http)
        assert False
    except oauthx.Error as exc:
        assert exc.error == error


@pytest.mark.asyncio
@pytest.mark.parametrize("error,code", [
    ('invalid_request', os.urandom(16).hex()),
])
async def test_validate_authorization_code(
    agent: httpx.AsyncClient,
    http: httpx.AsyncClient,
    client: oauthx.Client,
    authorize_request: AuthorizeFactory,
    error: str,
    code: str
):
    await validate(agent, http, client, authorize_request, code, error)


@pytest.mark.asyncio
@pytest.mark.parametrize("params", [
    {'aut': 1, 'mac': '', 'sub': '1'}
])
async def test_validate_authorization_code_signature(
    agent: httpx.AsyncClient,
    http: httpx.AsyncClient,
    client: oauthx.Client,
    authorize_request: AuthorizeFactory,
    random_signer: ISigner,
    params: dict[str, Any]
):
    params.setdefault('client_id', str(client.client_id))
    jws = jose.jws(params)
    await jws.sign(random_signer.default_algorithm(), random_signer)
    await validate(agent, http, client, authorize_request, jws.encode(bytes.decode), 'invalid_grant')


@pytest.mark.asyncio
@pytest.mark.parametrize("params", [
    {},
])
async def test_validate_authorization_code_payload(
    agent: httpx.AsyncClient,
    http: httpx.AsyncClient,
    client: oauthx.Client,
    authorize_request: AuthorizeFactory,
    random_signer: ISigner,
    params: dict[str, Any]
):
    params.setdefault('client_id', str(client.client_id))
    jws = jose.jws(params)
    await jws.sign(random_signer.default_algorithm(), random_signer)
    await validate(agent, http, client, authorize_request, jws.encode(bytes.decode), 'invalid_grant')


@pytest.mark.asyncio
@pytest.mark.parametrize("params", [
    {'aut': 1, 'mac': '', 'sub': '1'}
])
async def test_validate_authorization_code_mac(
    agent: httpx.AsyncClient,
    http: httpx.AsyncClient,
    client: oauthx.Client,
    authorize_request: AuthorizeFactory,
    signer: ISigner,
    params: dict[str, Any]
):
    params.setdefault('client_id', str(client.client_id))
    jws = jose.jws(params)
    await jws.sign(signer.default_algorithm(), signer)
    await validate(agent, http, client, authorize_request, jws.encode(bytes.decode), 'invalid_grant')