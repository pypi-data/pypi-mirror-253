# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 11:21
    Created:          12/01/2024 11:21
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
from .provider import Provider


class AuthManager(object):
    __auth_provider = None

    def __init__(self, auth_provider: Provider):
        """
        Authorization Manager - Keep track of authentication information.

        :param auth_provider: Authorization Provider
        """
        self.__auth_provider = auth_provider

