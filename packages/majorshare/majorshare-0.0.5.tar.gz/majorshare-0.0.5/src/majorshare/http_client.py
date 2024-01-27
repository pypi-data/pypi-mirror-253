# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
majors数据API接口 
Created on 2023/08/08
@author: majors
"""

import pandas as pd
import json
from functools import partial
import requests

server_dict = {"mjsapi":"http://mjsapi.majors.ltd:7000",
               "tsapi":"http://tsapi.majors.ltd:7000",
              "mjshis":"http://mjshis.majors.ltd:7000",
              "mjsrt":"http://mjsrt.majors.ltd:7000"}


class DataApi:

    __token = ''
    __http_url = 'http://mjsapi.majors.ltd:7000'
    __Appoint_url = ''

    def __init__(self, token='', server='', timeout=20):
        """
        Parameters
        ----------
        token: str
            API接口TOKEN，用于用户认证
        """
        if 'http' in server:
            self.__Appoint_url = server
        elif server in server_dict:
            self.__Appoint_url = server_dict[server]
        self.__token = token
        self.__timeout = timeout

    def query(self, api_name, fields='', **kwargs):
        req_params = {
            'api_name': api_name,
            'token': self.__token,
            'params': kwargs,
            'fields': fields
        }
        if self.__Appoint_url:
            res = requests.post(self.__Appoint_url, json=req_params, timeout=self.__timeout, headers={'Connection':'close'})
        else:
            if ("get_his_" in api_name) or ("get_" in api_name):
                self.__http_url = server_dict["mjshis"]
                if ("get_rt_" in api_name):
                    self.__http_url = server_dict["mjsrt"]
            else:
                self.__http_url = 'http://mjsapi.majors.ltd:7000'
            res = requests.post(self.__http_url, json=req_params, timeout=self.__timeout, headers={'Connection':'close'})
        result = json.loads(res.text)
        if result['code'] != 0:
            raise Exception(result['msg'])
        data = result['data']
        columns = data['fields']
        items = data['items']
        if columns:
            return pd.DataFrame(items, columns=columns)
        else:
            return data['items']

    def __getattr__(self, name):
        return partial(self.query, name)
