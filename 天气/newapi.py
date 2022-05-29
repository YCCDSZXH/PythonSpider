from tkinter import *
import requests
import urllib.request

def weather():
    host = 'http://jisutqybmf.market.alicloudapi.com/weather/query'
    method = 'GET'
    appcode = '8c42c716b4484ee3a01e2d3fdcf1c7bf'
    # 获取城市名字
    city = entry.get()
    # 编码
    city = urllib.request.quote(city)
    # 解码  百度举例
    # urllib.request.unquote("")
    # con = urllib.request.unquote("%E5%B1%85%E7%84%B6")
    # +'&citycode=citycode&cityid=cityid&ip=ip&location=location'
    querys = 'city=' + city
    # 拼接完整URL
    url = host + '?' + querys

    header = {'Authorization': 'APPCODE ' + appcode}
    request = requests.get(url, headers=header).json()

    info = request['result']
    # 清空之前的结果
    text.delete(0,END)
    text.insert(0, "星期:%s"%info['week'])
    text.insert(1, "天气:%s"%info['weather'])
    text.insert(2, "温度:%s"%info['temp'])
    text.insert(3, "风向:%s"%info['winddirect'])



root = Tk()
root.title('天气查询')

# 获取屏幕 宽、高
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 600
h = 300
# 计算 x, y 位置
x = str(int((ws/2) - (w/2)))
y = str(int((hs/2) - (h/2)))
# 窗口大小
root.geometry('500x400')
root.geometry('+500+300')
# 标签控件
lable = Label(root, text='输入要查询的城市名字：')
# grid 网格式布局   pack 包  place 位置
lable.grid(row=0, column=0)

# 输入控件
entry = Entry(root,font=("微软雅黑",22))
entry.grid(row=0, column=1)
# 列表框控件
text = Listbox(root,font = ('微软雅黑',15),width = 40,height = 10)
# columnspan  组件所跨越的列数
text.grid(row = 1,columnspan = 2)

# 按钮标签
button = Button(root, text='查询', width=10,command = weather)
button.grid(row=2, column=0, sticky=W)
button1 = Button(root, text='退出', width=10, command=root.quit)
button1.grid(row=2, column=1, sticky=E)
root.mainloop()









