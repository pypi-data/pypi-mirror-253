# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 12:01
    Created:          12/01/2024 12:01
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
from typing import Tuple

import requests
from requests import Response

from .provider import Provider
from ... import CONFIG
from ...exceptions import RequestException


class RequestManager(object):
    @staticmethod
    def request(method: str, url: str, headers: dict = None, data: dict | tuple | str | bytes = None,
                provider: Provider = None) -> tuple[Response, None] | tuple[None, RequestException]:
        try:
            if headers is None:
                headers = dict()

            if provider is not None:
                headers['Authorization'] = f"JWT {provider.auth_token()}"

            response = requests.request(method, url + '?XDEBUG_SESSION_START={{XDebugSessionId}}',
                                        headers=headers,
                                        data=data,
                                        verify=CONFIG().SSLVerify,
                                        proxies=CONFIG().Proxies)

            return response, None
        except Exception as e:
            return None, RequestException(e)
