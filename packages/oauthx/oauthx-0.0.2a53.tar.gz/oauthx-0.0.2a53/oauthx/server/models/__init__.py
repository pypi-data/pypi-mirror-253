# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .application import Application
from .assertion import Assertion
from .authorization import Authorization
from .authorizationcode import AuthorizationCode
from .authorizationcontext import AuthorizationContext
from .authorizationrequest import AuthorizationRequest
from .authorizationstate import AuthorizationState
from .baseclient import BaseClient
from .basemodel import BaseModel
from .claim import Claim
from .claimset import ClaimSet
from .client import Client
from .clientkey import ClientKey
from .confidentialclient import ConfidentialClient
from .grantedauthorizationcode import GrantedAuthorizationCode
from .issuedtoken import IssuedToken
from .objectfactory import ObjectFactory
from .principal import Principal
from .principal import PrincipalType
from .principal import PrincipalValueType
from .publicclient import PublicClient
from .receipt import Receipt
from .refreshtoken import RefreshToken
from .resourceowner import ResourceOwner
from .resourceownerkey import ResourceOwnerKey
from .responsemode import ResponseMode
from .scope import Scope
from .session import Session
from .subject import Subject
from .subjectkey import SubjectKey
from .userinfo import UserInfo


__all__: list[str] = [
    'Authorization',
    'Assertion',
    'AuthorizationCode',
    'AuthorizationContext',
    'AuthorizationRequest',
    'AuthorizationState',
    'Application',
    'BaseClient',
    'BaseModel',
    'Claim',
    'ClaimSet',
    'Client',
    'ClientKey',
    'ClientType',
    'ConfidentialClient',
    'GrantedAuthorizationCode',
    'IssuedToken',
    'ObjectFactory',
    'Principal',
    'PrincipalType',
    'PrincipalValueType',
    'PublicClient',
    'Receipt',
    'RefreshToken',
    'ResourceOwner',
    'ResourceOwnerKey',
    'ResponseMode',
    'Scope',
    'Session',
    'SubjectKey',
    'Subject',
    'UserInfo',
]

ClientType = ConfidentialClient | PublicClient