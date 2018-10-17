# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/8 15:18
from selenium import webdriver

import datetime
import time

driver = webdriver.Chrome()
url='https://www.baidu.com'
driver.get(url)

def login(uname, pwd):
    driver.get("http://www.jd.com")
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(5)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()



def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_id('order-submit').click()
            time.sleep(3)

        time.sleep(0.5)


# entrance
login('18268603978', 'asd6577+-..')
buy_on_time('2018-10-08 16:00:00')

