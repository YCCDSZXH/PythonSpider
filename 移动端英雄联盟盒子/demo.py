# @ Time    : 2020/4/16 16:57
# @ Author  : JuRan
import requests
import time
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    "Cookie": "l_uin=o844297347; p_uin=o844297347; p_skey=vQHmViM9*SlEk*At*oCijqXgyeEIZygn6YdxyXiOPQM_; uin=o844297347; skey=M4TVuexvyk;",
    "Host": "qt.qq.com",
}

# 这是版本列表页面的URL
url = "https://qt.qq.com/php_cgi/news/php/varcache_getnews.php?id=367&page=1&plat=android&version=9942"


r = requests.get(url, headers=header).json()

for item in r['list']:
    # print(item)
    title = item['title']
    article_url = item["article_url"]
    intent = item["intent"]
    # print(intent)
    # print(article_url)
    if intent:
        ver = re.findall(r"version_key=(\d+)", intent)
        # https://qt.qq.com/php_cgi/lol_mobile/newver/php/varcache_tablist.php?ver=20200416&plat=android&version=9942
        taburl = "https://qt.qq.com/php_cgi/lol_mobile/newver/php/varcache_tablist.php?ver={}&plat=android&version=9942".format(ver[0])
        time.sleep(1)
        res = requests.get(taburl).json()
        for tab in res['data']:
            # print(tab)
            # tab_id = tab['tab_id']
            tab_url = tab['tab_url']
            r2 = requests.get(tab_url).json()
            print(r2)
            time.sleep(1)
    else:
        article_url = item["article_url"]
        r3 = requests.get(article_url, headers=header)
        r3.encoding = "utf-8"
        print("正在获取英雄联盟动态：%s" % title)

        with open("./info/%s.html" % title, "w", encoding="utf-8") as f:
            f.write(r3.text)



# http://qt.qq.com/php_cgi/lol_mobile/newver/php/newveritemlist.php?ver=20200416&tabid=456&tabtype=hero&areaid=16&next_cursor=&plat=android&version=9942

# http://qt.qq.com/php_cgi/lol_mobile/newver/php/newveritemlist.php?ver=20191226&tabid=420&tabtype=hero&areaid=16&next_cursor=&plat=android&version=9942

# http://qt.qq.com/php_cgi/news/php/varcache_article.php?id=60627&version=9942&areaid=16&APP_BROWSER_VERSION_CODE=1&android_version=1&imgmode=auto