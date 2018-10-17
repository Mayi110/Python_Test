# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/17 10:57
#####上传头像
import requests

from Interface_Test.api import url
from Interface_Test.user import login


class UploadPicControl(object):
    # 初始化对象
    def __init__(self):
        self.URL = url.URL()
        self.uploadpic = self.URL.base_online_url + self.URL.upload_pic
        self.login = login.LoginControl()
    # 上传头像网络请求
    def uploadpic_Success(self):
        self.login.login_Success()
        self.uid = self.login.getUid()
        data={'uid':self.uid}
        files = {'file':('h.jpg',open('C:\Users\ZhangMengke\Desktop\h.jpg','rb'),'image/jpg')}
        self.response = requests.post(url=self.uploadpic,data=data,files=files).json()
        return self.response