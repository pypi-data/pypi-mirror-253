# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from oauthx.lib.exceptions import InteractionException
from oauthx.lib.exceptions import StopSnooping

from .accountissues import AccountIssues
from .authorizationkey import AuthorizationKey
from .authorizationrequestkey import AuthorizationRequestKey
from .claimsetkey import ClaimSetKey
from .iauthorizationrequest import IAuthorizationRequest
from .iauthorizationrouter import IAuthorizationRouter
from .iclaimset import IClaimSet
from .invalidauthorizationrequest import InvalidAuthorizationRequest
from .invalidclient import InvalidClient
from .invalidredirecturi import InvalidRedirectURI
from .invalidresponsetype import InvalidResponseType
from .iprincipalmasker import IPrincipalMasker
from .iresponsemode import IResponseMode
from .loginrequired import LoginRequired
from .missingredirecturi import MissingRedirectURI
from .tokenmac import TokenMAC
from .unauthorizedaccount import UnauthorizedAccount
from .unauthorizedclient import UnauthorizedClient
from .unusableaccount import UnusableAccount


__all__: list[str] = [
    'AuthorizationKey',
    'AuthorizationRequestKey',
    'AccountIssues',
    'ClaimSetKey',
    'IAuthorizationRequest',
    'IAuthorizationRouter',
    'IClaimSet',
    'InteractionException',
    'InvalidAuthorizationRequest',
    'InvalidClient',
    'InvalidRedirectURI',
    'InvalidResponseType',
    'IPrincipalMasker',
    'IResponseMode',
    'LoginRequired',
    'MissingRedirectURI',
    'StopSnooping',
    'TokenMAC',
    'UnauthorizedAccount',
    'UnauthorizedClient',
    'UnusableAccount',
]