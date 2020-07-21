from qiyu.createBaseData.common import *
from qiyu.createBaseData.login import *
from qiyu.createBaseData.KefuGroup import *
from qiyu.createBaseData.Kefu import *
from qiyu.createBaseData.user import *
from qiyu.createBaseData.sessionCategory import *
from qiyu.createBaseData.worksheetCategory import *
from qiyu.createBaseData.robotKnowledge import *
#登录
req,cookie,pagetoken =login().loginInfo()
print(cookie)
print(pagetoken)
KefuGroup_num=2 #客服分组的个数
kefu_num=2 #客服的个数
user_num=2 #用户的个数

# KefuGroup().addKefuGroup(req,cookie,pagetoken,KefuGroup_num)
# Kefu().addKefu(req,cookie,pagetoken,kefu_num)
# user().adduser(req,cookie,pagetoken,corpid,appkey,user_num)
# sessionCategory().sessioncategory(req,cookie,pagetoken)
#worksheetCategory().worksheetcategory(req,cookie,pagetoken)#error
# robotKnowledge().addcategory(req, cookie, pagetoken)
# robotKnowledge().addquestion(req, cookie, pagetoken)