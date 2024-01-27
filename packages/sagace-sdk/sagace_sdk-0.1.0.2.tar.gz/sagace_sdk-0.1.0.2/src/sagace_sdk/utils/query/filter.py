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
from typing import Any
from ...enums import FilterOperator


class Filter(object):
    operator = FilterOperator.EQ
    value = None

    def __init__(self, operator: FilterOperator = FilterOperator.EQ, value: Any = None):
        self.operator = operator
        self.value = value
