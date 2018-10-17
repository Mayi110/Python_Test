# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/10 11:29
from appium import webdriver

calculator = {
    "platformName":"Android",
    "platformVersion":"19 ",
    "deviceName":"127.0.0.1:62001",
    "androidPackage":"com.bwei.telephone",
    "androidActivity":"com.bwei.telephone.MainActivity"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",calculator)
driver.find_element_by_id("com.bwei.telephone:id/txt9").click()
#加号
driver.find_element_by_id("com.bwei.telephone:id/txtPlus").click()
driver.find_element_by_id("com.bwei.telephone:id/txt8").click()
#等号
driver.find_element_by_id("com.bwei.telephone:id/txtIs").click()
#除号
driver.find_element_by_id("com.bwei.telephone:id/txtMul").click()
driver.find_element_by_id("com.bwei.telephone:id/txt5").click()
driver.find_element_by_id("com.bwei.telephone:id/txtIs").click()