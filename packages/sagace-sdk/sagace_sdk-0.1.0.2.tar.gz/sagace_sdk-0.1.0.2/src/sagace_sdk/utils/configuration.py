# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 12:22
    Created:          12/01/2024 12:22
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
import json

from . import URL
from ..exceptions import UrlSearchException


class Configuration:
    BaseURL = "https://sagace.online"
    SSLVerify = True
    Proxies = None
    __URL__ = {
        'base': {
            'authentication_and_notifications': {
                'login': URL('POST', '/auth/base/login/')
            },
            'users': {
                'get_all': URL('GET', '/auth/user/get-all/')
            }
        }
    }

    def url(self, ref) -> (URL | None, UrlSearchException):
        url_cp = self.__URL__.copy()

        for key in str(ref).split('.'):
            if key not in url_cp:
                return None, UrlSearchException(f"Key {key} not found in configuration")
            url_cp = url_cp[key]
        if type(url_cp) != URL:
            return None, UrlSearchException(f"Key {ref} not found in configuration")
        return URL(url_cp.method, f"{self.BaseURL}{url_cp.url}"), None


