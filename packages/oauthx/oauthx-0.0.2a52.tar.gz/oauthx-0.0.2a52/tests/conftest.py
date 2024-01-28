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
from aiopki.lib import JSONWebKey
from aiopki.utils import b64encode

from aiopki.lib import JSONWebKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key




@pytest.fixture(scope='function')
def random_signer() -> JSONWebKey:
    return JSONWebKey.model_validate({
        'kty': 'oct',
        'use': 'sig',
        'alg': 'HS384',
        'k': b64encode(os.urandom(32))
    })


@pytest.fixture(scope='session')
def rsa_key() -> RSAPrivateKey:
    return generate_private_key(65537, 2048)


@pytest.fixture(scope='session')
def rsa_enc(rsa_key: RSAPrivateKey) -> JSONWebKey:
    return JSONWebKey.model_validate({
        'use': 'enc',
        'key': rsa_key,
    })