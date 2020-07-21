import uuid

from qiyu.createBaseData.login import *
from qiyu.createBaseData.common import *
import requests
import time,random,json


robotCategory='data/robotCategory.txt'
robotCategory_logfile = open(robotCategory, 'w')
robotQuestion='data/robotQuestion.txt'
robotQuestion_logfile = open(robotQuestion, 'w')

class robotKnowledge():
    def get_login(self):
        req, cookie, pagetoken=self.s,self.cookie,self.pagetoken =login().loginInfo()
        # print(cookie)
        # print(pagetoken)
        return req, cookie, pagetoken
        # print(self.cookie,self.pagetoken)

    def getRobot(self,req,token,formTypeHeaders):
        formTypeHeaders = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': cookie,
        }
        url = root_url + '/robot/api/robotlist/getNew?token=' + token
        resut = requests.get(url,headers=formTypeHeaders)
        robotlist=resut.json().get('result')[0].get('robotList')
        # print(robotlist)
        robotIdList=[]
        for info in robotlist:
            robotIdList.append(info.get('robotId'))
        return robotIdList

    def addcategory(self,req,cookie,token):
        url = root_url + '/robot/api/category/list/set?token='+token
        jsonHeaders = {
            'Content-Type': "application/json",
            'Cookie': cookie,
            'Accept':"application/json",
            'Content-Length':"905"
        }
        nowtime = int(time.time() * 1000)
        robotIdList=self.getRobot(req,token,formTypeHeaders)
        # print(robotIdList)
        for robot in robotIdList:
            body = '{"robotId":%s,"id":0,"time":%s,"list":[{"name":"perftest1"},{"name":"perftest2"},{"name":"perftest3"},{"name":"perftest4"},{"name":"perftest5"},{"name":"perftest6"},{"name":"perftest7"},{"name":"perftest8"},{"name":"perftest9"}]}' % (robot, nowtime)
            data = req.post(url, data=body.encode('utf-8'), headers=jsonHeaders)
            # print(data.content)
            result = data.json().get('result')
            # print(result)

    def getcategory(self,req,token):
        formTypeHeaders = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': cookie,
        }
        robotIdList = self.getRobot(req, token, formTypeHeaders)
        robotCategory={}
        for robot in robotIdList:
            categoryId=[]
            url = root_url + '/robot/api/category/list/get?robotId='+ str(robot) + '&token=' + token
            data = req.get(url, headers=formTypeHeaders)
            result = data.json().get('result')
            for i in result:
                categoryId.append(i.get('id'))
            robotCategory.setdefault(robot,categoryId)
        return robotCategory

    def addquestion(self, req, cookie, token):
        formTypeHeaders = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': cookie,
        }
        url = root_url + '/robot/api/knowledge/question/add?token=' + token
        categoryMap=self.getcategory(req,token)
        standard=['商品怎么咨询','你好，考拉原因重新购买的差价问题？','你好，双十一工作时间？','你好，工作时间？','你好，如何办理黑卡会员？','你好，如何办理会员？','你好，如何申请退差价？','你好，如何申请退款？','你好，双休日正常发货吗？','你好，多长时间发货？','你好，超级品牌联盟活动什么时候开始？','你好，双十一有活动吗？','你好，搞活动的是正品？','你好，七鱼客服工作时间？','你好，网易考拉直营吗？','商品可以保修吗？','国行商品怎么维修？','有哪些商品是只换不修服务？','页面怎么打不开?','网易白条如何查看是否受邀?']
        i=0
        for key in categoryMap:
            categoryList=categoryMap.get(key)
            for categoryId in categoryList:
                # body = {"robotId": key,
                #         "categoryId": categoryId,
                #         "standard":'商品怎么咨询',
                #         "foreignAnswer":'test',
                #         "internalAnswer":'test',
                #         "isAnswerRich":'0',
                #         "validitySwitch":'1'
                # }
                body="similars=&standard="+standard[i]+"&foreignAnswer=perftest&categoryId="+str(categoryId)+"&validitySwitch=1&internalAnswer=perftest&robotId="+str(key)+"&isAnswerRich=0"
                # body="title = 555 & content = 5555 & categoryId = 592193 & validitySwitch = 1 & robotId = 57001"
                data = req.post(url, data=body.encode('utf-8'), headers=formTypeHeaders)
                questionId = data.json().get('result')
                print(questionId)
                robotQuestion_logfile.write(str(questionId)+ ',' + str(categoryId) + ',' + str(key) + '\n')
                i=i+1

    def addpoint(self, req, cookie, token):
        formTypeHeaders = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': cookie,
        }
        url = root_url + '/robot/api/knowledge/point/add?token=' + token
        categoryMap = self.getcategory(req, token)
        title = ['test','test2','test3','test4']
        i = 0
        for key in categoryMap:
            categoryList = categoryMap.get(key)
            for categoryId in categoryList:
                tmp = random.randint(1, 1000)
                body="title=perf"+ str(tmp) +"&content=perftest&categoryId="+str(categoryId)+"&validitySwitch=1&robotId="+str(key)
                data = req.post(url, data=body.encode('utf-8'), headers=formTypeHeaders)
                pointId = data.json().get('result')
                # print(pointId)
                # i = i + 1


if __name__ == "__main__":
    ss = robotKnowledge()
    req, cookie, pagetoken=ss.get_login()
    # ss.addcategory(req, cookie, pagetoken)
    # ss.addquestion(req, cookie, pagetoken)
    ss.addpoint(req, cookie, pagetoken)