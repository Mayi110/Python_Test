# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/9 15:49
from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()
# http://gate.jd.com/InitCart.aspx?pid=4993737&pcount=1&ptype=1

def login(username, password):
    driver.get("https://passport.jd.com/new/login.aspx")
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(username)
    driver.find_element_by_name("nloginpwd").send_keys(password)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[1]/div/div[1]/a").click()
    time.sleep(3)
    driver.get("https://item.jd.com/3509912.html")
    time.sleep(3)
    driver.find_element_by_link_text("加入购物车").click()
    time.sleep(3)
    # driver.find_element_by_link_text("我的购物车").click()
    # time.sleep(3)
    # time.sleep(3)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()
    # now_time = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('login success, you can ou up!')


def buy_on_time(buytime):
    # buy_on_time 函数处设置秒杀时间
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_id('order-submit').click()
            time.sleep(3)
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('purchase success')
            time.sleep(3)

login('18268603978', 'asd6577+-..')
buy_on_time('2018-10-9 15:30:00')
