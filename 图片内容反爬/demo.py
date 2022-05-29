import requests
from bs4 import BeautifulSoup
import re
from baidu import get_content
import time

html = requests.get('http://58921.com/alltime/2019')
html.encoding = 'utf-8'
html = html.text

soup = BeautifulSoup(html,'lxml')

req = r'<td><a href="/film/.*?" title="(.*?)">.*?</a></td>'

title = re.findall(req,html)
# print(len(title))
img_url = soup.find_all('img')[1:]
# print(len(img_url))
i = 0
for url in img_url:
    # print(url.get('src'))
    urls = url.get('src')
    img_content = requests.get(urls).content
    # print(img_content)
    with open('result/{}.png'.format(title[i]),'wb') as f:
        f.write(img_content)
    i+=1

    pf = get_content('result/{}.png'.format(title[i]))
    time.sleep(1)
    print(pf)

可迭代->迭代器->生成器->yield from->协程->协程和线程之间的对比
	
我们是怎么聊到索引的呢，是因为我提到我们的业务量比较大，每天大概有几百万的新数据生成，于是有了以下对话：
面试官：你们每天这么大的数据量，都是保存在关系型数据库中吗？

我：是的，我们线上使用的是MySQL数据库

面试官：每天几百万数据，一个月就是几千万了，那你们有没有对于查询做一些优化呢？

我：我们在数据库中创建了一些索引（我现在非常后悔我当时说了这句话）。
面试官：那你能说说什么是索引吗？
我：（这道题肯定难不住我啊）索引其实是一种数据结构，能够帮助我们快速的检索数据库中的数据。

面试官：那么索引具体采用的哪种数据结构呢？
我：（这道题我也背过）常见的MySQL主要有两种结构：Hash索引和B+ Tree索引，我们使用的是InnoDB引擎，默认的是B+树。

面试官：既然你提到InnoDB使用的B+ Tree的索引模型，那么你知道为什么采用B+ 树吗？这和Hash索引比较起来有什么优缺点吗？






