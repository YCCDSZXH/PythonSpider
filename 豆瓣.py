#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 21:22
# @Author  : Jerry
# @File    : 豆瓣.py
# @Software: PyCharm

# 需求：爬取电影的名字 评分 引言 详情页的url，每一页都爬取并且把数据保存到csv文件当中

import requests
from lxml import etree
import csv

# 第一步获取网页源码
# def getSource():
#     # 反爬 填写headers请求头
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
#     }
#
#     response = requests.get('https://movie.douban.com/top250?start=0&filter=',headers=headers)
#
#     print(response.text)
#
#
# getSource()

# https://movie.douban.com/top250?start=25&filter= 第二页
# https://movie.douban.com/top250?start=50&filter= 第三页
# https://movie.douban.com/top250?start=75&filter= 第四页
# （page-1）* 25
doubanUrl = 'https://movie.douban.com/top250?start={}&filter='


# 第一步获取网页源码
def getSource(url):
    # 反爬 填写headers请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    # 防止出现乱码
    response.encoding = 'utf-8'
    # print(response.text)
    return response.text

# 第二步定义一个函数 获取电影信息
def getEveryItem(source):


    html_element = etree.HTML(source)

    movieItemList = html_element.xpath('//div[@class="info"]')

    # 定义一个空的列表
    movieList = []

    for eachMoive in movieItemList:

        # 创建一个字典 像列表中存储数据[{电影一},{电影二}......]
        movieDict = {}

        title = eachMoive.xpath('div[@class="hd"]/a/span[@class="title"]/text()') # 标题
        otherTitle = eachMoive.xpath('div[@class="hd"]/a/span[@class="other"]/text()')  # 副标题
        link = eachMoive.xpath('div[@class="hd"]/a/@href')[0]  # url
        star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0] # 评分
        quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')  # 引言（名句）

        if quote:
            quote = quote[0]
        else:
            quote = ''
        # 保存数据
        movieDict['title'] = ''.join(title+otherTitle)
        movieDict['url'] = link
        movieDict['star'] = star
        movieDict['quote'] = quote

        movieList.append(movieDict)

        print(movieList)
    return movieList

# 保存数据
def writeData(movieList):

    with open('douban.csv','w',encoding='utf-8',newline='') as f:

        writer = csv.DictWriter(f,fieldnames=['title','star','quote','url'])

        writer.writeheader() # 写入表头

        for each in movieList:

            writer.writerow(each)


if __name__ == '__main__':
    movieList = []

    # 一共有10页

    for i in range(10):

        pageLink = doubanUrl.format(i * 25)


        source = getSource(pageLink)

        movieList += getEveryItem(source)


    writeData(movieList)











