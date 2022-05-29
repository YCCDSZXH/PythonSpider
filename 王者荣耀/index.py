from urllib.request import urlretrieve
import requests
import os

# 英雄列表URL地址
heros_url = "http://gamehelper.gm825.com/wzry/hero/list"
# 武器URL地址
weapon_url = "http://gamehelper.gm825.com/wzry/equip/list"

# 下载王者荣耀英雄图片
def hero_imgs_download(url,header):
    # 获取文本.text 获取图片 .content
    req = requests.get(url = url,headers = header).json()
    # 字典格式
    # print((req))
    hero_num = len(req['list'])
    print("一共有%d个英雄"%hero_num)
    hero_images_path = 'hero_images'
    if not os.path.exists(hero_images_path):
        os.mkdir(hero_images_path)
    hero_list = req['list']
    for each_hero in hero_list:
        # print(each_hero)
        hero_photo_url = each_hero['cover']
        hero_name = each_hero['name'] + '.jpg'
        filename = hero_images_path + '/' + hero_name
        print("正在下载 %s的图片"%each_hero['name'])
        # if hero_images_path not in os.listdir():
        #     os.makedirs(hero_images_path)
        # 下载图片
        urlretrieve(url = hero_photo_url,filename = filename)

# hero_imgs_download(heros_url,headers)


# 打印所有英雄的名字和ID
def hero_list(url,header):
    print('*' * 100)
    print('\t\t\t\t欢迎使用《王者荣耀》出装小助手！')
    print('*' * 100)
    req = requests.get(url = url,headers = header).json()
    flag = 0
    hero_list = req['list']
    for each_hero in hero_list:
        hero_name = each_hero['name']
        hero_id = each_hero['hero_id']
        flag += 1
        # 为end传递一个\t，这样print函数不会在字符串末尾添加一个换行符，而是添加一个\t
        print("%s的ID为:%s"%(hero_name,hero_id),end = '\t\t')
        if flag == 3:
            # 先不加end  在加end 看效果
            print('\n',end='')
            flag = 0

# hero_list(heros_url, headers)
# hero_id = input("请输入要查询的英雄ID:")


# 获取武器信息
def hero_weapon(url,header):
    req = requests.get(url=url, headers=header).json()
    weapon_info_list = req['list']
    return weapon_info_list


# 根据equip_id查询武器名字和价格
# weapon_info - 存储所有武器的字典
def seek_weapon(equip_id,weapon_info):
    for each_weapon in weapon_info:
        if each_weapon['equip_id'] == str(equip_id):
            weapon_name = each_weapon['name']
            weapon_price = each_weapon['price']
            # 返回两个变量，可以用元组
            weapon = (weapon_name,weapon_price)
            return weapon

            # return weapon_name,weapon_price


# 获取英雄ID并打印出装信息
# weapon_info  所有武器的字典
def hero_info(url,header,weapon_info):
    req = requests.get(url=url, headers=header).json()
    print("\n历史上的%s:\n %s"%(req['info']['name'],req['info']['history_intro']))
    for each_equip_choice in req['info']['equip_choice']:
        # print(each_equip_choice)
        print('\n%s:%s'%(each_equip_choice['title'],each_equip_choice['description']))
        flag = 0
        total_price = 0
        for each_weapon in each_equip_choice['list']:
            flag += 1
            equip_id = each_weapon['equip_id']
            # 根据equip_id 查询出武器的名称以及价格
            weapon = seek_weapon(equip_id,weapon_info)
            # print(weapon)
            weapon_name = weapon[0]
            weapon_price = weapon[1]
            print('%s:%s' % (weapon_name, weapon_price), end='\t')
            if flag == 3:
                print('\n', end='')
                flag = 0
            total_price += int(weapon_price)
        print("神装套件共计:%d"%total_price)

# 程序入口
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Host': 'gamehelper.gm825.com'
    }

    # 武器URL地址
    weapon_url = "http://gamehelper.gm825.com/wzry/equip/list"
    # 英雄列表URL地址
    heros_url = "http://gamehelper.gm825.com/wzry/hero/list"

    hero_list(heros_url, headers)
    hero_id = input("请输入要查询的英雄ID:")

    # 英雄出装URL
    hero_url = "http://gamehelper.gm825.com/wzry/hero/detail?hero_id={}".format(hero_id)

    # 下载
    # hero_imgs_download(heros_url,headers)

    # 获取武器信息
    weapon_info_dict = hero_weapon(weapon_url, headers)
    # 获取英雄ID并打印出装信息
    hero_info(hero_url,headers,weapon_info_dict)