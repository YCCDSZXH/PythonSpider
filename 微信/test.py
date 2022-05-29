import itchat
import time
import requests
# hotReload=True
itchat.auto_login(hotReload=True)
listfriend = itchat.get_friends(update=True)
# print(listfriend[0:])
# exit()

apiUrl = 'http://www.tuling123.com/openapi/api'
# friendname = input("请输入要自动回复的微信好友:")

def get_response(message):
    data = {
        'key':'024848ea750a46f993eba7975330dd1d',
        'info':message,
        'userid':'robot'
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        print('robot reply:%s'% r["text"])
        return r['text']
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    defaultRreply = '我知道了'
    realFriend = itchat.search_friends(name='东东啊')
    realFriendUserName = realFriend[0]['UserName']
    print('message:%s'%msg['Text'])
    reply = get_response(msg['Text'])
    if msg['FromUserName'] == realFriendUserName:
        itchat.send(reply or defaultRreply,toUserName= realFriendUserName)

itchat.run()