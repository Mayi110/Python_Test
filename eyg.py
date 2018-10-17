# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/9 8:41
import time

import datetime
from selenium import webdriver
#  获取谷歌驱动
driver = webdriver.Chrome()

driver.get('https:www.jd.com/')
class JDLOGIN(object):
    def login_jd(self,num,pwd):
        driver.find_element_by_link_text('你好，请登录').click()
        time.sleep(5)
        driver.find_element_by_link_text('账户登录').click()
        time.sleep(3)
        driver.find_element_by_id('loginname').send_keys(num)
        driver.find_element_by_id('nloginpwd').send_keys(pwd)
        time.sleep(3)
        driver.find_element_by_id('loginsubmit').click()
        time.sleep(5)
        nowwhandle = driver.current_window_handle
        driver.find_element_by_link_text('秒杀').click()
        time.sleep(3)
        driver.find_element_by_link_text('立即抢购').click()


    def start(self,num,pwd,buytime):
        self.login_jd(num,pwd)
        self.buy_on_time(buytime)
jdlogin=JDLOGIN()
jdlogin.start('18268603978','asd6577+-..','2018-10-09' )