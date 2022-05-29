# @ Time    : 2019/3/2 13:42
# @ Author  : JuRan
import requests
import urllib
import re

def get_content_list(keyword):
    keyword = urllib.parse.quote(keyword)
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword={}&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis'.format(keyword)
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'referer':'https://www.toutiao.com/search/?keyword=%s'%keyword
    }
    try:
        response = requests.get(url,headers=header)
        # print(response['MNIST_data'])
        if response.status_code == 200:
            result = response.json()
            for item in result['MNIST_data']:
                # print(item['article_url'])
                return item['article_url']
    except Exception as e:
        return None



def get_commont(commont_url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

    html = requests.get(commont_url,headers=header).text
    # print(html)
    regex = r"shareUrl: 'https://m.toutiao.com/group/(.*?)/'"
    regex = re.compile(regex,re.S)
    data = re.findall(regex,html)
    group_id,item_id = data[0],data[0]

    url = 'https://www.toutiao.com/api/comment/list/?group_id={}&item_id={}&offset=0&count=25'.format(group_id,item_id)
    commont = requests.get(url,headers=header).json()
    # print(commont['MNIST_data'])
    for item in commont['MNIST_data']['comments']:
        # print(item)
        # return item['text']
        with open('./demo.txt','a',encoding='utf-8') as f:
            f.write(item['text']+'\n')

commont_url = get_content_list('华为5G')
get_commont(commont_url)
