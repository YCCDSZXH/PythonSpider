# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 14:06
# @Author  : Amy
# @File    : 爬取斗鱼网.py

import requests
import os

# https://www.douyu.com/gapi/rknc/directory/yzRec/1
# https://www.douyu.com/gapi/rknc/directory/yzRec/2

# 获取数据
def get_html(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    # print(response.json())
    html = response.json()
    return html

# 解析数据
def parse_html(html):
    rl_list = html['data']['rl']
    # print(rl_list)
    img_info_list = []
    for rl in rl_list:
        img_info = {}
        img_info['img_url'] = rl['rs1']
        img_info['title'] = rl['nn']
        # print(img_url)
        # exit()
        img_info_list.append(img_info)
    # print(img_info_list)
    return img_info_list

# 保存数据
def save_to_images(img_info_list):
    dir_path = 'directory'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for img_info in img_info_list:
        img_path = os.path.join(dir_path, img_info['title']+'.jpg')
        res = requests.get(img_info['img_url'])
        res_img = res.content
        with open(img_path, 'wb') as f:
            f.write(res_img)
        # exit()


if __name__ == '__main__':
    url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/1'
    html = get_html(url)
    img_info_list = parse_html(html)
    save_to_images(img_info_list)
