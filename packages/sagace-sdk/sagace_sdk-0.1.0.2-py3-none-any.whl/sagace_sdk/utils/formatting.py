# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 15:41
    Created:          12/01/2024 15:41
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""


def convert_from_table_format(table_format: list) -> list:
    response = list()

    for table in table_format:
        item = {}
        for column in table:
            item[column] = table[column]['value']
        response.append(item)
    return response
