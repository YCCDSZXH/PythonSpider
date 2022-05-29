import urllib.request
import sys
import json
host = 'http://jisutqybmf.market.alicloudapi.com'
path = '/weather/query'
method = 'GET'
appcode = '8c42c716b4484ee3a01e2d3fdcf1c7bf'

city = input("请输入要查询的城市：")
# 编码
city = urllib.request.quote(city)
# 解码  百度举例
# urllib.request.unquote("")
# con = urllib.request.unquote("%E5%B1%85%E7%84%B6")

# querys = 'city=%E5%AE%89%E9%A1%BA&citycode=citycode&cityid=cityid&ip=ip&location=location'
querys = 'city='+city
# bodys = {}
url = host + path + '?' + querys

# 生成Request对象
request = urllib.request.Request(url)
# 如果不加头部信息
# response = urllib.request.urlopen('http://python.org/')
# 添加头部信息  模拟浏览器请求
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib.request.urlopen(request)
# bytes类型
content = response.read()
# decode解码    python3对文本以及二进制数据做了比较清晰的区分
# 解码就是将字节码转换为字符串，将比特位显示成字符。
info = content.decode('utf-8')

# 解码之后是一个字符串  还需要转成json形式
info = json.loads(info)

print(info['result']['week'])
print(info['result']['weather'])
print(info['result']['temp'])
print(info['result']['winddirect'])

# if (content):
#     print(content.decode())


