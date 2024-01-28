# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import os
import pathlib
from typing import Any

import fastapi
import httpx
import pytest
import pytest_asyncio
import yaml

import aiopki
from aiopki.ext.jose import JWK
from aiopki.ext.keychain import Keychain
from aiopki.utils import b64encode

from oauthx.server.models import ResourceOwner
from oauthx.server import Masker
from oauthx.server import OIDCRouter
from oauthx.server import ObjectFactory
from oauthx.server.config import Config
from oauthx.server.models import Session
from oauthx.server.ref import Storage
from oauthx.server.request import Request
from oauthx.models import Client
from oauthx.types import IStorage


aiopki.install_backend('aiopki.ext.cryptography')


@pytest.fixture(scope='session')
def config_data() -> dict[str, Any]:
    data = yaml.safe_load(open(pathlib.Path(__file__).parent.joinpath('oidc.conf'), 'r').read())
    data['issuer']['id'] = 'https://127.0.0.1'
    return data


@pytest.fixture(scope='function')
def config(config_data: dict[str, Any]) -> Config:
    return Config.model_validate(config_data)


@pytest.fixture(scope='session')
def dek() -> JWK:
    return JWK.model_validate({
        'kty': 'oct',
        'use': 'enc',
        'alg': 'A256GCM',
        'k': os.environ['CONTENT_ENCRYPTION_KEY']
    })


@pytest_asyncio.fixture # type: ignore
async def session_signer(config: Config) -> Any:
    return await config.ui.session_key # type: ignore


@pytest_asyncio.fixture # type: ignore
async def session_cookie(session_signer: Keychain) -> str:
    session = Session.new()
    session.sub = '1'
    return await Request.sign_session(session, session_signer)


@pytest_asyncio.fixture(scope='function') # type: ignore
async def signer(config: Config) -> Keychain:
    await asyncio.gather(*map(asyncio.ensure_future, config.issuer.signing_keys))
    return await Keychain(keys=config.issuer.signing_keys)


@pytest.fixture(scope='function')
def storage_class() -> type[Storage]:
    return type('Storage', (Storage, ), {'objects': {}})


@pytest_asyncio.fixture(autouse=True) # type: ignore
async def storage(
    config: Config,
    storage_class: type[Storage],
    dek: JWK
) -> Storage:
    storage = storage_class(config=config, key=dek)
    factory = ObjectFactory(
        issuer=config.issuer.id,
        storage=storage,
        masker=Masker(
            key=JWK.model_validate({
                'kty': 'oct',
                'use': 'sig',
                'alg': 'HS384',
                'k': os.environ['SECRET_KEY']
            })
        )
    )
    await storage.persist(
        ResourceOwner.model_validate({
            'client_id': 'default',
            'sub': '1',
            'sector_identifier': 'localhost'
        }),
    )
    subject = await factory.subject(pk=1)
    await subject.encrypt_keys(dek)
    await storage.persist(subject)
    return storage


@pytest_asyncio.fixture # type: ignore
async def app(
    config: Config,
    storage_class: type[Storage]
) -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    router = OIDCRouter.from_config(
        app=app,
        config=config,
        prefix='/oauth/v2',
        storage_class=storage_class
    )
    app.include_router(router)
    return app


@pytest_asyncio.fixture(scope='function') # type: ignore
async def agent(app: fastapi.FastAPI, session_cookie: str):
    params = {
        'cookies': {'sessionid':  session_cookie}
    }
    async with httpx.AsyncClient(app=app, **params) as client:
        yield client


@pytest_asyncio.fixture(scope='function') # type: ignore
async def http(app: fastapi.FastAPI):
    async with httpx.AsyncClient(app=app) as client:
        yield client


@pytest_asyncio.fixture(scope='function') # type: ignore
async def client_credential() -> Any:
    return None


@pytest.fixture(scope='function')
def scope() -> list[str]:
    return ['email']


@pytest.fixture(scope='function')
def grant_types() -> list[str]:
    return ['authorization_code']


@pytest.fixture(scope='function')
def response_mode() -> str:
    return 'query'


@pytest.fixture(scope='function')
def response_types() -> list[str]:
    return ['code']


@pytest_asyncio.fixture(scope='function') # type: ignore
async def client(
    client_credential: Any,
    http: httpx.AsyncClient,
    storage: IStorage,
    grant_types: list[str],
    response_types: list[str],
    scope: list[str]
) -> Client:
    client = Client.model_validate({
        'client_id': 'foo',
        'client_name': 'foo',
        'grant_types': grant_types,
        'scope': scope,
        'redirect_uris': ['http://127.0.0.1:23390'],
        'response_types': response_types,
        'credential': client_credential,
        'access_tokens': {
            'claims': ['email'],
            'ttl': 600
        }
    })
    await client.persist(storage)
    return Client.model_validate({
        'provider': {
            'issuer': 'https://127.0.0.1',
            'authorization_endpoint': 'http://localhost/oauth/v2/authorize',
            'token_endpoint': 'http://localhost/oauth/v2/token',
            'authorization_response_iss_parameter_supported': True
        },
        'client_id': 'foo',
        'credential': client_credential
    })