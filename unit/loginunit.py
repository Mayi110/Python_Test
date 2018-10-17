# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/17 10:33
#####  登录
import unittest
from Interface_Test.user import login

class LoginUnit(unittest.TestCase):
    # 单元测试的初始化方法
    @classmethod
    def setUpClass(cls):
        cls.login = login.LoginControl()

    def test_Login(self):
        self.response = self.login.login_Success()
        print self.response

        self.uid = self.login.getUid()
        self.token = self.login.getToken()
        print self.uid,self.token

        self.assertEqual("21387",str(self.uid))