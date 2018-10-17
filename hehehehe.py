# _*_ coding: utf-8 _*_
# 作者    ： ZhangMengke
# 创建时间： 2018/10/11 13:21
#导入appium包下的webdriver
from appium import webdriver
#导入单元测试的包
import unittest
#导入os文件路径包
import os
#导入时间包
import time
#导入第三方生成测试报告包
import HTMLTestRunner
#导入邮件包
import smtplib
#导入邮件文本包
from email.mime.text import  MIMEText
#导入邮件头包
from email.header import Header

#定义单元测试类
class CalculateTest(unittest.TestCase):
    # 只初始化一次，并不是每次用例执行都进行初始化
    @classmethod #注解修饰类方法
    def setUpClass(cls):
        calculator = {
              'platformName': 'Android',  # 平台
              'deviceName': '127.0.0.1:62001',  # 设备
              'platformVersion': '19',  # 设备的系统版本
              'appPackage': 'com.bwei.telephone',  # 程序的包名
              'appActivity': 'com.bwei.telephone.MainActivity'  # 程序的启动activity
          }
        # 通过驱动远程接连appium服务并添加配置信息
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", calculator)

    def test_add(self):
        self.driver.find_element_by_name('9').click()
        self.driver.find_element_by_id('com.bwei.telephone:id/txtPlus').click()
        self.driver.find_element_by_name('1').click()
        self.driver.find_element_by_name('=').click()
        result = self.driver.find_element_by_id('com.bwei.telephone:id/output').text
        # 设置断言，不然不管对错，最后得出的报告统统PASS，那就尴尬了。text的属性为str，断言内容在这前后格式要相同，不然得出的报告全部FAIL，那也尴尬了。
        self.assertEqual(result, str(10.0))
        self.driver.find_element_by_name('AC')# 最后一定要清空，为下一个用例作准备

    def test_substract(self):
        self.driver.find_element_by_name('9').click()
        self.driver.find_element_by_id('com.bwei.telephone:id/txtMinus').click()
        self.driver.find_element_by_name('1').click()
        self.driver.find_element_by_name('=').click()
        result = self.driver.find_element_by_id("com.bwei.telephone:id/output").text
        print("test_substract:" + result)
        self.assertEqual(result, str(8.0))
        self.driver.find_element_by_name('AC')

    def test_multi(self):
       self.driver.find_element_by_name('9').click()
       self.driver.find_element_by_id('com.bwei.telephone:id/txtMul').click()
       self.driver.find_element_by_name('9').click()
       self.driver.find_element_by_name('=').click()
       result = self.driver.find_element_by_id("com.bwei.telephone:id/output").text
       print("test_multi:" + result)
       self.assertEqual(result, str(81.0))
       self.driver.find_element_by_name('AC')

    def test_div(self):
       self.driver.find_element_by_name('9').click()
       self.driver.find_element_by_id('com.bwei.telephone:id/txtDiv').click()
       self.driver.find_element_by_name('3').click()
       self.driver.find_element_by_name('=').click()
       result = self.driver.find_element_by_id("com.bwei.telephone:id/output").text
       print("test_div:" + result)
       self.assertEqual(result, str(3.0))
       self.driver.find_element_by_name('AC').click()

    #结束脚本
    @classmethod #注解修饰类方法
    def tearDownClass(cls):
           cls.driver.quit()

#======定义发送邮件========
def send_mail(report_path):
    #读取测试报告
    f=open(report_path,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header('手机计算器自动化测试报告','utf-8')
    #这里使用 简单邮件协议
    smtp=smtplib.SMTP()
    smtp.connect('smtp.qq.com',25)
    smtp.login('1605895640@qq.com','nxcamnldhhsphbhf')#不是你的邮箱登录密码，而是你登录成功之后设置授权码
    smtp.sendmail('1605895640@qq.com','1605895640@qq.com',msg.as_string())
    smtp.quit()
    print ('邮件已发出！注意查收。')

#======查找测试目录，找到最新生成的测试报告======

def new_report(test_report):
    lists=os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report+'\\'+fn))
    file_new=os.path.join(test_report,lists[-1])
    print (file_new)
    return file_new

#定义主方法
if __name__=='__main__':
    #添加单元测试到测试套件中
    cal_suit= unittest.makeSuite(CalculateTest,"test")
    path = os.getcwd()  # 此脚本的父级目录
    report_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    report_name = path + '\\report\\' + report_time + '-report.html'  # 报告保存路径及名称
    #写入
    with open(report_name, 'wb') as fp:
       # 生成报告未HTML格式，
       runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'手机计算器测试报告', description=u'用例执行情况')
       runner.run(cal_suit)  # 开始执行生成测试报告
    #此方法是获取测试报告的所在目录路径
    new_report = new_report(path + '\\report\\')
    #此方法根据测试报告所在目录路径发送邮件
    send_mail(new_report)