# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import re
from typing import Any

import aiopki
import aiopki.types
import aiopki.ext.jose
import fastapi
import httpx
from aiopki.ext.keychain import Keychain
from canonical.protocols import ITemplateService

from oauthx.lib.protocols import IClient
from oauthx.lib.protocols import IStorage
from oauthx.lib.types import RedirectURI
from oauthx.server.protocols import IRequestSession
from oauthx.server.protocols import IRequestSubject
from .models import AuthorizationContext
from .models import ResponseMode


CACHE_HEADERS: set[str] = {
    'Cache-Control',
    'Expires',
    'Pragma',
}


class Request(fastapi.Request):
    context: AuthorizationContext | None = None
    http: httpx.AsyncClient | None = None
    keychain: Keychain
    oauth_client: IClient | None = None
    promptable: bool = False
    redirect_uri: RedirectURI | None = None
    response_mode: ResponseMode | None = None
    session_data: IRequestSession | None = None
    session_cookie: str
    signer: aiopki.types.ICryptoKey
    storage: IStorage
    subject: IRequestSubject | None = None
    templates: ITemplateService
    token_signer: aiopki.CryptoKeyType

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

    def authenticate(
        self,
        sub: str,
        email: str | None = None
    ) -> None:
        if self.session_data:
            self.session_data.authenticate(sub, email)

    def can_redirect(self) -> bool:
        return any([
            self.response_mode and self.response_mode.can_redirect(),
            self.context and self.context.can_redirect()
        ])

    def get_response_media_type(self, select: list[str]) -> str | None:
        accepts = {
            re.sub(';.*$', '', x)
            for x in str.split(self.headers.get('Accept', 'application/json'), ',')}
        return 'text/html'\
            if bool({'text/html', '*/*'} & accepts)\
            else 'application/json'

    def is_authenticated(self) -> bool:
        return self.subject is not None and self.subject.is_authenticated()

    def set_client(self, client: IClient):
        self.oauth_client = client

    def set_context(self, context: AuthorizationContext):
        self.context = context

    def set_session(self, session: IRequestSession) -> None:
        self.session_data = session

    async def error(
        self,
        template_names: str | list[str],
        error: str,
        error_description: str | None = None,
        error_uri: str | None = None,
        status_code: int = 400,
        media_type: str | None = None,
        context: dict[str, Any] | None = None,
        allow_redirect: bool = True
    ) -> fastapi.Response:
        accepts = self.get_response_media_type(['text/html', 'application/json']) or media_type
        context = {**(context or {}), 'client': self.oauth_client, 'error': error}
        headers: dict[str, str] = {
            'X-Error': error
        }
        if error_description:
            context['error_description'] = error_description
            headers['X-Error-Description'] = error_description
        if error_uri:
            context['error_uri'] = error_uri
            headers['X-Error-URI'] = error_uri
        if self.context:
            context.update(await self.context.get_template_context())
        can_redirect = allow_redirect and any([
            self.response_mode and self.response_mode.can_redirect(),
            self.context and self.context.can_redirect()
        ])
        match accepts:
            case 'text/html':
                if self.response_mode and can_redirect:
                    response = await self.response_mode.redirect(
                        error=context['error'],
                        error_description=context.get('error_description'),
                        error_uri=context.get('error_uri'),
                    )
                    response.headers.update(headers)
                elif self.context and can_redirect:
                    response = fastapi.responses.RedirectResponse(
                        status_code=302,
                        headers=headers,
                        url=await self.context.error(
                            error=error,
                            error_description=error_description,
                            error_uri=error_uri
                        )
                    )
                else:
                    response = await self.render_to_response(
                        template_names=template_names,
                        status_code=status_code,
                        headers=headers,
                        context=context
                    )
            case 'application/json':
                response = fastapi.responses.JSONResponse(
                    status_code=status_code,
                    headers=headers,
                    content=context
                )
            case _:
                response = fastapi.responses.Response(
                    status_code=status_code,
                    headers=headers
                )
        return response

    @staticmethod
    async def sign_session(session: IRequestSession, signer: aiopki.types.ICryptoKey) -> str:
        jws = aiopki.ext.jose.jws(session.claims())
        await jws.sign(
            algorithm=signer.default_algorithm(),
            signer=signer,
            protected={'typ': 'jwt+session'}
        )
        return jws.encode(encoder=bytes.decode)

    async def process_response(self, response: fastapi.Response) -> fastapi.Response:
        # See https://curity.io/resources/learn/oauth-cookie-best-practices/
        if self.session_data and self.session_data.is_dirty():
            response.set_cookie(
                key=self.session_cookie,
                value=await self.sign_session(self.session_data, self.signer),
                max_age=(86400 * 365),
                secure=True,
                httponly=True,
                samesite='lax'
            )
        if not bool(set(response.headers) & CACHE_HEADERS):
            response.headers.update({
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Expires': '0',
                'Pragma': 'Expires'
            })
        return response

    async def render_to_response(
        self,
        template_names: list[str] | str,
        context: dict[str, Any] | None = None,
        status_code: int = 200,
        headers: dict[str, Any] | None = None
    ) -> fastapi.Response:
        context = {
            **(context or {}),
            'request': self,
            'client': self.oauth_client
        }
        return fastapi.responses.HTMLResponse(
            status_code=status_code,
            headers=headers,
            content=await self.templates.render_template(
                template_names,
                context=context or {}
            )
        )

    async def sign(
        self,
        message: bytes,
        algorithm: aiopki.types.IAlgorithm | None = None,
        using: str | None = None
    ) -> bytes:
        return await self.signer.sign(message, algorithm, using)