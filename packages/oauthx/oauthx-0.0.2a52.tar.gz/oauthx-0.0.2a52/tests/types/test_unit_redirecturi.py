# Copyright (C) 2021-2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import urllib.parse
from typing import Any

import pydantic
import pytest

from oauthx.types import InvalidRequest
from oauthx.types import RedirectURI


VALID_VALUES: list[str] = [
    "https://google.com/callback",
    "http://127.0.0.1/callback",
    "http://127.0.0.1:8000/callback",
    "http://[::1]/callback",
    "http://[::1]:8000/callback",
    "https://google.com/",
    "http://127.0.0.1/",
    "http://127.0.0.1:8000/",
    "http://[::1]/",
    "http://[::1]:8000/",    
]


INVALID_VALUES: list[str | None] = [
    "invalid",
    None,
    'a' * 2049,
    'http://rp.example.com/callback',
    'http://localhost:8000/callback',
    'https://localhost:8000/callback',
    'https://localhost:8000/callback?foo=bar',
    'https://localhost:8000/callback#fragment',
    'http://1.1.1.1/callback',
    'http://::1',
    'https://::1',
    'http://0:0:0:0:0:0:0:1',
    'https://0:0:0:0:0:0:0:1',
    "urn:ietf:wg:oauth:2.0:oob",
    "urn:ietf:wg:oauth:2.0:oob:auto",
]


class M(pydantic.BaseModel):
    redirect_uri: RedirectURI

    class Config:
        json_encoders: dict[type, Any] = {
            RedirectURI: str
        }


@pytest.mark.parametrize("value", VALID_VALUES)
def test_valid_values(value: Any):
    RedirectURI(value)


@pytest.mark.parametrize("value", VALID_VALUES)
def test_valid_values_model(value: str):
    M.model_validate({'redirect_uri': value})


@pytest.mark.parametrize("value", INVALID_VALUES)
def test_invalid_values(value: Any):
    with pytest.raises(InvalidRequest):
        RedirectURI(value)


@pytest.mark.parametrize("value", INVALID_VALUES)
def test_invalid_values_model(value: str | None):
    if value is None:
        return
    with pytest.raises(pydantic.ValidationError):
        M.model_validate({'redirect_uri': value})


def test_cast_to_string():
    url = RedirectURI('https://rp.example.com')
    assert str(url) == 'https://rp.example.com'


def test_create_redirect_uri():
    url = RedirectURI('https://rp.example.com')
    p = urllib.parse.urlparse(url.redirect(foo='bar'))
    q = dict(urllib.parse.parse_qsl(p.query))
    assert 'foo' in q
    assert q.get('foo') == 'bar'


def test_serialize_model():
    obj = M.model_validate({
        'redirect_uri': 'https://rp.example.com/callback'
    })
    obj.model_dump_json()


@pytest.mark.parametrize("value", [
    "http://[::1]",
    "http://[::1]:8000",
    "http://[0:0:0:0:0:0:0:1]",
    "http://[0:0:0:0:0:0:0:1]:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
])
def test_is_recognized_as_loopback(value: str):
    redirect_uri = RedirectURI(value)
    assert redirect_uri.is_loopback()


@pytest.mark.parametrize("x,y,allowed", [
    ("http://127.0.0.1", "http://127.0.0.1:8000", True),
    ("http://127.0.0.1:6000", "http://127.0.0.1:8000", True),
    ("http://[::1]:6000", "http://[::1]:8000", True),
    ("https://www.example.com/foo", "https://www.example.com/foo", True),
    ("https://www.example.com", "https://www.example.com:8000", False),
    ("https://www.example.com", "https://www.example.com/foo", False),
])
def test_allows_redirect(x: str, y: str, allowed: bool):
    assert RedirectURI(x).can_redirect(y) == allowed


def test_redirect_add_parameters():
    uri = RedirectURI('https://example.com')
    assert str.endswith(uri.redirect(foo=1), '?foo=1')