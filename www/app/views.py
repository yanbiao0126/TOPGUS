from app import app
from flask import request, render_template, redirect, url_for, abort, session, jsonify,flash
from app.funtion import login_required
from app.forms import login_form,addname_form
import requests, json,time,random
from app.mysql import mydb

my = mydb()

@app.route('/')
@login_required
def index():
    #user = session.get('user')
    #length = my.get_order_len(user[0])
    #return render_template('home.html',length = length[0])
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if not session.get('user'):
        forms = login_form()
        if request.method == "POST":
            if forms.validate_on_submit():
                data = forms.data
                phone = data['phone']
                pwsd = data['pwsd']
                user = my.get_name(phone,pwsd)
                if user:
                    session['user'] = user
                    print(session.get('user'))
                    return redirect(url_for('index'))
                else:
                    flash('账号或密码错误')
        return render_template('login.html', form=forms)
    else:
        return redirect(url_for('index'))


@app.route('/addname/', methods=['POST', 'GET'])
def addname():
    if not session.get('user'):
        forms = addname_form()
        if request.method == "POST":
            if forms.validate_on_submit():
                data = forms.data
                user = data['user']
                phone = data['phone']
                email = data['email']
                pwsd = data['pwsd']
                code = data['code']
                if my.get_name_emali(email):
                    flash('邮箱被占用')
                elif my.get_name_phone(phone):
                    flash('手机号被占用')
                elif not my.get_code(phone,code):
                    flash('验证码与手机号不符')
                else:
                    my.addname(email, phone, pwsd,user)
                    return redirect(url_for('login'))
        return render_template('new.html', form=forms)
    return redirect(url_for('index'))


# @app.route('/login/', methods=['POST', 'GET'])
# @login_required
# def login():
#     print('到这了')
#     forms = login_form()
#     user = my.get_name(session.get('user'))
#     print(user)
#     titles = True
#     for i in user:
#         if i == None or i == '':
#             titles = False
#     if titles:
#         return redirect(url_for('home'))
#
#     if request.method == "POST":
#         if forms.validate_on_submit():
#             data = forms.data
#             phone = data['phone']
#             email = data['email']
#             code = data['code']
#             iss = my.get_code(session.get('user')[0])
#             if iss:
#                 if int(code) == int(iss[1]):
#                     my.updatename(session.get('user')[0], phone, email)
#                     return redirect(url_for('home'))
#             flash('验证码与手机号不符')
#             return render_templa
#                 <div style="text-align: center">
#                     <img src='{{ name[4] }}' alt="">
#                     <p style="text-align: center">{{ name[2] }}</p>
#                 </div>te('login.html', form=forms)
#
#         else:
#             return render_template('login.html', form=forms)
#     return render_template('login.html', form=forms)


@app.route('/code',methods=['POST'])
#@login_required
def code():
    if request.method == 'POST':
        try:
            phone = request.form.get('phone')
            phones = requests.post(url='http://www.daodianwang.com/Tantou/SmsVerification/message',data={'phone':phone})
            data=json.loads(phones.text)
            cod = data['result']['code']
            tim = data['result']['time']
            phone = data['result']['phone']
            print(phone,cod)
            cods = my.get_phone(phone)
            if cods:
                # 更新
                my.update_code(phone, cod, tim)
            else:
                # 添加
                my.addcode(phone, cod, tim)


            print(cods)
            return jsonify({'status':'ok'})
        except:
            return jsonify({'status': '0'})
#
#
#
# @app.route('/home')
# @login_required
# def home():
#     return render_template('home.html')
#
@app.route('/addorder',methods=['POST','GET'])
@login_required
def addorder():
    if request.method == "POST":
        datax = request.form.to_dict()
        # 订单号
        orderno = time.strftime("%Y%m%d%H%M%S", time.localtime())+str(random.randint(0,9))\
                  +str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        user = session.get('user')

        # 商品数量
        lenst =0
        # 创建订单
        for data in datax:
            dat = (datax[data]).strip()
            if len(dat) > 0 and data.find('data') == 0:
                lenst += 1
        if lenst > 0:
            # 创建订单
            my.addorder(orderno, user[0], lenst)
            shuliang = 0
            # 创建商品
            for data in datax:
                dat = (datax[data]).strip()
                if len(dat) > 0 and data.find('data') == 0:
                    if not my.ifproduct(orderno,dat):
                        shuliang += 1
                        my.addproduct(orderno,dat)
            my.updateorder(orderno,shuliang)

            # 最新订单号
            session['orderno'] = orderno

            # content = str(datax)
            # print(len(datax))
            # resp = Response_headers(content)
            # print(resp.get_data)
            # print(resp.data)
            #print(type(resp))
            #return resp
            return redirect(url_for('order'))
        return redirect(url_for('home'))


@app.route('/order')
@login_required
def order():
    orderno = my.get_order(session['orderno'])
    product = my.get_product(session['orderno'])
    #print(orderno,product)
    img_url = int(int(orderno[2])*9.9)

    # 判断订单数量
    # user = session.get('user')
    # print(user[0])
    # length = my.get_order_len(user[0])
    # print(length)
    return render_template('order.html',orderno = orderno,product = product,img_url=img_url)

@app.route('/deleteproduct/<int:product>')
def deleteproduct(product):
    try:
        my.deleteproduct(product)
        my.deleteorder(product)
    except:
        print('删除订单出错了')
    return redirect(url_for('index'))

@app.route('/ok')
def ok():
    print(session['orderno'])
    my.ad_updateorder_2(session['orderno'])
    return render_template('ok.html')

# @app.context_processor
# def content():
#     open_id = session.get('user')
#     if open_id:
#         username = my.get_name(open_id)
#         return {
#             'title': '关键词',
#             'name': username
#         }
#     else:
#         return {
#             'title': '关键词'
#         }
#
#
# @app.errorhandler(400)
# def excep():
#     return '<h1>页面被吃了</h1>'
#
#
# @app.errorhandler(404)
# def excep():
#     return '<h1>页面不存在</h1>'
