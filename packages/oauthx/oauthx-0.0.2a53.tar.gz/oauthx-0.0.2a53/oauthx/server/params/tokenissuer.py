# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import hashlib
import inspect
import logging
from typing import Annotated
from typing import Any
from typing import Iterable
from typing import TypeAlias

import fastapi
from aiopki.ext import jose
from aiopki.ext.jose import OIDCToken
from aiopki.types import ISigner
from aiopki.utils import b64encode

from oauthx.lib import utils
from oauthx.lib import RFC9068AccessToken
from oauthx.lib.protocols import IClient
from oauthx.lib.types import AccessToken
from oauthx.lib.types import RedirectURI
from oauthx.server.models import Authorization
from oauthx.server.config import Config
from oauthx.server.models import RefreshToken
from oauthx.server.protocols import IResourceOwner
from oauthx.server.request import Request
from oauthx.server.types import TokenMAC
from .currentconfig import CurrentConfig
from .datamaskingkey import DataMaskingKey
from .issuer import Issuer
from .storage import Storage


__all__: list[str] = ['TokenIssuer']


class _TokenIssuer:
    __module__: str = 'oauthx.server.handlers'
    default_ttl: int = 3600
    logger: logging.Logger = logging.getLogger('uvicorn')
    storage: Storage

    @utils.class_property
    def __signature__(cls) -> inspect.Signature:
        return utils.merge_signatures([
            inspect.signature(cls.__init__),
            inspect.signature(cls.setup)
        ])

    def __init__(
        self,
        request: Request,
        issuer: Issuer,
        masking_key: DataMaskingKey,
        storage: Storage,
        config: Config = CurrentConfig,
        **kwargs: Any
    ):
        self.config = config
        self.issuer = issuer
        self.masking_key = masking_key
        self.request = request
        self.storage = storage
        self.setup(**kwargs)

    async def access_token(
        self,
        signer: ISigner,
        client_id: str,
        sub: str,
        aud: str | Iterable[str] | None = None,
        scope: set[str] | None = None,
        **claims: Any
    ) -> AccessToken:
        token = RFC9068AccessToken.new(
            ttl=self.default_ttl,
            client_id=client_id,
            aud=aud or client_id,
            iss=self.issuer,
            scope=scope or set(),
            sub=sub,
            **claims
        )
        return AccessToken(await token.sign(signer))

    async def authorization_code(
        self,
        signer: ISigner,
        client: IClient,
        owner: IResourceOwner,
        authorization_id: int,
        sub: str,
        redirect_uri: RedirectURI | str | None
    ) -> str:
        mac = TokenMAC()
        mac.add(client)
        mac.add(owner)
        params: dict[str, Any] = {
            'aut': int(authorization_id),
            'client_id': str(client.id),
            'sub': str(sub),
            'mac': str(mac),
        }
        if redirect_uri is not None:
            params['redirect_uri'] = b64encode(
                hashlib.sha3_256(str.encode(redirect_uri)).digest(),
                encoder=bytes.decode
            )
        jws = jose.jws(params)
        await jws.sign(signer.default_algorithm(), signer, {'typ': 'jwt+code'})
        return jws.encode(encoder=bytes.decode)

    async def id_token(
        self,
        signer: ISigner,
        userinfo: OIDCToken,
        access_token: AccessToken | None = None,
        code: str | None = None,
    ) -> jose.JOSEObject:
        jws = jose.jws(userinfo.model_dump(), {'typ': 'jwt'})
        await jws.sign(signer.default_algorithm(), signer)
        return jws

    async def refresh_token(
        self,
        signer: ISigner,
        client: IClient,
        owner: IResourceOwner,
        authorization: Authorization,
    ):
        rt = RefreshToken.new(
            ttl=86400*180,
            iss=self.issuer,
            aud=str(self.request.url_for('oauth2.token')),
            aut=authorization.id,
            client_id=str(client.id),
            sub=str(owner.sub)
        )
        return await rt.sign(signer)

    def setup(self, **kwargs: Any):
        pass


TokenIssuer: TypeAlias = Annotated[_TokenIssuer, fastapi.Depends(_TokenIssuer)]