from app.admin import admin
from flask import render_template,redirect,url_for,request,jsonify,session,flash
from app.mysql import mydb
from functools import wraps
from app.forms import login_form


# 登录限制
def admin_login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('admin'):
            user = session.get('admin')
            if not my.get_admin_id(user[0]):
                session.clear()
                return redirect(url_for("admin.login"))
            return func(*args,**kwargs)
        else:
            return redirect(url_for("admin.login"))
    return wrapper




my = mydb()

@admin.route('/')
@admin_login_required
def index():
    data = my.ad_get_order(0)
    name = my.ad_get_name()
    print(data)
    print(name)
    return render_template('admin/index.html',data = data,name = name)

@admin.route('/login',methods=["POST","GET"])
def login():
    if not session.get('admin'):
        forms = login_form()
        if request.method == "POST":
            if forms.validate_on_submit():
                data = forms.data
                phone = data['phone']
                pwsd = data['pwsd']
                user = my.get_admin_name(phone, pwsd)
                if user:
                    session['admin'] = user
                    print(session.get('user'))
                    return redirect(url_for('admin.index'))
                else:
                    flash('账号或密码错误')
        return render_template('admin/login.html',form = forms)
    else:
        return redirect(url_for('admin.index'))


@admin.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin.index'))



@admin.route('/isok/<int:isot>')
def delorder(isot):
    print(isot)
    try:
        my.ad_updateorder(isot)
    except:
        print('审核错误')
    return redirect(url_for('admin.index'))

@admin.route('/deleteproduct/<int:product>')
def deleteproduct(product):
    try:
        my.deleteproduct(product)
        my.deleteorder(product)
    except:
        print('删除订单出错了')
    return redirect(url_for('admin.index'))

@admin.route('/note',methods=['POST'])
def note():
    if request.method == 'POST':
        orderno = request.form.get('orderno')
        notes = request.form.get('notes')
        my.ad_updateorder_note(orderno,notes)
        return jsonify({'status':'ok'})
