# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Any
from typing import Literal

import fastapi
from aiopki.ext.jose import OIDCToken

from oauthx.lib.params import Logger
from oauthx.lib.types import RedirectURI
from oauthx.lib.types import OIDCIssuerIdentifier
from oauthx.server.protocols import IAuthorizationServer
from oauthx.server.protocols import IRegisteredClient
from oauthx.server.protocols import IResourceOwner
from oauthx.server.protocols import ISubject
from .models import SubjectKey
from .params import ContentEncryptionKey
from .params import ObjectFactory
from .params import Storage
from .params import SubjectLogger
from .params import TokenIssuer
from .params import TokenSigner
from .subjectresolver import SubjectResolver


class AuthorizationServer(IAuthorizationServer):
    __module__: str = 'oauthx.server'
    factory: ObjectFactory
    non_personal_claims: set[str] = {
        'aud', 'exp', 'iss', 'nbf', 'at_hash', 'c_hash',
        'nonce', 'iat', 'azp', 'acr', 'amr'
    }
    storage: Storage
    subjects: SubjectResolver

    def __init__(
        self,
        issuer: TokenIssuer,
        logger: Logger,
        storage: Storage,
        encryption_key: ContentEncryptionKey,
        factory: ObjectFactory,
        signer: TokenSigner,
        subject_publisher: SubjectLogger,
        subjects: SubjectResolver = fastapi.Depends(SubjectResolver)
    ):
        self.encryption_key = encryption_key
        self.factory = factory
        self.issuer = issuer
        self.logger = logger
        self.signer = signer
        self.storage = storage
        self.subjects = subjects
        self.subject_publisher = subject_publisher

    async def get_subject(
        self,
        pk: SubjectKey,
        decrypt: bool = False
    ) -> ISubject | None:
        """Return the subject identified by the primary key."""
        subject = await self.storage.get(pk)
        if subject is not None and decrypt:
            await subject.decrypt_keys(self.encryption_key)
        return subject

    async def issue_authorization_code(
        self,
        client: IRegisteredClient,
        owner: IResourceOwner,
        authorization_id: int,
        redirect_uri: RedirectURI | None = None
    ) -> str:
        """Issue an authorization code that the client can use to obtain
        an access token.
        """
        return await self.issuer.authorization_code(
            signer=self.signer,
            client=client,
            owner=owner,
            authorization_id=authorization_id,
            sub=owner.sub,
            redirect_uri=redirect_uri
        )

    async def onboard_oidc(
        self,
        token: OIDCToken,
        use: Literal['personal', 'institutional'],
        request_id: int | None = None,
        client_id: str | None = None
    ) -> tuple[ISubject, bool]:
        created = False
        issuer = OIDCIssuerIdentifier(token.iss)
        register: set[Any] = set()
        subject = None

        # Try to get subject by the identifier returned by the identity provider.
        # If the identifier yields no subject, then this provider was not used
        # before to login. In that case, it is safe to lookup the subject by
        # its email address and associate the identifier. If the sub claim
        # does resolve to a principal, the email address MUST match the
        # known email address or be None.
        email = await self.subjects.resolve_principal(token.email)
        subject_id = await self.subjects.resolve_principal(token.subject_id)
        if subject_id and email:
            # If there is an email principal, then the sub claims must match.
            if not email.is_owned_by(subject_id.owner):
                # We have a problem.
                self.logger.warning("OIDC ID Token resolved to multiple principals.")
                raise self.AmbiguousPrincipal
            subject = await self.storage.get(email.owner)
            if subject is None:
                self.logger.critical(
                    "Could not retrieve Subject with the given Principal "
                    "(kind: %s, mask: %s)",
                    email.kind, email.masked
                )
                raise self.OrphanedPrincipal
        elif not any([subject_id, email]):
            # This is a new user and we can safely created it.
            created = True
            subject = await self.factory.subject(use)
            subject.update_from_oidc(token)
            register.update({token.subject_id, token.email, token.phone_number})
        elif subject_id and not email:
            subject = await self.storage.get(subject_id.owner)
            if subject is None:
                self.logger.critical(
                    "Could not retrieve Subject with the given Principal "
                    "(kind: %s, mask: %s)",
                    subject_id.kind, subject_id.masked
                )
                raise self.OrphanedPrincipal
            register.update({token.email, token.phone_number})
        elif email and not subject_id:
            subject = await self.storage.get(email.owner)
            if subject is None:
                self.logger.critical(
                    "Could not retrieve Subject with the given Principal "
                    "(kind: %s, mask: %s)",
                    email.kind, email.masked
                )
                raise self.OrphanedPrincipal
            register.update({token.subject_id, token.phone_number})
        else:
            raise NotImplementedError
        register.remove(None)
        assert subject is not None
        assert None not in register
        if created:
            self.logger.info(
                "Registered subject from OpenID Connect "
                "(iss: %s, sub: %s)",
                token.iss, subject.get_primary_key()
            )
            await subject.encrypt_keys(self.encryption_key)
            await self.storage.persist(subject)
        await subject.decrypt_keys(self.encryption_key) # type: ignore
        if token.subject_id in register:
            await self.register_principal(
                issuer=OIDCIssuerIdentifier(token.iss),
                subject=subject,
                value=token.subject_id,
                created=created,
                verified=True
            )
        if token.email in register:
            await self.register_principal(
                issuer=OIDCIssuerIdentifier(token.iss),
                subject=subject,
                value=token.email,
                created=created,
                verified=token.email_verified
            )
        if token.phone_number in register:
            await self.register_principal(
                issuer=issuer,
                subject=subject,
                value=token.email,
                created=created,
                verified=token.phone_number_verified
            )

        receipt = await self.factory.receipt(
            provider=token.iss,
            purpose='LOGIN',
            sub=int(subject.get_primary_key()), # type: ignore
            claims={k for k in token.model_dump(
                exclude=self.non_personal_claims,
                exclude_none=True
            )},
            request_id=request_id,
            client_id=client_id
        )
        async with receipt.transaction(subject, self.storage, self.subject_publisher) as tx:
            tx.add('birthdate', token.gender, issuer='self')
            tx.add('gender', token.gender, issuer='self')
            tx.add('email', token.email,
             issuer='self' if not token.email_verified else issuer)
            tx.add('phone_number', token.phone_number,
             issuer='self' if not token.phone_number_verified else issuer)
            tx.add('name', token.name, issuer='self')
            tx.add('given_name', token.given_name, issuer='self')
            tx.add('middle_name', token.middle_name, issuer='self')
            tx.add('family_name', token.family_name, issuer='self')
            tx.add('nickname', token.nickname, issuer='self')

        return subject, created

    async def register_principal(
        self,
        *,
        issuer: OIDCIssuerIdentifier,
        subject: ISubject,
        value: Any,
        created: bool = False,
        verified: bool = False
    ) -> None:
        now = datetime.datetime.now(datetime.timezone.utc)
        new = await self.factory.principal(
            subject=subject,
            issuer=issuer,
            owner=subject.get_primary_key(), # type: ignore
            now=now,
            value=value,
            verified=verified
        )
        old = await self.storage.get(new.masked)
        if not old or not old.is_verified():
            await new.encrypt(subject)
            await self.storage.persist(new)