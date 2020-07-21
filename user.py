import uuid

from qiyu.createBaseData.login import *
from qiyu.createBaseData.common import *
import requests


kefugroup='data/corp1_user.txt'
logfile = open(kefugroup, 'w')

class user():
    def get_login(self):
        self.s,self.cookie,self.pagetoken =login().loginInfo()
        # print(self.cookie,self.pagetoken)

    def adduser(self,req,cookie,token,corpid,appkey,num):
        url = root_url + '/webapi/user/create.action'
        formTypeHeaders = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': cookie,
        }
        for i in range(0, num):
            deviceid = uuid.uuid4()
            body = {
                "appkey": appkey,
                "deviceid": str(deviceid),
                "token": token,
                "vipLevel": '1',
            }
            res = req.post(url, body, formTypeHeaders)
            # print(res.content)
            result = res.json().get('info')
            # print(result)
            logfile.write(
                '{"corp_id":"' + corpid + '","accid":"' + result.get('accid') + '","token":"' + result.get(
                    'token') + '","deviceId":"' + str(deviceid) + '"}' + '\n')


if __name__ == "__main__":
    ss = user()
    # ss.get_login()
    # ss.addKefuGroup()