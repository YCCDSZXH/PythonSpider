# !/usr/bin/env python  # windows环境,没用
# -*- coding:utf-8 -*-  # Python3,没有

# 1. 导入我们的第三方测试模块和时间模块
from selenium import webdriver
import time

# 2. 创造一个浏览器对象
chrome = webdriver.Chrome()
# 3. 输入要访问的网址
chrome.get('http://www.taobao.com/')
# 4. 找到搜索框的唯一标示,并且给他一个变量保存可操作对象
search_ele = chrome.find_element_by_id('q')
# 4.1 输入我们要找的关键字.
search_ele.send_keys(u'笔记本电脑')
# 5. 找到对应ID的操作按钮标识,并且用变量保存按钮对象
search_btn = chrome.find_element_by_class_name('btn-search')
# 6. 点击按钮对象
search_btn.click()
# 7. 创建一个文件
file = open('shops.txt', 'wb')
# 8, 生成要翻页的页数.
for i in range(1, 11):
    print('正在爬取第 {} 页数据'.format(i))
    # 控制浏览器的滚动条,让他加载数据
    for x in range(1, 11, 2):
        # 等待浏览器加载数据
        time.sleep(0.5)
        # 计算我们拖动的距离
        j = x/10
        # 用变量保存我们的js语句,并且把坐标距离填入到语句中
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        # 执行js代码
        chrome.execute_script(js)

    # 浏览器滚动结束以后,开始取出数据
    # 找到所有的class叫info-cont的标签
    conts = chrome.find_elements_by_class_name('info-cont')
    # 遍历我们取出来的数据,取出每一个商品的信息
    for data in conts:
        # print(MNIST_data)
        # 用utf-8的编码格式,向文件里面写入文本数据
        file.write(data.text.encode('utf-8'))

    # 用xpath的语法去找到网页中的按钮标签
    # 判断一下这个标签是否存在
    try:  # 异常处理
        # if chrome.find_element_by_xpath('//div[@title="取消浮动跟随"]'):
        element_xpath = chrome.find_element_by_xpath('//div[@title="取消浮动跟随"]')
        element_xpath.click()
    except:
        pass

    # 实现翻页的功能
    # 找到我们下一页的按钮,给他一个变量保存
    search_text = chrome.find_element_by_link_text('下一页')
    # 点击下一页按钮
    search_text.click()

# 关闭文件
file.close()

# 关闭浏览器
chrome.close()