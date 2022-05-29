# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 13:57
# @Author  : Amy
# @File    : 回车壁纸.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import requests
import time


class WallPaperSpider():
    def __init__(self):
        """初始化方法-魔法方法"""
        self.url = 'https://mm.enterdesk.com/'
        self.dir = 'MMimages'

    def get_html(self):
        """
        获取html代码：
        1.驱动
        2.等待
        3.获取
        """
        browser = webdriver.Chrome()
        browser.get(url=self.url)
        # 强制等待->睡着了->全部加载完还在等待
        # time.sleep(4)
        # 隐性等待->等待整个页面所有元素加载完毕->结束等待
        # 否则->等待超出10秒抛出异常
        # 弊端->等待整个页面所有元素加载完毕->没必要的js等
        # browser.implicitly_wait(10)
        # 显性等待->等待某元素加载完毕->结束等待
        wait = WebDriverWait(browser,10)
        # 传的是元祖
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
        ".egeli_pic_m ")))
        # 翻页
        # range(2)->0,1
        for i in range(2):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(3)

        # 获取页面
        pic_m = browser.find_element(By.CSS_SELECTOR,".egeli_pic_m")
        # print(pic_m)
        pic_li = pic_m.find_elements(By.CSS_SELECTOR,
        ".egeli_pic_li dl dd a img")
        # print(pic_li)   # []  遍历出来取src属性
        pic_list = []
        for pic in pic_li:
            img = dict()
            img['pic_url'] = pic.get_attribute('src')
            img['pic_title'] = pic.get_attribute('title')
            # print(img)
            pic_list.append(img)
            # yield img
        return pic_list



    def save_to_images(self, pic_list):
        # 创建文件夹
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        for pic in pic_list:
            img_path = os.path.join(self.dir, pic['pic_title']+'.jpg')
            res = requests.get(url=pic['pic_url'])
            with open(img_path,'wb') as f:
                f.write(res.content)
            print('正在保存第{}'.format(pic_list.index(pic)+1))

    def main(self):
        pic_list = self.get_html()
        self.save_to_images(pic_list)


if __name__ == '__main__':
    spider = WallPaperSpider()
    spider.main()
