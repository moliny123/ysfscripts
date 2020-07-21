import requests
from qiyu.createBaseData.common import *

class login():
    def loginInfo(self):
        login_url = root_url + '/api/kefu/login'
        login_body = {
            "username": username,
            "password": password,
            "autoLogin":"on",
            "terminalType": "0",
        }
        s = requests.session()
        res = s.post(login_url, login_body, formTypeHeaders)
        # print(res.content)
        cookie = res.headers.get('Set-Cookie')
        pagetoken = res.json().get('result').get('pageToken')
        # print(cookie)
        # print(pagetoken)
        return s,cookie,pagetoken


if __name__ == "__main__":
    ss = login()
    ss.loginInfo()
