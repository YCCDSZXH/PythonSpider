

from lxml import etree

import requests

tieba_name = input('请输入你要爬取的贴吧:')

startPage = int(input('开始页:'))
endPage = int(input('结束页:'))

url = 'https://tieba.baidu.com/f?'

for page in range(startPage,endPage+1):
    yema = (page-1)*50
    response = requests.get(url,params={'kw':tieba_name,'pn':yema})
    html = response.text
    content = etree.HTML(html)

    link_list = content.xpath('//a[@class="j_th_tit "]/@href')

    for link in link_list:
        fulllink = 'https://tieba.baidu.com'+link
        tiezi_resp = requests.get(fulllink)

        tiezi_html = tiezi_resp.text
        img_link = etree.HTML(tiezi_html)

        img_list = img_link.xpath('//img[@class="BDE_Image"]/@src')
        for my_img in img_list:
            img_response = requests.get(my_img)

            img = img_response.content
            img_name = my_img[-10:]
            f = open('img/'+img_name,'wb')
            f.write(img)
            f.close()
