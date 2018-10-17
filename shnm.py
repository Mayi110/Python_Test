# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/7 19:22
from selenium import webdriver
#获取谷歌驱动
path = webdriver.Chrome()
url = 'https://www.baidu.com'
path.get(url)

