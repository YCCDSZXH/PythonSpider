

import requests
import json

# 1.拿到统一的url
url = 'https://www.ximalaya.com/revision/play/v1/show?id=231012348&sort=1&size=30&ptype=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

r = requests.get(url,headers=headers)

ret = r.text

# 2.拿到音乐的id
# print(type(ret))
result = json.loads(ret)

# print(result,type(result))

content_list = result['data']['tracksAudioPlay']

for content in content_list:

    t_id = content['trackId'] # 音频的id
    name = content['trackName'] # 音频的name

    # print(t_id,type(t_id))

    url = 'https://www.ximalaya.com/revision/play/v1/audio?id=%d&ptype=1'%t_id
    # print(url)
    # 请求音频的链接地址
    mus_response = requests.get(url,headers=headers)
    # 拿到音频的网页数据
    mus_html = mus_response.text
    # 把数据转换成字典
    mus_result = json.loads(mus_html)

    # print(mus_html,type(mus_result))
    # 3 拿到音频的url
    mus_src = mus_result['data']['src']
    # print(mus_src)
    # 4.保存所有的音频
    with open('img/%s.m4a'% name,'wb') as f:
        mus = requests.get(mus_src)

        f.write(mus.content)

