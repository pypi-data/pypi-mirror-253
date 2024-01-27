# -*- coding: utf-8 -*-
"""
    --------------------------------------------------------------------------------------------------------------------

    Description:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Obs.:

    Author:           @diego.yosiura
    Last Update:      12/01/2024 11:29
    Created:          12/01/2024 11:29
    Copyright:        (c) Ampere Consultoria Ltda
    Original Project: sagace-v2-package
    IDE:              PyCharm
"""
import json

from . import Provider
from ...exceptions import AuthProviderException


class FileProvider(Provider):
    _file_path = ''

    def __init__(self, file_path: str):
        self._file_path = file_path
        data, e = self.get_file_data()
        if data is None:
            raise e
        super().__init__(data['ds_username'], data['ds_password'], data['ds_token'])

    def get_file_data(self) -> (dict | None, Exception | None):
        """
        Read file content and format.
        :return: dict containing file information or None if file was not found or invalid.
        """
        try:
            with open(self._file_path, 'rb') as f:
                data = f.read()
                response = json.loads(data.decode())
                if response is None:
                    return None, AuthProviderException("Invalid Auth file data")

                not_found = []
                for item in ['id_user', 'ds_application_name', 'ds_description', 'ds_link', 'ds_username',
                             'ds_password', 'ds_token', 'dt_creation_date', 'vl_expires', 'ck_enabled']:
                    if item not in response:
                        not_found.append(item)

                if len(not_found) > 0:
                    return None, AuthProviderException(f"Invalid Auth file data. Keys not found: {not_found}")
                return response, None
        except Exception as e:
            return None, AuthProviderException(f"Invalid exception: {e}")
