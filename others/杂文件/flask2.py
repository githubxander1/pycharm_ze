from flask import Flask, request, jsonify, session,make_response

# from flask_session import Session
app = Flask(__name__)
app.secret_key = 'a1234567'  # 设置密钥
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

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
    
@app.route('/getuser', methods=['GET'])
def getuser():
    # name = session.get('name')
    name= request.cookies.get('cookie_name')
    if name is not None:
        id = request.args.get('id')
        if id is None:
            return jsonify({'code': 1000, 'msg': 'must be required'})
        elif not id.isdigit():
            return jsonify({'code': 1001, 'msg': 'must be a number'})
        else:
            # 用户已登录，执行其他操作
            return jsonify({'code': 200, 'msg': 'user is logged in'})
    else:
        return jsonify({'code': 1002, 'msg': 'please login first'})


@app.route('/user/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if not username or not password:
        return jsonify({'code': 1001, 'msg': 'parameter error'})
    if username == 'admin' and password == '123456':
        mr=make_response({'code':200,'msg':"login success"})
        mr.set_cookie(key='cookie_name',value=username,max_age=5)
        return mr
        # session['name'] = username  # 添加session
        # return jsonify({'code': 1000, 'msg': 'login success'})
    else:
        return jsonify({'code': 1002, 'msg': 'account or password error'})


@app.route('/user/logout', methods=['GET'])
def logout():
    # name = session.get('name')
    name = request.cookies.get('cookie_name')
    if name is not None:
        # session.pop('name')  # 删除指定session
        # return jsonify({'code': 200, 'msg': 'logout success'})
        mr=make_response({'code': 200, 'msg': 'logout success'})
        mr.delete_cookie('cookie_name')
        return mr
    else:
        return jsonify({'code': 1002, 'msg': 'not logged in'})


if __name__ == '__main__':
    app.run(debug=True)
