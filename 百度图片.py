

# 通过观察数据我们发现能不能把瀑布流形式的数据变成传统页面形式的数据呢？index->flip

# 先去爬取一张图片
import requests
import re
# http://img.xiami.net/images/collect/587/87/8262587_1320898545.jpg objurl
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
# 1.拿到目标的url
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=88'
# 2.拿到网页的源码

r = requests.get(url,headers=headers)
ret = r.text
# print(ret)
# 3.拿到图片的url
result = re.findall('"objURL":"(.*?)"',ret)
# print(result)

# 4.保存图片
# a = 1
for i in result:
# url = 'http://img.xiami.net/images/collect/587/87/8262587_1320898545.jpg'

    # 获取图片的名字
    name = i[-10:]
    name = re.sub('/','',name)
    print(name)

    # 处理图片的格式
    end = re.search(r'(\.jpg|\.png|\.jpeg|\.gif)$',name)

    if end == None:

        name = name + '.jpg'


    with open('img/'+name,'wb') as f:
        # 网络问题
        try:
            r = requests.get(i)

        except Exception as e:
            print(e)

        f.write(r.content)

        # a += 1