import requests
def getBdMsg(keyword,page):
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81       Safari/537.36",
    }
    try:
        res = requests.get('https://www.baidu.com/s?wd={}&pn={}'.format(keyword,page),headers=headers)
        res.encoding = 'utf-8'
        res = res.text

        html = res.replace('//www.baidu.com/img/baidu_jgylogo3.gif','static/images/logic.jpg')
        html.replace('百度一下','搜索')
        return html
    except Exception as e:
        print('获取错误url = %s'%keyword)
if __name__ == '__main__':
    print(getBdMsg('python',0))

# html = getBdMsg()
# print(html.url)
# print(html.headers)
# print(html.content)