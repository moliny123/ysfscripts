from qiyu.createBaseData.login import *
from qiyu.createBaseData.common import *
import random


kefu='data/corp1_staff.txt'
logfile = open(kefu, 'w')

kefugroup='data/kefugroup.txt'
groupsinfile1=open(kefugroup, 'r')
kefugrouplist = []
for line in groupsinfile1.readlines():
    kefugrouplist.append(line.strip())
groupsinfile1.close()

class Kefu():
    def get_login(self):
        self.s,self.cookie,self.pagetoken =login().loginInfo()
        # print(self.cookie,self.pagetoken)

    def getMobile(self, i):
        mobile = '2' + str(151220) + str("%04d" % i)
        return mobile

    def getbody(self,i,password,token,groupId):
        username = "perftest" + str("%05d" % i)
        mobile = self.getMobile(i)
        email = username + '@163.com'
        body = {
            "token": token,
            "username": username,
            "realname":username,
            "nickname":username,
            "role":0,
            "mobile":mobile,
            "email":email,
            "theme":0,
            "isformal":1,
            "maxSession":20,
            "groupIds":groupId,
            "skillScoreChat":'',
            "skillScoreIpcc":'',
            "callEnable":'',
            "subRoleName":"普通客服",
            "subRoleId":4340403,
            "authority":'{"KEFU_CALL_OUT":0,"KEFU_CALL":0}',
            "defaultPortrait":"http://qiyukf.netease.com/sdk/res/default/robot_portrait.png",
            "portrait":'',
            "portraitName":'',
            "portraitSize":'',
            "password":password

        }
        return body

    def addKefu(self,req,cookie,token,num,groupIds):
        url = root_url + '/api/kefu/add'
        formTypeHeaders = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': cookie,
        }
        for i in range(0, num):
            groupId=kefugrouplist[random.randint(0,len(kefugrouplist)-1)].split(',')[0]
            body=self.getbody(i,password,token,groupId)
            res = req.post(url, body, formTypeHeaders)
            # print(res.content)
            result = res.json().get('result')
            print(result)
            logfile.write(str(result)+ '\n')

if __name__ == "__main__":
    ss = Kefu()
    # ss.get_login()
    # ss.addKefuGroup()