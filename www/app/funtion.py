from functools import wraps
from flask import session,redirect,url_for,make_response,Response
from app.mysql import mydb
my = mydb()

# 登录限制
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user'):
            user = session.get('user')
            if not my.get_openid(user[0]):
                session.clear()
                return redirect(url_for("login"))
            return func(*args,**kwargs)
        else:
            return redirect(url_for("login"))
    return wrapper




# 接受post数据
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp