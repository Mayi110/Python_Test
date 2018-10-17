# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/16 14:20
#####注册
        #插件
import requests

from Interface_Test.api import url


class RegisterControl(object):
    # 初始对象
    def __init__(self):
    # 得到对象
     self.URL = url.URL()
    # 调用对象中属性得到注册的接口地址
     self.register = self.URL.base_test_url+self.URL.register

    # 注册的网络请求
    def register_Success(self):
        # 封装参数
        data={
            'mobile':'18813605623',
            'password':'123456'}
        # 得到响应数据
        self.response = requests.post(url=self.register,data=data).json()

        # 返回结果数据
        return self.response
    # 获取code值
    def getCode(self):
        self.code = self.response['code']
        return self.code

    # 获取msg值
    def getMsg(self):
        self.msg = self.response['msg']
        return self.msg