#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
req = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

def login():
    # 获取图片
    pic_response = req.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand')
    codeImage = pic_response.content
    fn = open('code2.png', 'wb')
    fn.write(codeImage)
    fn.close()

    codeStr = input('请输入验证码坐标:')
    data = {
        'answer': codeStr,
        'rand': 'sjrand',
        'login_site': 'E'
    }

    response = req.post('https://kyfw.12306.cn/passport/captcha/captcha-check',data=data,headers=headers)

    print(response.text)

login()