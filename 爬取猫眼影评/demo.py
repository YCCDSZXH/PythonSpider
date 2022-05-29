# import requests
# import csv
#
# num = 0
# print('[INFO]: start page is %d...'%num)
# with open("demo.csv", "a+", newline="", encoding="utf-8") as datacsv:
#     # newline="" 如果不加这个参数，新的一行会隔一行写入。
#     # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
#     csvwriter = csv.writer(datacsv, dialect=("excel"))
#     # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
#     csvwriter.writerow(["用户名", "评论"])
#     while True:
#         url = 'http://m.maoyan.com/review/v2/comments.json?movieId=248172&userId=-1&offset={}&limit=15&ts=0&type=3'.format(
#             num)
#         num += 15
#         res = requests.get(url)
#         # print(result['MNIST_data']['comments'])
#         if res.status_code == 200:
#             result = res.json()
#             # print(result)
#             print('[page]:%d'%num)
#             for item in result['MNIST_data']['comments']:
#                 content = item['content']
#                 nickname = item['nick']
#                 csvwriter.writerow([nickname, content])

import os
import jieba
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
    with open('myl.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()[1:]
        for item in data:
            i = item.split(',')
            if len(i) == 2:
                comment = i[1]
                comments.append(comment)

    comment_after_split = jieba.cut(str(comments))  # 非全模式分词，cut_all=false
    # print(list(comment_after_split))    # jieba.cut返回的结构是一个可迭代的generator
    words = ' '.join(comment_after_split)  # 以空格进行拼接
    # print(words)
    # with open(words, 'r',encoding='utf-8') as f:
        # print(f.read())
    # 根据文本生成词云
    wc.generate_from_text(words)

    filepath = savepath + '/' + title + '.png'
    # ./results/demo/demo.png  不同的操作系统下面可能用到的文件分隔符不同
    # print(os.path.join(savepath, title, title + '.png'))
    # 保存图片
    wc.to_file(filepath)

drawWordCloud('demo')





