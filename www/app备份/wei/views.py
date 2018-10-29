from app.wei import wei
from app.wei.fun import weixi,weixin
from flask import request,render_template,session,redirect,url_for
import requests,json,pymysql


@wei.route('/')
def index():
    return render_template('weixin/login.html')

@wei.route('/api/token', methods=['POST', 'GET'])
def get_auth_token():
    weix = weixi()

    if request.method == 'GET':
        return weix.main()
    else:
        user = weixin()
        user.get_user_info()

        return weix.message()

@wei.route('/api/caidan')
def caidan():
    weix = weixin()
    return weix.caidan()


@wei.route('/login')
def login():
    return render_template('weixin/go.html')


@wei.route('/user')
def user():
    code = request.args.get('code')
    if code:
        data = requests.get('https://api.weixin.qq.com/sns/oauth2/access_token?appid=wxe03a47dc1c18a735&secret=745f4f1daa376908d7294efd727962d7&code=%s&grant_type=authorization_code'%code)
        data = json.loads(data.text)
        url ='https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN'%(data['access_token'],data['openid'])
        data = requests.get(url)
        data.encoding = 'utf-8'
        print(data.text)
        data = json.loads(data.text)
        print(data)

        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "123456", "weixin")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT id FROM name WHERE open_id = '%s'" % data['openid']
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchone()
            print("--------------------------%s-------------------------" % (results))
            session['openid'] = results
            if not results:
                # 关闭数据库连接
                db.close()

                # 打开数据库连接
                db = pymysql.connect("localhost", "root", "123456", "weixin")

                # SQL 插入语句
                sql = """INSERT INTO `name` (`open_id`,
                            `nickname`, `sex`, `headimgurl`) 
                            VALUES ('%s', '%s', '%s', '%s')
                            """ % (data['openid'], data['nickname'], data['sex'], data['headimgurl'])
                print(sql)
                try:
                    # 执行sql语句
                    cursor.execute(sql)
                    # 提交到数据库执行
                    db.commit()
                except:
                    # 如果发生错误则回滚
                    db.rollback()

        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        db.close()



        return render_template('weixin/user.html')

    #return redirect(url_for('wei.login'))
    return render_template('weixin/user.html')

@wei.context_processor
def context():
    username = session.get('user')
    if username:
        return {
            'title':'有用户'
        }
    else:
        return {
            'title':'没有登录'
        }
