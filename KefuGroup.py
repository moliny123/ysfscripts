from qiyu.createBaseData.login import *
from qiyu.createBaseData.common import *
import requests


kefugroup='data/kefugroup.txt'
logfile = open(kefugroup, 'w')

class KefuGroup():
    def get_login(self):
        self.s,self.cookie,self.pagetoken =login().loginInfo()
        # print(self.cookie,self.pagetoken)

    def addKefuGroup(self,req,cookie,token,num):
        url = root_url + '/api/kefuGroup/add?token=' + token
        formTypeHeaders = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': cookie,
        }
        for i in range(0, num):
            groupname = '2154group' + str(i)
            body = {
                "name": groupname,
            }
            res = req.post(url, body, formTypeHeaders)
            # print(res.content)
            result = res.json().get('result')
            print(result)
            logfile.write(str(result.get('id')) + '||' + result.get('name') + '\n')

if __name__ == "__main__":
    ss = KefuGroup()
    # ss.get_login()
    # ss.addKefuGroup()