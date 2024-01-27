# -*- coding:utf-8 -*- 
"""
majors数据API接口 
Created on 2023/08/08
@author: majors
"""

import os
import requests
import threading


TOKEN_FILE = 'majorshare_token.txt'


def set_token(token):
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, TOKEN_FILE)
    with open(fp, 'w') as file:
        file.write(token)
    print("token文件已存储至 ",fp)
    
def get_token():
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, TOKEN_FILE)
    try:
        with open(fp, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"默认路径 {fp} 未发现token文件，如不小心清除，请使用set_token(token)重新设置")
        return None
    
def update_server_dict(server_dcit):
    def update(server_dcit):
        url = "http://mjsapi.majors.ltd:7000/get_server_dict"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()  # 将响应的 JSON 数据转换为字典
                if len(data)>=4:
                    server_dcit.update(data)
            else:
                pass
        except Exception as e:
            pass
        
    thread = threading.Thread(target=update,args=(server_dcit,))
    thread.start()
    thread.join(5)  # 等待线程结束，超时时间为 5 秒
    if thread.is_alive():
         return False
         thread.terminate()  
    return True