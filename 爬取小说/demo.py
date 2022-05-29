import requests
import re

# 1.获取主页源代码
# 2.获取章节超链接
# 3.获取章节超链接源码
# 4.获取内容
# 5.下载，对文件操作


def getNovertContent():
    # http://www.biqukan.com
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81       Safari/537.36",
    }
    '''
    response = requests.get("http://www.quanshuwang.com/book/0/269")
    response.encoding = "gbk"
    html = response.text
    # print(html)
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    # 提高效率
    reg = re.compile(reg)
    urls = re.findall(reg, html)

    for url in urls:
        # print(url[0])
        # 可以写在read().decode
        novel_url = url[0]
        novel_title = url[1]
        chapt = requests.get(novel_url)
        chapt.encoding = "gbk"
        chapt_html = chapt.text
        reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        reg = re.compile(reg, re.S)
        chapt_content = re.findall(reg, chapt_html)
        # print(chapt_content)
        chapt_content = chapt_content[0].replace('&nbsp;&nbsp;&nbsp;&nbsp;', "")
        chapt_content = chapt_content.replace("<br />", "")
        print("正在保存 %s" % novel_title)
        # w 读写模式  wb 二进制形式读写
        f = open('{}.txt'.format(novel_title), 'w')
        f.write(chapt_content)

getNovertContent()