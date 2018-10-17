# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/9 18:39
from appium import webdriver

search = {
    "platformName":"Android",
    "platformVersion":"19 ",
    "deviceName":"127.0.0.1:62001",
    "androidPackage":"com.example.login",
    "androidActivity":"com.example.login.MainActivity"
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",search)
driver.find_element_by_id("com.example.login:id/et_username").send_keys("123456")
driver.find_element_by_id("com.example.login:id/et_password").send_keys("123456")
driver.find_element_by_class_name("android.widget.Button").click()
