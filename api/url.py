# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/16 14:19

class URL(object):
    #测试环境的接口地址
    base_test_url ="http://120.27.23.105"
    #生产环境的接口地址
    base_online_url ="https://www.zhaoapi.cn"

    #注册
    register = "/user/reg"
    #登录
    login="/user/login"
    #获取用户信息
    userinfo="/user/getUserInfo"
    # 上传头像
    upload_pic = "/file/upload"