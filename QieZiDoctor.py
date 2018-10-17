# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/12 18:38

from appium import webdriver
import time
from time import sleep

doctor = {
    "platformName":"Android",
    "deviceName":"127.0.0.1:62001",
    "platformVersion":"4.4",
    "androidPackage":"com.qiezzi.eggplan",
    "androidActivity":"com.qiezzi.eggplant.base.WelcomeActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",doctor)
#程序启动后休眠一会
time.sleep(19)
#获取屏幕的宽和高
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print width,height

#swipe从A点滑动至B点，滑动时间为毫秒 start_x起始位置， start_y起始位置， end_x结束位置, end_y结束位置, duration毫秒时长
driver.swipe(width-100,height/2,100,height/2,1000)
sleep(2)
driver.swipe(width-100,height/2,100,height/2,1000)
sleep(2)
driver.swipe(width-100,height/2,100,height/2,1000)

sleep(1)
driver.find_element_by_id("com.qiezzi.eggplant:id/btn_feel_right_now").click()
sleep(3)
driver.find_element_by_id("com.qiezzi.eggplant:id/edt_frist_login_accout").send_keys("18810609754")
driver.find_element_by_id("com.qiezzi.eggplant:id/edt_frist_login_password").send_keys("123456")
driver.find_element_by_id("com.qiezzi.eggplant:id/btn_frist_login_immediately").click()

