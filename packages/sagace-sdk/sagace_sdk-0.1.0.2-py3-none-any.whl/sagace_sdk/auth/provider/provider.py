# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 11:23
    Created:          12/01/2024 11:23
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
import json

from datetime import datetime
from ...exceptions import AuthProviderException
from ...data_models.auth.login_request import LoginRequest

from ... import CONFIG


class Provider(object):
    _username = ''
    _password = ''
    _app_token = ''
    _login_request = None
    _auth_token = None
    _date = None

    def __init__(self, username: str, password: str, app_token: str):
        self._username = username
        self._password = password
        self._app_token = app_token
        self._auth_token = None
        self._login_request = LoginRequest(self._username, self._password)

    def auth_token(self):
        if self._auth_token is None:
            self._authenticate()
        elif datetime.now().timestamp() - self._date.timestamp() >= 3500:
            self._authenticate()

        return self._auth_token

    def _authenticate(self):
        from . import RequestManager

        url, e = CONFIG().url('base.authentication_and_notifications.login')

        if e is not None:
            raise e
        response, e = RequestManager.request(url.method, f"{url.url}",
                                             headers={"Authorization": f"{self._app_token}"},
                                             data=self._login_request.get_json_string())
        if e is not None:
            raise e

        if response.status_code == 200:
            data = json.loads(response.text)
            if data['status'] != 1:
                raise AuthProviderException(data['message'])
            self._auth_token = data['data']['authorization_token']
            self._date = datetime.now()
            return
        raise AuthProviderException(f"Invalid status code: {response.status_code}")
