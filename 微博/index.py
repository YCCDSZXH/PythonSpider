import requests
# 配置文件作为一种可读性很好的格式，非常适用于存储程序中的配置数据
from configparser import ConfigParser

def loginwb():
    target = ConfigParser()
    target.read('password.ini',encoding='utf-8')
    pwd = target.get('weibo','password')

    data = {
        'client_id':'',
        'code':'',
        'ec':'0',
        'entry':'mweibo',
        'hff':'',
        'hfp':'',
        'loginfrom':'',
        'mainpageflag':1,
        'pagerefer':'https://m.weibo.cn/',
        'password':pwd,
        'qq':'',
        'r':'https://m.weibo.cn/',
        'savestate':1,
        'username':18646175116,
        'wentry':''
    }
    url = 'https://passport.weibo.cn/sso/login'
    header = {
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Connection': 'close',
        'Referer': 'https://passport.weibo.cn/signin/login',
        'Host': 'passport.weibo.cn'
    }

    # result = requests.post(url,MNIST_data=MNIST_data,headers=header)
    session = requests.Session()
    session.post(url, data=data,headers=header)
    # print(result)

    html = session.get('https://m.weibo.cn/profile/3308185293').text
    print(html)
    # # html.encoding = 'gb2312'
    # print(html.text)

if __name__ == '__main__':
    loginwb()