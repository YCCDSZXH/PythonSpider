import itchat
import os
import time
#import cv2 #如果使用opencv的话可以远程拍照

sendMsg = u"[消息助手]:暂时无法回复" #自动回复内容
usageMsg = u"使用方法：\n1.运行CMD命令：cmd xxx (xxx为命令)\n-例如关机命令:\ncmd shutdown -s -t 0 \n2.获取一张图片：cap\n3.启用消息助手(默认关闭)：ast\n4.关闭消息助手：astc"

@itchat.msg_register('Text') #注册文本消息

def text_reply(msg): #心跳程序
    global flag
    message =  msg['Text'] #接收文本消息
    fromName =msg['FromUserName'] #发送方
    toName = msg['ToUserName'] #接收方

    if toName == "filehelper":
        if message == "cap": #远程拍照并发送到手机
            cap=cv2.VideoCapture(0)
            ret,img =cap.read()
            cv2.imwrite("weixinTemp.jpg",img)
            itchat.send('@img@%s'%u'weixinTemp.jpg','filehelper')
            cap.release()
        if message[0]+message[1]+message[2] == "cmd": #远程执行cmd命令
            os.system(message.strip(message[0]+message[1]+message[2]+message[3])) #远程执行cmd命令，可以实现关机
        if message == "ast":
            flag = 1
            itchat.send("消息助手已开启","filehelper")
        if message == "astc":
            flag = 0
            itchat.send("消息助手已关闭","filehelper")
    elif flag==1:
        itchat.send(sendMsg,fromName)
        myfile.write(message) #保存消息内容
        myfile.write("\n")
        myfile.flush()

flag = 0 #消息助手开关
nowTime = time.localtime()
filename =str(nowTime.tm_mday)+str(nowTime.tm_hour)+str(nowTime.tm_min)+str(nowTime.tm_sec)+".txt"
myfile = open(filename,'w')

if __name__ == '__main__':
    itchat.auto_login()
    itchat.send(usageMsg,"filehelper")
    itchat.run()