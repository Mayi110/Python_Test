# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/15 8:59
#导入appium包下的webdriver
from selenium import webdriver
import time
import datetime

#获取谷歌驱动
driver = webdriver.Chrome()
url='https://www.baidu.com'
driver.get(url)
#获取京东链接
driver.get("https://www.jd.com/")
time.sleep(2)
driver.find_element_by_link_text("你好，请登录").click()
time.sleep(3)
driver.find_element_by_link_text("账户登录").click()
time.sleep(5)
driver.find_element_by_id("lodinname").send_keys("18268603978")
driver.find_element_by_id("password").send_keys("asd6577+-..")
driver.find_element_by_id("loginsubmit").click()

