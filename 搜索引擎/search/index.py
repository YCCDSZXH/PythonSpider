from flask import Flask
from flask import render_template
from spider import getBdMsg
from flask import request
# Flask(__name__).run()
app = Flask(__name__)

# 装饰器   给该函数增加新功能
@app.route('/')  #定义路由
def index():
    # 调试错误信息
    # return  'hello world' + 123
    # return '<h1>python</h1>'
    # return  三个引号放html代码
    # return open('index.html',encoding='utf-8').read()
    return render_template('index.html',name = '搜索引擎')

@app.route('/juran')
def demo():
    return "hello juran"

@app.route('/s')
def s():
    # print(request.args.get('search'))
    keyword = request.args.get('wd')
    page = request.args.get('pn')
    text = getBdMsg(keyword,page)
    return text

if __name__ == '__main__':
    # 开启debug模式 会自动重启
    # 端口号 还可以修改  port = 8000
    # Debugger PIN: 101-699-405 调试用的
    app.run(debug=True,port=8000)

	

