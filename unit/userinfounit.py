# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/17 11:21
#####获取用户信息
import unittest

from Interface_Test.user import userinfo


class UserInfoUnit(unittest.TestCase):
    # 初始化对象的方法
    @classmethod
    def setUpClass(cls):
        cls.userinfo = userinfo.UserInfoControl()

    def test_UserInfo(self):
        self.response = self.userinfo.getUserinfo_Success()
        print self.response

        self.icon = self.userinfo.getIcon()
        print self.icon