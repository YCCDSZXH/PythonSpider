#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 20:45
# @Author  : Jerry
# @File    : 练习爬取天气.py
# @Software: PyCharm

# 需求:爬取全国所有的城市名称以及对应的气温
# http://www.weather.com.cn/textFC/hb.shtml 华东 分析其他区域的url规律


import requests

from bs4 import BeautifulSoup

# 定义一个函数来解析网页
def parse_page(url):

    response = requests.get(url)
    # 解决乱码
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib') # pip install html5lib
    # 网页接卸
    # 一、class="conMidtab"
    conMidtab = soup.find('div',class_='conMidtab')
    # print(conMidtab)
    # 二、table
    tables = conMidtab.find_all('table')
    # print(tables)

    for table in tables:
        # print(table)
        # 三、tr 过滤掉去前2个
        trs = table.find_all('tr')[2:]
        # enumerate 返回2个值第一个是下标 第二个下标所对应的元素
        for index,tr in enumerate(trs):
            # print(tr)
            tds = tr.find_all('td')

            # 判断
            city_td = tds[0] # 城市

            if index == 0:
                city_td = tds[1] # 省会


            # 获取一个标签下面的子孙节点的文本信息
            city = list(city_td.stripped_strings)[0]

            temp_td = tds[-2]
            temp = list(temp_td.stripped_strings)[0]
            print('城市:',city,'温度:',temp)
        # break # 先打印北京

    # 四、td

    # print(text)


def main():

    url = 'http://www.weather.com.cn/textFC/hb.shtml' # 华东
    # url = 'http://www.weather.com.cn/textFC/db.shtml' # 东北
    url = 'http://www.weather.com.cn/textFC/gat.shtml' # 港澳台

    urls = ['http://www.weather.com.cn/textFC/hb.shtml','http://www.weather.com.cn/textFC/db.shtml' ,'http://www.weather.com.cn/textFC/gat.shtml']

    for url in urls:
        parse_page(url)


if __name__ == '__main__':


    main()