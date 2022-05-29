import requests
import re
import json

# 获取JS源代码      获取英雄ID
# 拼接URL地址
# 获取下载图片名称
# 下载图片


# http://lol.qq.com/web201310/info-heros.shtml
def getLOLImages():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    url_js = r'https://lol.qq.com/biz/hero/champion.js'
    # 获取到的是bytes类型  需要转码    忽略对SSL证书的验证 verify=False
    # res_js = requests.get(url_js,headers = header).content
    html_js = requests.get(url_js,headers = header).text
    # html_js = res_js.decode("gbk")
    # 正则表达式
    req = r'"keys":(.*?),"data"'
    req = re.compile(req)
    # 获取到的数据类型是str
    list_js = re.findall(req,html_js)

    # 转成dict
    dict_js = json.loads(list_js[0])


    # 定义图片列表
    pic_list = []
    for key in dict_js:
        # 英雄ID
        # print(key)
        #  81001    266011
        # http://ossweb-img.qq.com/images/lol/web201310/skin/big266002.jpg
        # 循环20次 有的英雄没有那么多皮肤怎么办？
        for i in range(20):
            num = str(i)
            # 判断i的值大小
            if len(num) == 1:
                # 001 002
                hreo_num = "00" + num
            elif len(num) == 2:
                # 011 012
                hreo_num = "0" + num
            # 81000
            numStr = key + hreo_num
            print(numStr)
            # https://game.gtimg.cn/images/lol/act/img/skin/big1002.jpg
            # url = r'http://ossweb-img.qq.com/images/lol/web201310/skin/big' + numStr + '.jpg'
            url = r'https://game.gtimg.cn/images/lol/act/img/skin/big' + numStr + '.jpg'
            pic_list.append(url)

    # 获取图片下载名称
    list_filePath = []
    # 'D:\桌面\python-公开课\练习\LOLpic\\Zereal.jpg'
	# path = r'results\\'
    path = r'D:\Python上课代码\python-公开课\英雄联盟\LOLPic\\'
    for name in dict_js.values():
        # 英雄名称
        # print(name)
        for i in range(20):
            # Aatrox0.jpg
            file_path = path + name + str(i) + '.jpg'
            list_filePath.append(file_path)


    # 下载图片
    n = 0
    for picurl in pic_list:
        res = requests.get(picurl)
        n+=1
        if res.status_code == 200:
            print("正在下载%s" % list_filePath[n]) 
            # f = open(list_filePath[n],'wb')
            # f.write(res.content)
            # f.close()
            with open(list_filePath[n], "wb") as f:
                f.write(res.content)

    # for i in range(len(pic_list)):
    #     # 获取图片  verify=False
    #     res = requests.get(pic_list[i])
    #     if res.status_code == 200:
    #         print("正在下载%s" % list_filePath[i])
    #         with open(list_filePath[i], "wb") as f:
    #             f.write(res.content)

getLOLImages()











