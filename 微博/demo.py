# @ Time    : 2019/4/24 16:54
# @ Author  : JuRan
from selenium import webdriver
# 配置文件作为一种可读性很好的格式，非常适用于存储程序中的配置数据
from configparser import ConfigParser
import time


# 打开浏览器  executable_path='./driver/chromedriver.exe'
wd = webdriver.Chrome()
# 设置窗口大小
# wd.set_window_size(1280,800)
wd.maximize_window()
# 输入网址
wd.get('http://www.baidu.com')
# 截图
wd.save_screenshot("baidu.png")
# 找到输入框
kw = wd.find_element_by_id('kw')
# 在输入框中输入酒店
kw.send_keys("酒店")
# 点击百度一下
wd.find_element_by_id('su').click()
time.sleep(3)
wd.quit()


# 实例化浏览器  executable_path='./driver/chromedriver.exe'
driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(10)

driver.set_window_size(1200,1000)
# 窗口最大化
# driver.maximize_window()

target = ConfigParser()
target.read('test.ini',encoding='utf-8')
pwd = target.get('weibo','password')
# 发送请求
# PC端模拟登陆
'''
driver.get('https://weibo.com/')
driver.find_element_by_id('loginname').send_keys('18646175116')

driver.find_element_by_xpath("//div[@class='info_list password']/div/input").send_keys('ycl1993.')
driver.find_element_by_xpath("//div[@class='info_list login_btn']/a").click()
'''
# 元素定位
driver.get('https://passport.weibo.cn/signin/login')
driver.find_element_by_id('loginName').send_keys('18646175116')
driver.find_element_by_id('loginPassword').send_keys(pwd)
driver.find_element_by_id('loginAction').click()
driver.find_element_by_id("getCode").click()





