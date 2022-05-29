# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 13:58
# @Author  : Amy
# @File    : QQ音乐.py


import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/76.0.3809.100 Safari/537.36"}


def getSongMid():
    searchword = input("请输入想要搜索的歌曲:")
    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=1&w=%s" % searchword
    res = requests.get(url=url, headers=headers)
    # 注意 此处通过postman返回并不是json的
    html = res.text
    print(type(html))
    # print(html)
    # 想要获取songmid-->1.正则匹配 2.截取->转为字典
    html = html[9:-1]
    songdata = json.loads(html)
    # 获取songmid
    song_li = songdata["data"]["song"]["list"]
    # 注意list下为列表格式
    song_info_li = []
    for song_info in song_li:
        songmid = song_info["songmid"]
        songname = song_info["songname"]
        song_info_li.append((songmid, songname))
    return song_info_li


def getPurl(song_info_list):
    for song_info in song_info_list:
        songmid = song_info[0]
        songname = song_info[1]

        p_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data = {"req": {"param": {"guid": "8182077584"}},"req_0": {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey","param": {"guid": "8182077584", "songmid": ["%s"], "uin": "7945"}},"comm": {"uin": 7945}}' % songmid
        res = requests.get(url=p_url, headers=headers)
        jsonData = res.json()
        # print(jsonData)
        purl = jsonData["req_0"]["data"]["midurlinfo"][0]["purl"]
        # print(purl)
        song_url = 'http://isure.stream.qqmusic.qq.com/' + purl
        songContent = requests.get(url=song_url, headers=headers).content
        path = songname + '.mp3'
        with open(path, 'wb') as f:
            f.write(songContent)
            print("下载完毕")


song_info_list = getSongMid()
getPurl(song_info_list)
