import itchat
import pygame

'''提示'''
def alarm():
	# pygame.mixer 用于加载和播放声音的pygame模块
	pygame.mixer.init()		# 初始化混音器模块
	pygame.mixer.music.load('alarm.mp3')	# 载入一个音乐文件用于播放
	pygame.mixer.music.play()				# 开始播放音乐流。
	# try:
	# 	import tkinter.messagebox
	# 	tkinter.messagebox.showinfo('抢红包啦!', '有人发红包了, 快去抢啊！')
	# except:
	# 	pass

'''监控是否有红包-群聊(Note参数: 通知消息类型)'''
@itchat.msg_register('Note', isGroupChat=True)
def getNoteGroup(msg):
	if u'收到红包' in msg['Text']:
		print('[INFO]: %s' % msg['Text'])
		alarm()

'''监控是否有红包-个人(Note参数: 通知消息类型)'''
@itchat.msg_register('Note', isGroupChat=False)
def getNote(msg):
	if u'收到红包' in msg['Text']:
		print('[INFO]: %s' % msg['Text'])
		alarm()
		
if __name__ == '__main__':
	itchat.auto_login(hotReload=True)
	itchat.run()
	itchat.logout()