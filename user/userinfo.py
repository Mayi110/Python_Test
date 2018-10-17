# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/17 11:14
#####获取用户信息
import requests

from Interface_Test.api import url
from Interface_Test.user import login


class UserInfoControl(object):
    # 初始化对象的方法
    def __init__(self):
        self.URL = url.URL()
        self.userinfo = self.URL.base_online_url + self.URL.userinfo
        self.login = login.LoginControl()
    # 获取用户信息的网络请求
    def getUserinfo_Success(self):
        self.login.login_Success()
        self.uid = self.login.getUid()
        self.token = self.login.getToken()
        data={
            'uid':self.uid,
            'token':self.token
        }
        self.response = requests.post(url=self.userinfo,data=data).json()
        return self.response
    # 解析数据得到data
    def getData(self):
        self.data = self.response['data']
        return self.data

    def getIcon(self):
        self.icon = self.getData()['icon']
        return self.icon