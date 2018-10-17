# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/17 11:07
#####上传头像
import unittest
from Interface_Test.user import uploadpic


class UploadPicUnit(unittest.TestCase):
    #初始化对象
    @classmethod
    def setUpClass(cls):
        cls.uploadpic = uploadpic.UploadPicControl()

    def test_UploadPic(self):
        self.response = self.uploadpic.uploadpic_Success()
        print self.response