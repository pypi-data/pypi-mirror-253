# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import json
import os
import pathlib
import urllib.parse
from typing import Any
from typing import Awaitable
from typing import Callable

import fastapi
import httpx
import pytest
import pytest_asyncio
import aiopki
import yaml
from aiopki.lib import JSONWebKey
from aiopki.utils import b64encode

from oauthx.client import Client as ConsumingClient
from oauthx.lib import AuthorizationResponse
from oauthx.lib import ClientAuthorizationState
from oauthx.lib import Error
from oauthx.lib import RedirectionParameters
from oauthx.server.config import Config
from oauthx.server.params.masker import _Masker as Masker # type: ignore
from oauthx.server import OIDCRouter
from oauthx.server.ref import Storage
from oauthx.server.models import ObjectFactory
from oauthx.server.models import ResourceOwner
from oauthx.server.models import Session
from oauthx.server.request import Request
from oauthx.server.models import Client as ServerClient


aiopki.install_backend('aiopki.ext.cryptography')


@pytest_asyncio.fixture(scope='function') # type: ignore
async def agent(app: fastapi.FastAPI, session_cookie: str):
    params = {
        'cookies': {'sessionid':  session_cookie}
    }
    async with httpx.AsyncClient(app=app, **params) as client: # type: ignore
        yield client


@pytest_asyncio.fixture # type: ignore
async def app(
    config: Config,
    storage_class: type[Storage]
):
    app = fastapi.FastAPI()
    client = httpx.AsyncClient(app=app)
    await client.__aenter__()
    router = OIDCRouter.from_config(
        app=app,
        config=config,
        prefix='/oauth/v2',
        http=client
    )
    app.include_router(router)
    yield app
    await client.__aexit__(None, None, None)



@pytest_asyncio.fixture(scope='function') # type: ignore
async def authorize_request(
    client: ConsumingClient,
    agent: httpx.AsyncClient,
) -> Callable[..., Awaitable[tuple[AuthorizationResponse | None, Error| RedirectionParameters | None, ClientAuthorizationState | None]]]:
    #await client.discover(agent)

    async def f(
        *,
        status_code: int = 302,
        expect_error: str | None = None,
        expect_params: set[str] = set(),
        expect_media_type: str | None = None,
        **kwargs: Any
    ) -> tuple[AuthorizationResponse | None, Error| RedirectionParameters  | None, ClientAuthorizationState | None]:
        state = await client.authorize(
            http=agent,
            state_class=ClientAuthorizationState,
            **kwargs
        )
        response = await agent.get(state.authorize_url)
        assert response.status_code == status_code,\
            f"{response.headers.get('X-Error')}: {response.headers.get('X-Error-Description')}\n"\
            + '\n'.join([f'{k}: {v}' for k, v in sorted(response.headers.items(), key=lambda x: x[0])])
        if 300 <= status_code < 400:
            assert 'Location' in response.headers
            assert 'X-Error' not in response.headers or expect_error,\
                f"{response.headers.get('X-Error')}: {response.headers.get('X-Error-Description')}"
            assert 'X-Error' in response.headers or not expect_error,\
                f"{response.headers.get('X-Error')}: {response.headers.get('X-Error-Description')}"
            assert not expect_media_type or response.headers.get('Content-Type') == expect_media_type
            try:
                loc: str = response.headers['Location']
                p = urllib.parse.urlparse(loc)
                q = dict(urllib.parse.parse_qsl(p.query))
                assert set(q.keys()) == expect_params or not expect_params,\
                    f'Missing parameters: {str.join(",", expect_params - set(q.keys()))}'
                return AuthorizationResponse.model_validate(q), await client.on_redirected(state, q), state
            except json.JSONDecodeError:
                for name, value in response.headers.items():
                    print(f'{name}: {value}')
                print(response.content)
                raise

        return None, None, None

    return f


