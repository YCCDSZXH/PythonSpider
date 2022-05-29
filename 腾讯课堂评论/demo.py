# @ Time    : 2019/6/25 16:19
# @ Author  : JuRan

import requests
import csv

'''
User-Agent注入 Less-18演示
Referer注入    Less-19演示
sqlmap   referer注入 python sqlmap.py -r target.txt --batch 
target.txt中的referer中加上*
'''
header = {
    'cookie': '',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'referer': 'https://ke.qq.com/course/371296?tuin=3252f483'
}
proxies = {
    'http':'123.132.232.254:61017',
}
with open('demo.csv','a+',newline='',encoding='utf-8') as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    csvwriter.writerow(["用户名", "评论"])
    # 'https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=371296&count=10&page=0&filter_rating=0&bkn=152062940&r=0.6925735290154831'
    for i in range(10):
        res = requests.get('https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=371296&count=10&page={}&filter_rating=0&bkn=152062940&r=0.6489506254400161'.format(i),headers=header,proxies=proxies)
        if res.status_code == 200:
            result = res.json()
            # print(result['result']['items'])
            for item in result['result']['items']:
                nick_name = item['nick_name']
                comment = item['first_comment']
                print("正在用户保存评论")
                csvwriter.writerow([nick_name, comment])





import jieba
import os
from scipy.misc import imread
from wordcloud import WordCloud

def drawWordCloud(title, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    # mask=imread('mask.png')  按照图片形状来生成词云
    wc = WordCloud(font_path='simkai.ttf', background_color='white', max_words=2000, width=1920,
                   height=1080, mask=imread('mask.png'))
    # 数据处理
    comments = []
    with open('demo.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()[1:]
        for item in data:
            i = item.split(',')
            if len(i) == 2:
                comment = i[1]
                comments.append(comment)

    comment_after_split = jieba.cut(str(comments))  # 非全模式分词，cut_all=false
    # print(list(comment_after_split))    # jieba.cut返回的结构是一个可迭代的generator
    words = ' '.join(comment_after_split)  # 以空格进行拼接

    # 根据文本生成词云
    wc.generate_from_text(words)

    filepath = savepath + '/' + title + '.png'

    # 保存图片
    wc.to_file(filepath)

# drawWordCloud('demo')


# 我不敢下苦功琢磨自己,怕终于知道自己并非珠玉;然而心中又存在一丝希冀,便又不肯甘心与瓦砾为伍


### 经典的参数错误

def add(a,b):
    a += b
    return a

a = 1
b = 2
c = add(a,b)
print(c)        # 3
print(a,b)      # 1,2

a = [1,2]
b = [3,4]
c = add(a,b)
print(c)        # [1,2,3,4]
print(a,b)      # [1,2,3,4][3,4]

a = (1,2)
b = (3,4)
c = add(a,b)
print(c)        # (1,2,3,4)
print(a,b)      # (1,2)(3,4)


Python的每个对象都分为可变和不可变，主要的核心类型中，数字、字符串、元组是不可变的，列表、字典是可变的。


对不可变类型的变量重新赋值，实际上是重新创建一个不可变类型的对象，并将原来的变量重新指向新创建的对象（如果没有其他变量引用原有对象的话（即引用计数为0），原有对象就会被回收）。

### 不可变类型

以int类型为例:实际上 i += 1 并不是真的在原有的int对象上+1，而是重新创建一个value为6的int对象，i引用自这个新的对象。

通过id函数查看变量i的内存地址进行验证（使用hex(id(i)) 可以查看16进制的内存地址）
```
>>> i = 5
>>> i += 1
>>> i
6
>>> id(i)
140243713967984
>>> i += 1
>>> i
7
>>> id(i)
140243713967960
```

可以看到执行 i += 1 时，内存地址都会变化，因为int 类型是不可变的。

再改改代码，但多个int类型的变量值相同时，看看它们内存地址是否相同。
```
>>> i = 5
>>> j = 5
>>> id(i)
140656970352216
>>> id(j)
140656970352216
>>> k = 5
>>> id(k)
140656970352216
>>> x = 6
>>> id(x)
140656970352192
>>> y = 6
>>> id(y)
140656970352192
>>> z = 6
>>> id(z)
140656970352192
```

### 可变类型
以list为例。list在append之后，还是指向同个内存地址，因为list是可变类型，可以在原处修改。
```
>>> a = [1, 2, 3]
>>> id(a)
4385327224
>>> a.append(4)
>>> id(a)
4385327224
```
改改代码，当存在多个值相同的不可变类型变量时，看看它们是不是跟可变类型一样指向同个内存地址
```
>>> a = [1, 2, 3]
>>> id(a)
4435060856
>>> b = [1, 2, 3]
>>> id(b)
4435102392
```

python2和python3 的range
为什么用list可以把range转成列表


#### 使用type创建类

一个函数有两个功能,不建议大家这样写,但是Python为了兼容不同的版本让type有了两个功能

type还可以动态的创建类,type(类名,由父类组成的元组,包含属性的字典)

```
User = type("User",(),{})
obj = User()
print(obj)

添加属性
User = type("User", (), {'name':'juran'})
obj = User()
print(obj.name) # 打印结果为juran

添加类中的方法
def info(self):
    # return "info"
    return self.name

User = type("User", (), {'name':'juran',"info":info})
obj = User()
print(obj.info())  # 打印结果为juran

类的继承
class BaseClass:
    def demo(self):
        return "base class"
        
User = type("User", (BaseClass,), {'name':'juran',"info":info})
obj = User()
print(obj.demo())  # 打印结果为base class


什么是元类,元类是创建类的类,就是type
```



修改全局变量一定需要加global嘛?
lis = [11,22]

def test():
    lis.append(33)


















