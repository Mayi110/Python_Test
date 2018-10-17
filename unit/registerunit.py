# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/16 14:35
#####  注册单元测试
import unittest
from Interface_Test.user import register

class RegisterUnit(unittest.TestCase):
    # 初始化注册对象
    @classmethod
    def setUpClass(cls):
        cls.register = register.RegisterControl()
    # 对注册请求进行单元测试
    def test_Register(self):
        self.response = self.register.register_Success()
        print(self.response)
        # 断言-判断结果是否相等
        self.assertEqual('1',self.register.getCode())