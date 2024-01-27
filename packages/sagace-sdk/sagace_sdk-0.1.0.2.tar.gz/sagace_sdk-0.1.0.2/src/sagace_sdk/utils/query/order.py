# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 14:29
    Created:          12/01/2024 14:29
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
from ...enums import QueryOrder


class Order(object):
    name = ''
    order = QueryOrder.ND

    def __init__(self, name: str, order: QueryOrder):
        self.name = name
        self.order = order
