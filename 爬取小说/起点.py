import requests
# 解析库,例如 lxml , 使用的是 XPath 语法
from lxml import etree      # pip install lxml

# 获取小说章节连接以及标题
# 获取章节内容
# 下载小说

'''
由于起点中文网打击盗版，用了js进行渲染，所以进入小说浏览页面无法点击右键，但我们也不是没有办法
比较通俗的破解方法是进入浏览器的设置---安全设置--关闭js脚本
也可以查看你的浏览器快捷键设置，里面有按键打开页面源代码的组合键，我这里是
'''

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}

def getbookurls():
    url = 'https://book.qidian.com/info/1010734471#Catalog'
    charpters = requests.get(url, headers=headers).text
    #  这个就是转换为xml的python的语法 HTML括号内填入目标站点的源码
    objects = etree.HTML(charpters)

    # 标签对象 是列表
    objs=objects.xpath("//ul[@class='cf']/li")

    tinybox=[]
    for obj in objs:
        try:
            # 获取文本
            chapt_names=obj.xpath('a/text()')[0]
            # @ 获取属性
            chapt_urls=obj.xpath('a/@href')[0]
            info={
                    'chapt_names':chapt_names,
                    'chapt_urls':'https:'+chapt_urls
                }
            tinybox.append(info)
            # print(charpnames,charpurls)
        except:
            pass

    return tinybox

def getcontent(url):
    res = requests.get(url, headers=headers).text
    objects = etree.HTML(res)
    objs=objects.xpath("//div[@class='read-content j_readContent']/p/text()")

    content=[]
    for obj in objs:
        # \u3000 是全角的空白符
        obj=obj.replace('\u3000\u3000','')
        # print(obj,end='')
        content.append(obj)
    return content


tinybox = getbookurls()



for i in tinybox:
    chapt_names = i['chapt_names']
    chapt_urls = i['chapt_urls']
    # 列表
    content = getcontent(i['chapt_urls'])
    text = ''
    for j in content:
        text = text + j
    print('正在下载 %s'%chapt_names)

    with open('起点爬虫\%s.doc'%chapt_names,'w') as f:
        f.write(text)


