# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/15 10:17
from selenium import webdriver
import datetime
import time

#获取谷歌驱动
driver = webdriver.Chrome()
url='https://www.baidu.com'
driver.get(url)

def login(uname, pwd):
    # 获取京东链接
    driver.get("http://www.jd.com")
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[1]/div/div[1]/a").click()
    time.sleep(2)
    driver.get("https://item.jd.com/2338923.html")
    time.sleep(2)
    driver.find_element_by_link_text("加入购物车").click()
    time.sleep(3)
    driver.find_element_by_link_text("我的购物车").click()
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    time.sleep(2)

# buytime = '2016-12-27 22:31:00'
def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_id('order-submit').click()
            time.sleep(3)

        time.sleep(0.5)


# entrance
login('18268603978', 'asd6577+-..')
buy_on_time('2017-01-01 14:00:00')