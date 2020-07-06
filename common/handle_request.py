# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/3 8:44

import requests


class HandleRequest:
    def send(self, url, method, params=None, data=None, json=None, headers=None):
        # 将请求的方法转换为小写
        method = method.lower()
        if method == "post":
            return requests.post(url=url, json=json, data=data, headers=headers)
        elif method == "patch":
            return requests.patch(url=url, json=json, data=data, headers=headers)
        elif method == "get":
            return requests.get(url=url, params=params, headers=headers)


class HandleSessionRequest:
    """使用session鉴权的接口，使用这个类类发送请求"""

    def __init__(self):
        self.se = requests.session()

    def send(self, url, method, params=None, data=None, json=None, headers=None):
        # 将请求的方法转换为小写
        method = method.lower()
        if method == "post":
            return self.se.post(url=url, json=json, data=data, headers=headers)
        elif method == "patch":
            return self.se.patch(url=url, json=json, data=data, headers=headers)
        elif method == "get":
            return self.se.get(url=url, params=params)


if __name__ == '__main__':
    # 登录接口地址
    login_url = "http://api.lemonban.com/futureloan/member/login"

    # 登录的参数
    login_data = {
        "mobile_phone": "15867554893",
        "pwd": "123456qwe",
    }
    # 登录的请求头
    header = {
        "X-Lemonban-Media-Type": "lemonban.v2",
        "Content-Type": "application/json"
    }

    http = HandleRequest()
    res = http.send(url=login_url, method="post", json=login_data, headers=header)
    print(res.json())
