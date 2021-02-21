from flask import Flask,render_template,request
import datetime
app = Flask(__name__)

#路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():
#     return '傻逼!'
#通过访问路径，获取用户的字符串、整型、浮点型参数
@app.route("/user/<name>")
def hello(name):
    return "%s是sb"%name

@app.route("/user/<int:id>")
def hello2(id):
    return "%d号的会员"%id


#返回给用户渲染后的网页文件
# @app.route("/")
# def index2():
#     return render_template("index.html")#jinjia渲染

#向页面传递变量
@app.route("/")
def index2():
    time=datetime.date.today()  #普通变量
    name =["小张","小王","小赵"]#列表类型
    task={"任务":"打扫卫生","时间":"3小时"}
    return render_template("index.html",var=time,list=name,task=task)#jinjia渲染

#表单提交
@app.route('/test/register')
def register():
    return render_template("test/register.html")
#接收表单提交的路由，需要制定的method为post
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template("test/result.html",result=result)


if __name__ == '__main__':
    app.run()
