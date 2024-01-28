# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import functools
import hashlib
import operator
import secrets
from typing import Any
from typing import Literal
from typing import Iterable

import fastapi
from aiopki.utils import b64encode
from aiopki.ext.jose import OIDCToken

from oauthx.lib.protocols import IStorage
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import ResponseType
from oauthx.lib.types import OIDCIssuerIdentifier
from oauthx.server.models import BaseClient
from oauthx.server.protocols import ISubject
from oauthx.server.protocols import IUserInfoContributor
from oauthx.server.types import IPrincipalMasker
from oauthx.server.types import IResponseMode
from .authorization import Authorization
from .authorizationrequest import AuthorizationRequest
from .claim import Claim
from .principal import Principal
from .principal import PrincipalValueType
from .receipt import Receipt
from .responsemode import ResponseMode
from .scope import Scope
from .subject import Subject
from .subjectkey import SubjectKey
from .userinfo import UserInfo


class ObjectFactory:
    """Provides an interface to create model instances used by
    the authorization server.
    """
    __module__: str = 'oauthx.server'
    default_scopes: list[Scope] = [
        Scope(name='openid', claims=[
            'acr',
            'amr',
            'auth_time',
            'azp',
            'nonce',
            'sub',
        ]),
        Scope(name='address', claims=['address']),
        Scope(
            name='email',
            claims=[
                'email',
                'email_verified'
            ]
        ),
        Scope(
            name='profile',
            claims=[
                'name',
                'family_name',
                'given_name',
                'middle_name',
                'nickname',
                'preferred_username',
                'profile',
                'picture',
                'website',
                'gender',
                'birthdate',
                'zoneinfo',
                'locale',
                'updated_at' 
            ]
        ),
        Scope(
            name='phone',
            claims=[
                'phone_number',
                'phone_number_verified'
            ]
        ),
    ]
    masker: IPrincipalMasker
    storage: IStorage

    def __init__(
        self,
        issuer: str,
        storage: IStorage,
        masker: IPrincipalMasker,
        scopes: list[Scope] | None = None
    ):
        self.scopes = {
            **{x.name: x for x in self.default_scopes},
            **{x.name: x for x in (scopes or [])}
        }
        self.issuer = issuer
        self.masker = masker
        self.storage = storage

    async def authorization(
        self,
        request: AuthorizationRequest,
        client_id: str,
        sub: SubjectKey,
        token_types: Iterable[str],
        lifecycle: Literal['GRANTED', 'ISSUED'] = 'ISSUED',
        scope: set[str] | None = None,
        contributors: list[IUserInfoContributor] = []
    ) -> Authorization:
        obj = Authorization.model_validate({
            'issuer': self.issuer,
            'client_id': str(client_id),
            'id': request.id,
            'lifecycle': lifecycle,
            'scope': scope or set(),
            'sub': sub,
            'token_types': set(token_types),
            'resources': request.resources
        })
        for contributor in contributors:
            obj.contribute(contributor)
        return obj.attach(self.storage)

    async def claim(
        self,
        receipt_id: int,
        kind: Literal['email', 'gender', 'name'],
        provider: str,
        issuer: str,
        sub: int,
        value: Any,
        now: datetime.datetime | None = None,
        ial: int = 0,
    ) -> Claim:
        now = now or datetime.datetime.now(datetime.timezone.utc)
        return Claim.new(
            receipt_id=receipt_id,
            id=await self.storage.allocate_identifier(Claim),
            kind=kind,
            provider=provider,
            issuer=issuer,
            sub=sub,
            value=value,
            now=now
        )

    async def principal(
        self,
        *,
        subject: ISubject,
        issuer: Literal['self'] | OIDCIssuerIdentifier,
        owner: SubjectKey,
        value: PrincipalValueType,
        now: datetime.datetime | None = None,
        verified: bool = False
    ) -> Principal:
        """Create a new :class:`~oauthx.types.IPrincipal` instance."""
        mask = value.mask(self.masker.mask)
        now = now or datetime.datetime.now(datetime.timezone.utc)
        return Principal.model_validate({
            'issuer': issuer,
            'masked': await mask,
            'owner': int(owner),
            'registered': now,
            'value': value,
            'verified': verified
        })

    async def receipt(
        self,
        provider: str | OIDCIssuerIdentifier,
        purpose: Literal['IDENTIFY', 'INVITE', 'LOGIN', 'VERIFY_ACCOUNT'],
        sub: int,
        claims: set[str],
        now: datetime.datetime | None = None,
        request_id: int | None = None,
        client_id: str | None = None
    ):        
        now = now or datetime.datetime.now(datetime.timezone.utc)
        receipt_id = await self.storage.allocate_identifier('Receipt')
        return Receipt.model_validate({
            'id': receipt_id,
            'obtained': now,
            'purpose': purpose,
            'provider': provider,
            'sub': sub,
            'received': claims,
            'client_id': client_id,
            'request_id': request_id
        })

    async def request(
        self,
        client: BaseClient,
        request: fastapi.Request,
        redirect_uri: RedirectURI | None,
        resources: Iterable[str] | None = None,
        scope: set[str] | None = None
    ) -> AuthorizationRequest:
        obj = AuthorizationRequest.model_validate({
            **request.query_params,
            'iss': self.issuer,
            'id': await self.storage.allocate_identifier(Authorization),
            'client_id': str(client.client_id),
            'client_name': client.get_display_name(),
            'redirect_uri': redirect_uri,
            'resources': resources or set(),
            'scope': scope or set()
        })
        return obj.attach(self.storage)

    async def response_mode(
        self,
        iss: str,
        client: BaseClient,
        response_type: ResponseType | None,
        response_mode: str | None,
        redirect_uri: RedirectURI | None,
        state: str | None
    ) -> IResponseMode:
        return ResponseMode.model_validate({ # type: ignore
            'iss': iss,
            'client': client,
            'redirect_uri': redirect_uri,
            'response_type': response_type,
            'response_mode': response_mode,
            'state': state
        })

    async def subject(self, use: Literal['personal', 'institutional'], pk: int | None = None) -> ISubject:
        """Create a new :class:`~oauthx.types.ISubject` instance."""
        k = secrets.token_bytes(32)
        m = secrets.token_bytes(32)
        n = datetime.datetime.now(datetime.timezone.utc)
        return Subject.model_validate({
            'use': use,
            'sub': pk or await self.storage.allocate_identifier(Subject),
            'kind': 'User',
            'dmk': {
                'kty': 'oct',
                'alg': 'HS384',
                'iat': n,
                'kid': b64encode(hashlib.sha256(m).digest(), encoder=bytes.decode),
                'k': b64encode(k, encoder=bytes.decode),
                'use': 'sig',
            },
            'dek': {
                'kty': 'oct',
                'alg': 'dir',
                'iat': n,
                'kid': b64encode(hashlib.sha256(k).digest(), encoder=bytes.decode),
                'use': 'enc',
                'k': b64encode(k, encoder=bytes.decode)
            }
        })

    async def userinfo(
        self,
        subject: ISubject,
        scope: set[str] | None = None,
        contributors: list[IUserInfoContributor] | None = None,
        **claims: Any
    ) -> OIDCToken:
        """Construct an :class:`~aiopki.ext.jose.OIDCToken` instance representing
        the claims that are granted under the given `scope`.
        """
        userinfo = await UserInfo.restore(subject, self.storage)
        subject.contribute_to_userinfo(userinfo)
        for contributor in (contributors or []):
            contributor.contribute_to_userinfo(userinfo)
        granted = set(userinfo.claims.keys())
        if scope is not None:
            granted = self._get_granted_claims(scope)
        return OIDCToken.new(120, **{
            **userinfo.dump(granted),
            **claims,
            'sub': str(subject.get_primary_key()),
            'iss': self.issuer
        })

    def _get_granted_claims(self, scope: set[str]) -> set[str]:
        claims = [self.scopes[x].claims for x in scope if x in self.scopes]
        return set(functools.reduce(operator.add, claims, []))