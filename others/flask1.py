
from flask import Flask, jsonify, request, make_response,session

app = Flask(__name__)
# 设置静态路由
app.secret_key = 'a1234567'#设置密钥

@app.route('/index',methods=['GET'])
def index():
    return jsonify('hello,world')
userinfo={'1001':['张三','123'],
          '1002':['张三','1235'],
          '1003':['张三','1234']}
# 动态路由
@app.route('/students/<string:stno>',methods=['GET'])
def getstrinfo(stno):
    if stno in userinfo:
        return jsonify({stno:userinfo.get(stno)})
    else:
        return jsonify(f'{stno}不存在')

# request请求
@app.route('/getuser',methods=['GET'])
def get_user():
    # name=request.cookies.get('name')#获取指定cookie
    name=session.get('name')
    if name:
        id=request.args.get('id')
        if id is None:
            return jsonify({'code':1000,'id':id,'msg':'must be required'})
        elif not id.isdigit():
            return jsonify({'code':1001,'id':id,'msg':'must be a number'})
    else:
        return jsonify({'code':1002,'msg':'please login first'})

@app.route('/user/login',methods=['get'])
def login():
    username= request.values.get('username')
    passwd=request.values.get('password')
    if not username or not passwd:#检查参数是否都正常传入
        return jsonify({'code':'1001','msg':'parameter error'})
    if username=='admin' and passwd=='123456':
        mr=make_response(jsonify({'code':1000,'msg':'login success'}))#创建make-response对象
        # mr.set_cookie(key='name',value=username,max_age=60)#设置cookie
        session['name'] = username #添加session
        return mr
    else:
        return jsonify({'code':1002,'msg':'account or password error'})

@app.route('/user/loginout', methods=['get'])
def loginout():
    # name = request.cookies.get('name')  # 获取指定cookie
    name=session.get('name')
    if name is not None:
        return jsonify({'code':1000,'msg':'not login'})
    else:
        mr=make_response({'code':200,'msg':'loginout success'})
        session.pop('name')#删除指定cookie
        return mr




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5566,debug=True)
    # app.run(url='0.0.0.0:5566/index',debug=True)