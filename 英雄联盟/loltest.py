import requests
import re
import json


# http://lol.qq.com/web201310/info-heros.shtml
def path_js(url_js):
    # 获取到的是bytes类型  需要转码  , verify=False
    res_js = requests.get(url_js).content

    html_js = res_js.decode("gbk")
    # 正则表达式
    req = r'"keys":(.*?),"data"'
    req = re.compile(req)
    # 获取到的数据类型是str
    list_js = re.findall(req,html_js)
    # 转成dict
    dict_js = json.loads(list_js[0])

    return dict_js


def path_url(dict_js):
    pic_list = []
    for key in dict_js:
        for i in range(20):
            xuhao = str(i)
            if len(xuhao) == 1:
                num_houxu = "00" + xuhao
            elif len(xuhao) == 2:
                num_houxu = "0" + xuhao
            numStr = key + num_houxu
            url = r'http://ossweb-img.qq.com/images/lol/web201310/skin/big' + numStr + '.jpg'
            pic_list.append(url)
    # print(pic_list)
    return pic_list


def name_pic(dict_js, path):
    list_filePath = []
    for name in dict_js.values():
        for i in range(20):
            file_path = path + name + str(i) + '.jpg'
            list_filePath.append(file_path)
    return list_filePath


def writing(url_list, list_filePath):
    for i in range(len(url_list)):
        res = requests.get(url_list[i], verify=False)
        if res.status_code == 200:
            print("正在下载%s"%list_filePath[i])
            with open(list_filePath[i], "wb") as f:
                f.write(res.content)

if __name__ == '__main__':
    url_js = r'http://lol.qq.com/biz/hero/champion.js'
    path = r'D:\Python上课代码\python-公开课\英雄联盟\LOLPic\\'
    dict_js = path_js(url_js)
    url_list = path_url(dict_js)
    list_filePath = name_pic(dict_js, path)
    writing(url_list, list_filePath)