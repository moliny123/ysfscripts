import uuid

from qiyu.createBaseData.login import *
from qiyu.createBaseData.common import *
import requests
import time,random


sessionCategory='data/sessionCategory.txt'
logfile = open(sessionCategory, 'w')

class sessionCategory():
    def get_login(self):
        self.s,self.cookie,self.pagetoken =login().loginInfo()
        # print(self.cookie,self.pagetoken)

    def getBody(self, categoryid, categoryname, num):
        nowtime = int(time.time() * 1000)
        content = {}
        content_tmp = {}
        if (categoryid == 0):
            body = []
            for i in range(0,11):  # 默认一级分类创建十个
                content_tmp = {}
                content_tmp.setdefault('name', 'perfsessioncategory_' + str(i))
                body.append(content_tmp)
                num = num + 1
            content.setdefault("id", categoryid)
            content.setdefault('list', body)
            content.setdefault('time', nowtime)
        else:
            body = []
            m = random.randint(0, 5)  # 二级以下分类个数随机创建，最多不超过10个
            for i in range(m):
                content_tmp = {}
                content_tmp.setdefault('name', categoryname + '_' + str(i))
                body.append(content_tmp)
                num = num + 1
            content.setdefault("id", categoryid)
            content.setdefault('list', body)
            content.setdefault('time', nowtime)
        json = content
        return str(json), num


    def sessioncategory(self,req,cookie,token):
        url = root_url + '/api/category/list/set?token='+token
        formTypeHeaders = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': cookie,
        }
        num = 0
        categoryidlist = [0]
        categorynamelist = ['']
        for i in range(5):
            categoryidlist_tmp = []
            categorynamelist_tmp = []
            for j in range(len(categoryidlist)):
                categoryid = categoryidlist[j]
                categoryname = categorynamelist[j]
                body, num = self.getBody(categoryid, categoryname, num)
                print(body)
                print(num)
                data = req.post(url, body, formTypeHeaders)
                print(data)
                # if(num>=1200): break
                result = data.json().get('result')
                for n in range(len(result)):
                    categoryid_tmp = result.getJSONObject(n).get('id')
                    categoryname_tmp = result.getJSONObject(n).get('name')
                    categoryidlist_tmp.append(categoryid_tmp)
                    categorynamelist_tmp.append(categoryname_tmp)
                    logfile.write(str(categoryid_tmp) + ',' + categoryname_tmp + ',' + str(
                        categoryid) + ',' + categoryname + ',' + str(i) + '\n')  # 分类结果统计格式：分类id，分类名，父类id，父类名，级别
            if (num >= 1200): break
            print(num)
            categoryidlist = categoryidlist_tmp
            categorynamelist = categorynamelist_tmp



if __name__ == "__main__":
    ss = sessionCategory()
    # ss.get_login()
    # ss.sessionCategory()