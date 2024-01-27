# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 15:06
    Created:          12/01/2024 15:06
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
import json

from ... import CONFIG
from ... import AUTH_PROVIDER
from ...auth.provider import RequestManager
from ...utils.query import QueryRequest
from ...utils.formatting import convert_from_table_format


def get_all(query: QueryRequest) -> list:
    url, e = CONFIG().url('base.users.get_all')

    if e is not None:
        raise e
    body = query.get_request()
    response, e = RequestManager.request(url.method, f"{url.url}",
                                         headers={'Content-Type': 'application/json'},
                                         data=json.dumps(body),
                                         provider=AUTH_PROVIDER())
    if e is not None:
        raise e

    response_data = json.loads(response.text)

    if response_data['status'] == 1:
        return convert_from_table_format(response_data['data'])
    return []
