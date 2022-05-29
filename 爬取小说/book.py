import requests
import re

def getNovertContent():
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81       Safari/537.36",
    # }
    # ,headers=headers
    response = requests.get("http://www.biqukan.com/46_46298/")
    response.encoding = "gbk"
    html = response.text
    reg = r'<dd><a href="(.*?)">(.*?)</a></dd>'
    # 提高效率
    reg = re.compile(reg)
    urls = re.findall(reg, html)
    startUrl = "http://www.biqukan.com"
    for url in urls:
        # print(url[0])
        # 可以写在read().decode
        novel_url = startUrl + url[0]

        novel_title = url[1]
        chapt = requests.get(novel_url)
        chapt.encoding = "gbk"
        chapt_html = chapt.text
        reg = r'<div id="content" class="showtxt">(.*?)</div>'
        reg = re.compile(reg, re.S)
        chapt_content = re.findall(reg, chapt_html)
        # print(chapt_content)
        chapt_content = chapt_content[0].replace('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', "")
        chapt_content = chapt_content.replace("<br />", "")
        # print(chapt_content)
        print("正在保存 %s" % novel_title)
        # w 读写模式  wb 二进制形式读写
        f = open('{}.doc'.format(novel_title), 'w')
        f.write(chapt_content)

getNovertContent()