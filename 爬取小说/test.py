import urllib.request
import re

# 1.获取主页源代码
# 2.获取章节超链接
# 3.获取章节超链接源码
# 4.获取内容
# 5.下载，对文件操作

def getNovertContent():
    # 1 获取主页源码    HTTPResposne 类型的对象  read()
    html = urllib.request.urlopen("http://www.quanshuwang.com/book/0/269").read()
    # html.status  状态码
    # print(html)
    html = html.decode("gbk")
    # print(html)
    # 获取超链接
    # <a href="http://www.quanshuwang.com/book/138/138634/37031074.html" title="第一章 初级制药师，共3619字">第一章 初级制药师</a>
    #  r   表示原生字符串  正则表达式里使用"\"作为转义字符     匹配一个数字的"\\d"可以写成r"\d"
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    # 编译正则表达式字符串为对象，目的是增加效率
    reg = re.compile(reg)
    urls = re.findall(reg,html)
    # print(urls)
    # 2 获取章节超链接
    for url in urls:
        # print(url[0])
        # 可以写在read().decode
        # novel_url = url[0]
        # novel_title = url[1]
        novel_url,novel_title = url

        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode("gbk")
        reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        # S 多行匹配
        reg = re.compile(reg,re.S)
        # 3 获取章节超链接源码
        chapt_content = re.findall(reg,chapt_html)
        # print(chapt_content[0])   是文章内容
        # 4 获取内容
        # replace  要替换的    被替换的   替换后只有br
        chapt_content = chapt_content[0].replace('&nbsp;&nbsp;&nbsp;&nbsp;',"")
        chapt_content = chapt_content.replace("<br />","")
        # print(chapt_content)
        # print(len(chapt_content))
        # %s  format  字符串格式化  format不用指定数据类型
        print("正在保存 %s"%novel_title)
        # w 读写模式  wb 二进制形式读写
        f = open('{}.txt'.format(novel_title), 'w')
        f.write(chapt_content)
        f.close() 

        # with open(novel_title+'.txt','w') as f:
        #     f.write(chapt_content)


getNovertContent()