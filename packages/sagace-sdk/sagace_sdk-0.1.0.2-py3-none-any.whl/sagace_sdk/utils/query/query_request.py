# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 14:42
    Created:          12/01/2024 14:42
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
from typing import Any

from . import Pagination
from . import Order
from . import Filter
from ...enums import QueryOrder
from ...enums import QueryCondition
from ...enums import FilterOperator


class QueryRequest:
    pagination = Pagination()
    orders = {}
    filters = {}

    def get_request(self) -> dict:
        response = {
            "pagination": {
                "page": self.pagination.page,
                "size": self.pagination.size
            },
            "orders": {},
            "filters": {}
        }
        for key, value in self.orders.items():
            response['orders'][key] = value.value

        for key, value in self.filters.items():
            if key == QueryCondition.AND or key == QueryCondition.OR:
                for s_key, s_value in value.items():
                    if key not in response['filters']:
                        response['filters'][key] = {}
                    response['filters'][key][s_key] = {
                        "operator": s_value.operator.value,
                        "value": s_value.value
                    }
            else:
                response['filters'][key] = {
                    "operator": value.operator.value,
                    "value": value.value
                }

        if QueryCondition.AND in response['filters']:
            if len(response['filters'][QueryCondition.AND]) == 0:
                del response['filters'][QueryCondition.AND]

        if QueryCondition.OR in response['filters']:
            if len(response['filters'][QueryCondition.OR]) == 0:
                del response['filters'][QueryCondition.OR]

        return response

    def set_order(self, column: str, order: QueryOrder):
        self.orders[column] = order

    def remove_order(self, column: str):
        if column in self.orders:
            del self.orders[column]

    def set_filter(self, column: str, operator: FilterOperator, value: Any):
        self.filters[column] = Filter(operator, value)

    def remove_filter(self, column: str):
        if column in self.filters:
            del self.filters[column]

    def set_conditional_filter(self, condition: QueryCondition, column: str, operator: FilterOperator, value: Any):
        if condition not in self.filters:
            self.filters[condition] = {}
        self.filters[condition][column] = Filter(operator, value)

    def remove_conditional_filter(self, condition: QueryCondition, column: str):
        if condition in self.filters:
            if column in self.filters[condition]:
                del self.filters[condition][column]

            if len(self.filters[condition]) == 0:
                del self.filters[condition]
