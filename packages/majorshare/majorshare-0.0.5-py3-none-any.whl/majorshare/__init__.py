# -*- coding:utf-8 -*- 
import os

__version__ = '1.0.0'
__author__ = 'majorshare'


from majorshare.http_client import server_dict
from majorshare.upass import get_token, set_token,update_server_dict
update_server_dict(server_dict)

from majorshare.data_proxy import pro_api,pro_bar

