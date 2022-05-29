# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 14:01
# @Author  : Amy
# @File    : 汽车之家.py

import requests  # pip install requests  发送请求
from lxml import etree  # lxml
from fontTools.ttLib import TTFont


url = "https://club.autohome.com.cn/bbs/thread/665330b6c7146767/80787515-1.html"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}

# **kwargs 动态参数 可传可不传 要传-->字典
res = requests.get(url=url,headers=headers)

# 获取的网页源码
res_html = res.text
# print(res_html)

# 解析数据-->获取需要的数据-->浏览器转码了..字出现了
html = etree.HTML(res_html)
# //非根节点 标签[@属性名称="属性值"]
content_list = html.xpath('//div[@class="tz-paragraph"]//text()')
# print(content_list)  # list

'''
list 里面的 元素  拼接成 字符串  str.join()
字符串将 二进制 隐藏 但乱码 还存在
'''
content_str = "".join(content_list)  # 将 列表中 每个 元素 以 空字符串 的 连接起来
# print(content_str)

'''
\uedff --> 一

字体反爬  比如:猫眼 大众点评
实际上字体反爬的意思就是
通过调用自定义的ttf文件来渲染网页中的文字，而网页中的文字不再是文字，而是相应的字体编码。
也就是说 后端 是编码  前端 是根据 编码 显示 字  调虎离山之计


如何破解 打开百度字体(因为编码与字一一对应)
1.构建编码列表
2.构建字列表
3.编码与字 --> 对应一一替换
'''
# 使该文件可以打开-->保存为.xml文件
font = TTFont("wKgHFVsUz1eAH_VRAABj9PS-ubk57..ttf")
font.saveXML("fonts.xml")

# 获取所有字体对应的name的列表
uniList = font.getGlyphOrder()
print(uniList)

"""
uniEDFF-->'\uedff'  字符串处理成对应unicode编码
1.除第一个以外每一个都需处理-->for循环取出除第一个以外的元素
2.uniEDFF-->'\uedff'
3.添加到新的列表中
"""
uni_list = []
for i in uniList[1:]:
    # i = r"'\u"+i[3:]+"'"   # 仅仅是做了拼接  怎么将字符串里边的东西保留原有的类型？eval()

    i = eval(r"'\u"+i[3:]+"'")  # eval函数将去掉字符串的两个引号，保留原意
    # print(i)
    uni_list.append(i)

print(uni_list)
# uni_list = [eval(r"'\u"+i[3:]+"'") for i in uniList[1:]]


# 对应字体列表，前端以坐标形式呈现
word_list = ['很', '五', '多', '远', '大', '十', '更', '了', '的', '矮', '不', '少', '九', '三', '八', '一', '右', '坏', '近', '着', '呢', '左', '是', '长', '六', '上', '短', '七', '高', '二', '得', '好', '下', '和', '四', '地', '小', '低']

'''
怎么替换字符串当中的 编码 对应 的 字
1.len(uni_list)
'''
for i in range(len(uni_list)):
    # 对应位置的编码 替换为 对应位置的字 比如：\ued8c 替换成 很
    content_str = content_str.replace(uni_list[i],word_list[i]) # 字符串不可变的特性

print(content_str)