@pytest_asyncio.fixture(scope='function') # type: ignore
async def client(
    client_credential: Any,
    response_mode: str,
    client_params: dict[str, Any]
) -> ConsumingClient:
    return ConsumingClient.model_validate({
        'provider': 'http://127.0.0.1',
        'client_id': 'foo',
        'credential': client_credential,
        'response_mode': response_mode,
        **client_params
    })


@pytest_asyncio.fixture(scope='function') # type: ignore
async def client_credential() -> Any:
    return None


@pytest_asyncio.fixture(scope='function') # type: ignore
async def client_params() -> dict[str, Any]:
    return {}


@pytest.fixture(scope='function')
def config(config_data: dict[str, Any]) -> Config:
    return Config.model_validate(config_data)


@pytest.fixture(scope='session')
def config_data() -> dict[str, Any]:
    data = yaml.safe_load(open(pathlib.Path(__file__).parent.parent.joinpath('oidc.conf'), 'r').read())  # type: ignore
    data['issuer']['id'] = 'http://127.0.0.1'  # type: ignore
    return data  # type: ignore


@pytest_asyncio.fixture(scope='function') # type: ignore
async def dek(config: Config) -> aiopki.CryptoKeyType:
    return await config.storage.encryption_key


@pytest.fixture(scope='function')
def grant_types() -> list[str]:
    return ['authorization_code']


@pytest_asyncio.fixture(scope='function') # type: ignore
async def http(app: fastapi.FastAPI):
    async with httpx.AsyncClient(app=app) as client: # type: ignore
        yield client


@pytest.fixture
def redirect_uris() -> list[str]:
    return ['http://127.0.0.1:23390']


@pytest.fixture(scope='function')
def response_mode() -> str:
    return 'query'


@pytest.fixture(scope='function')
def response_types() -> list[str]:
    return ['code']


@pytest.fixture(scope='function')
def scope() -> list[str]:
    return ['email']


@pytest_asyncio.fixture # type: ignore
async def session_signer(config: Config) -> Any:
    return await config.ui.session_key # type: ignore


@pytest_asyncio.fixture # type: ignore
async def session_cookie(session_signer: aiopki.CryptoKeyType) -> str:
    session = Session.new()
    session.sub = '1'
    return await Request.sign_session(session, session_signer) # type: ignore


@pytest_asyncio.fixture(scope='function') # type: ignore
async def signer(config: Config) -> aiopki.CryptoKeyType:
    await config.issuer.signing_key
    return config.issuer.signing_key


@pytest_asyncio.fixture(autouse=True) # type: ignore
async def storage(
    config: Config,
    storage_class: type[Storage],
    dek: JSONWebKey
) -> Storage:
    storage = storage_class(config=config, key=dek)
    factory = ObjectFactory(
        issuer=config.issuer.id,
        storage=storage,
        masker=Masker(
            key=JSONWebKey.model_validate({ # type: ignore
                'kty': 'oct',
                'use': 'sig',
                'alg': 'HS384',
                'k': b64encode(os.urandom(32))
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
    subject = await factory.subject(pk=1, use='personal')
    await subject.encrypt_keys(dek)
    await storage.persist(subject)
    return storage


@pytest.fixture(scope='function')
def storage_class() -> type[Storage]:
    return type('Storage', (Storage, ), {'objects': {}})


@pytest_asyncio.fixture(scope='function', autouse=True) # type: ignore
async def server_client(
    client_credential: Any,
    http: httpx.AsyncClient,
    storage: Storage,
    grant_types: list[str],
    redirect_uris: list[str],
    response_types: list[str],
    response_mode: str,
    scope: list[str],
    client_params: dict[str, Any]
) -> ServerClient:
    client = ServerClient.model_validate({
        'client_id': 'foo',
        'client_name': 'foo',
        'grant_types': grant_types,
        'scope': scope,
        'redirect_uris': redirect_uris,
        'response_modes': [response_mode],
        'response_types': response_types,
        'credential': client_credential,
        'access_tokens': {
            'claims': ['email'],
            'ttl': 600
        },
        **client_params
    })
    await client.persist(storage)
    return client