# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 11:16
    Created:          12/01/2024 11:16
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
global __CONFIG__, __AUTH_PROVIDER__

# Manter no topo para evitar erro de referencia curcular
CONFIG = lambda: __CONFIG__ if __CONFIG__ is not None else Configuration()
AUTH_PROVIDER = lambda: __AUTH_PROVIDER__ if __AUTH_PROVIDER__ is not None else Provider('', '', '')


from .utils import Configuration
from .auth.provider import Provider


def configure(config: Configuration, auth_provider: Provider):
    global __CONFIG__, __AUTH_PROVIDER__
    __CONFIG__ = config
    __AUTH_PROVIDER__ = auth_provider
