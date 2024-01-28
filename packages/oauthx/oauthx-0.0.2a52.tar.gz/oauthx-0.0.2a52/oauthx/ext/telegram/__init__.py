# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

from oauthx.lib.protocols import IClient
from oauthx.server import Plugin
from oauthx.server.models import Authorization
from oauthx.server.models import Principal
from oauthx.server.params import PendingAuthorizationRequest
from oauthx.server.params import SubjectLogger
from oauthx.server.types import IAuthorizationRouter
from oauthx.server.types import StopSnooping
from .const import ISSUER
from .params import TelegramBotName
from .params import TelegramUserInfo
from .types import TelegramAccountUnusable


class TelegramPlugin(Plugin):
    __module__: str = 'oauthx.ext.telegram'
    
    @classmethod
    def __register__(cls, router: IAuthorizationRouter) -> None:
        router.add_plugin(
            methods=['GET'],
            path='telegram/confirm',
            handler=cls,
            method=cls.login,
            name='oauth.ext.telegram.login',
            description=(
                "Login with Telegram to register an account."
            ),
            authenticated=True
        )
        router.add_plugin(
            methods=['GET'],
            path='telegram/welcome',
            handler=cls,
            method=cls.welcome,
            name='oauth.ext.telegram.welcome',
            description="Callback for Telegram post-login.",
            authenticated=True,
            needs_data=True
        )
        router.register_template_module('oauthx.ext.telegram')

    async def welcome(
        self,
        authnreq: PendingAuthorizationRequest,
        userinfo: TelegramUserInfo,
        bot_name: TelegramBotName,
        logger: SubjectLogger
    ) -> fastapi.Response:
        # Retrieve or create a principal and determine if the currently
        # authenticated user has permission to use it.
        assert self.subject is not None
        context = {
            'telegram_bot_name': bot_name,
            'telegram_callback_url': self.request.url_for(
                'oauth.ext.telegram.welcome',
                pk=str(authnreq.pk)
            ),
            'telegram_username':  userinfo.username
        }
        principal = await self.storage.get(userinfo.masked)
        sub = int(self.subject.get_primary_key()) # type: ignore
        if principal is None:
            principal = await self.factory.principal(
                subject=self.subject,
                issuer=userinfo.issuer,
                owner=self.subject.get_primary_key(), # type: ignore
                verified=True,
                value=userinfo.id
            )
            await principal.encrypt(self.subject)
            await self.storage.persist(principal)
            
            receipt = await self.factory.receipt(
                provider=userinfo.issuer,
                purpose='VERIFY_ACCOUNT',
                sub=sub,
                claims={
                    'telegram',
                    'given_name',
                    'preferred_username',
                    'family_name'
                },
                client_id=str(authnreq.client_id),
                request_id=authnreq.id
            )
            async with receipt.transaction(self.subject, self.storage, logger) as tx:
                tx.add(
                    kind='telegram',
                    value=str(userinfo.id.sub),
                    issuer=userinfo.issuer
                )
        elif not principal.is_owned_by(sub):
            raise TelegramAccountUnusable(context)
        authnreq.add_to_template_context(self.request, context)
        return await self.request.render_to_response(
            template_names=f'oauthx/telegram/welcome.html.j2',
            context=context
        )

    async def login(
        self,
        authnreq: PendingAuthorizationRequest,
        bot_name: TelegramBotName,
    ) -> fastapi.Response:
        if self.subject is None:
            raise StopSnooping
        context = {
            'telegram_bot_name': bot_name,
            'telegram_callback_url': self.request.url_for(
                'oauth.ext.telegram.welcome',
                pk=str(authnreq.pk)
            ),
        }
        authnreq.add_to_template_context(self.request, context)
        return await self.request.render_to_response(
            template_names=f'oauthx/telegram/login.html.j2',
            context=context
        )

    def handles_scope(self, name: str) -> bool:
        return name == 'telegram'

    async def resolve_scope(
        self,
        client: IClient,
        authorization: Authorization,
        name: str
    ) -> tuple[str | None, dict[str, str]]:
        assert self.subject is not None
        principals = [x async for x in self.storage.find(
            kind=Principal,
            filters=[
                ('kind', '=', 'subject'),
                ('issuer', '=', ISSUER),
                ('owner', '=', int(self.subject.get_primary_key())) # type: ignore
            ]
        )]
        if principals:
            return None, {}

        return 'oauth.ext.telegram.login', {}