# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .error import Error
from .fatalerror import FatalError
from .insufficientscope import InsufficientScope
from .interactionexception import InteractionException
from .invalidauthorizationresponse import InvalidAuthorizationResponse
from .invalidgrant import InvalidGrant
from .invalidredirecturi import InvalidRedirectURI
from .invalidrequest import InvalidRequest
from .invalidscope import InvalidScope
from .invalidtarget import InvalidTarget
from .invalidtoken import InvalidToken
from .invalidtokenresponse import InvalidTokenResponse
from .stopsnooping import StopSnooping
from .trustissues import TrustIssues
from .unknownclient import UnknownClient
from .unsupportedresponsetype import UnsupportedResponseType
from .useragentexception import UserAgentException


__all__: list[str] = [
    'Error',
    'FatalError',
    'InsufficientScope',
    'InteractionException',
    'InvalidAuthorizationResponse',
    'InvalidGrant',
    'InvalidRedirectURI',
    'InvalidRequest',
    'InvalidScope',
    'InvalidTarget',
    'InvalidToken',
    'InvalidTokenResponse',
    'StopSnooping',
    'TrustIssues',
    'UnknownClient',
    'UnsupportedResponseType',
    'UserAgentException',
]