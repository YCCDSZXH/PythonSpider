import requests
import os
from urllib.parse import urlencode

# 设置条件
# 解析网页
# 下载图片
# 保存信息

# 解析网站
def get_one(page, startage, endage, gender, startheight, endheight, salary):
    # 设置请求头
    headers = {
        'Referer': 'http://www.lovewzly.com/jiaoyou.html',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 66.0.3359.170Safari / 537.36'
    }

    # 设置请求参数
    params = {
        # 页数
        'page':page,
        # 起始年龄
        'startage': startage,
        # 截止年龄
        'endage':endage,
        # 性别
        'gender':gender,
        # 所在城市的编号
        'cityid':'52',
        # 起始身高
        'startheight':startheight,
        # 终止身高
        'endheight':endheight,
        # 是否结婚
        'marry':'1',
        # 教育水平`
        'educatin':'40',
        # 工资薪水
        'salary':salary
    }
    # 网站链接
    # base_url = 'http://www.lovewzly.com/api/user/pc/list/search?'

    # http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=197&marry=1&salary=2&page=1
    # http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=197&marry=1&astro=1&lunar=1&education=10&salary=2&page=1
    base_url = 'http://www.lovewzly.com/api/user/pc/list/search?'+'page={}&startage={}&endage={}&gender={}&cityid=52&startheight={}&endheight={}&marry=1&educatin=40&salary={}'.format(page,startage,endage,gender,startheight,endheight,salary)
    # 拼接请求参数
    # url = base_url + urlencode(params)
    # print(base_url)
    # exit()

    # 调试信息
    # print(url)
    while True:
        try:
            # 利用 requests 库请求目标地址
            response = requests.get(base_url, headers=headers)
            # 判断请求的结果是否有效
            if response.status_code == 200:
                # 返回 json 数据
                return response.json()
        except ConnectionError:
            return None


# 设置年龄
def query_age():
    # 终端输入年龄
    age = input('请输入期望对方年龄(如:20)：')
    # 年龄区间进行判断
    if 21 <= int(age) <= 30:
        startage = 21
        endage = 30
    elif 31 <= int(age) <= 40:
        startage = 31
        endage = 40
    elif 41 <= int(age) <= 50:
        startage = 41
        endage = 50
    else:
        startage = 0
        endage = 0
    # 返回起始年龄和终止年龄
    return startage, endage


# 设置性别参数
def query_sex():
    '''性别筛选'''
    # 终端性别字符串的输入
    sex = input('请输入期望对方性别(如:女):')
    # 对输入的信息进行判断
    if sex == '男':
       gender = 1
    else:
       gender = 2

    # 返回性别对应的数字
    return gender

# 设置身高参数
def query_height():
    '''身高筛选'''
    # 终端输入身高信息
    height = input('请输入期望对方身高(如:162):')
    # 身高区域进行判断
    if 151 <= int(height) <= 160:
        startheight = 151
        endheight = 160
    elif 161 <= int(height) <= 170:
        startheight = 161
        endheight = 170
    elif 171 <= int(height) <= 180:
        startheight = 171
        endheight = 180
    elif 181 <= int(height) <= 190:
        startheight = 181
        endheight = 190
    else:
        startheight = 0
        endheight = 0

    # 返回对应的起始身高和终止身高
    return startheight, endheight


# 设置薪水参数
def query_money():
    '''待遇筛选'''
    # 终端输入薪水区间
    money = input('请输入期望的对方月薪(如:8000):')

    # 薪水区间进行判断
    if 2000 <= int(money) < 5000:
        salary = 2
    elif 5000 <= int(money) < 10000:
        salary = 3
    elif 10000 <= int(money) <= 20000:
        salary = 4
    elif 20000 <= int(money):
        salary = 5
    else:
        salary = 0
    # 返回薪水参数
    return salary


# 查询符合条件的数据
def query_data():
    print('请输入你的筛选条件, 开始本次姻缘')
    # 获取终端输入的性别
    gender = query_sex()
    # 获取终端输入的起始身高和终止身高
    startheight, endheight = query_height()
    # 获取终端输入的开始年龄和终止年龄
    startage, endage = query_age()
    # 获取终端输入的薪水
    salary = query_money()
    # 循环遍历 10 次，即抓取 10 次页面的数据
    for i in range(1, 10):
        # 获取抓取到的 json 数据
        json = get_one(i, startage, endage, gender, startheight, endheight, salary)

        # print(json['MNIST_data']['list'])
        # exit()
        # 循环遍历每个 json 数据
        for item in json['data']['list']:
            # save_to_monogo(item)
            # 保存图片
            save_image(item)
            save_to_txt(item)

# 图片保存
def save_image(item):
    # 判断当前目录是否存在 images 文件夹
    if not os.path.exists('images'):
        # 创建 images 文件夹
        os.mkdir('images')
    try:
        # 获得 image 信息
        # image_url = item.get('avatar')
        image_url = item['avatar']
        # print(image_url)
        # 利用 requests 请求图片地址
        response = requests.get(image_url)
        # 判断请求的地址是否有效
        if response.status_code == 200:
            # 设置图片保存地址
            # md5(response.content).hexdigest()
            file_path = 'images/{}.jpg'.format(item['userid'])
            # 判断文件是否已经存在
            if not os.path.exists(file_path):
                print("正在获取:%s的信息"%item['username'])
                # 打开对应的文件
                with open(file_path, 'wb')as f:
                    # 保存图片信息
                    f.write(response.content)
            else:
                # 输出图片保存成功信息
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        # 输出图片保存失败信息
        print('Failed to save image')


# 保存到文本中
def save_to_txt(item):
    with open('grilinfo/'+item['username']+'.txt','w',encoding='utf-8') as f:
        f.write('名字:'+item['username']+',城市:'+item['city'])


if __name__ == '__main__':
    query_data()


