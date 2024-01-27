# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 12:11
    Created:          12/01/2024 12:11
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
import json


class Model(object):
    def get_json_data(self) -> dict:
        obj_dict = self.__dict__
        return obj_dict

    def get_json_string(self) -> str:
        obj_dict = self.__dict__
        response_data = json.dumps(obj_dict)

        return response_data
