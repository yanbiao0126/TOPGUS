import pymysql,datetime,time
import random


class mydb:
    def min(self):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com',port=5511,user='topgus_f',passwd='Dear8717914',db='topgus',charset='utf8')
        return db

    # 保存基本信息
    def addname(self, email, phone, pwd,user):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        open_id = random.randint(1000000000, 99999999999)
        # SQL 插入语句
        sql = "INSERT INTO name(open_id,email,phone,pwd,user) VALUES('%s','%s',%d,'%s','%s')" % (open_id, email, int(phone), pwd,user)
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)

            # 提交到数据库执行
            db.commit()
            print('保存成功')
        except Exception as err:
            # Rollback in case there is any error
            db.rollback()
            print(err)
        db.close()


    # 添加数据手机和邮箱
    def updatename(self, id, phone, email):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """UPDATE name SET PHONE = \'%s\',EMAIL = \'%s\'  WHERE open_id = \'%s\' """ % (phone, email, id)
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            return '保存完成'
        except:
            # Rollback in case there is any error
            db.rollback()
            return '保存失败'

        db.close()

    # 创建订单
    def addorder(self, orderno, userid, count):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        DaTe = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = """INSERT INTO orders(orderno,open_id,count,time)
                         VALUES (\'%s\',\'%s\',%d,\'%s\')""" % (orderno, userid, count,DaTe)
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()


    # 更新订单数量
    def updateorder(self, orderno, lens):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """UPDATE orders SET COUNT = '%s' WHERE orderno = '%s'""" % (lens,orderno)
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

    # 删除订单
    def deleteorder(self, orderno):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """DELETE FROM orders WHERE ORDERNO = \'%s\' """ % (orderno)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

    # 添加商品
    def addproduct(self, orderno, keyword):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """INSERT INTO product(ORDERNO,KEYWORD)
                         VALUES (\'%s\',\'%s\')""" % (orderno, keyword)
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

    # 判断是否重复商品
    def ifproduct(self, orderno, keyword):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """SELECT * FROM  product WHERE orderno = '%s' and keyword = '%s'""" % (orderno, keyword)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results


    # 更新商品
    def updateproduct(self, orderno, keyword):
        db = min()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """UPDATE PRODUCT SET KEYWORD = %s  WHERE ORDERNO = %s """ % (keyword, orderno)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()


    # 删除商品
    def deleteproduct(self, orderno):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """DELETE FROM product WHERE ORDERNO = \'%s\' """ % (orderno)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

    # 生成手机验证码
    def addcode(self, phone, code, tim):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """INSERT INTO code(phone,code,time)
                         VALUES (\'%s\',\'%s\',\'%s\')""" % (phone, code, tim)
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

    # 更新手机验证码
    def update_code(self, phone, code, tim):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句

        sql = """UPDATE code SET code = %d,time = \'%s\'  WHERE phone = \'%s\'""" % (code, tim, phone)
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

    # 查询openid
    def get_openid(self,openid):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """SELECT open_id FROM name WHERE open_id =\'%s\' """ % (openid)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 查询手机邮箱
    def get_name_emali(self, email):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()



        # SQL 插入语句
        sql = """select * from name where email= '%s'"""%email
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 查询手机号码
    def get_name_phone(self, phone):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """select * from name where phone= %s""" % phone
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 用户登录
    def get_name(self, phone,pwd):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """select open_id from name where phone= '%s' and pwd = '%s'""" % (phone,pwd)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 管理员用户登录
    def get_admin_name(self, phone, pwd):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """select id from admin where admin= '%s' and pwd = '%s'""" % (phone, pwd)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 查询管理员ID
    def get_admin_id(self, openid):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """SELECT id FROM admin WHERE id =\'%s\' """ % (openid)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results





    # 查询订单
    def get_order(self, order):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """SELECT * FROM orders WHERE orderno =\'%s\' """ % (order)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 查询订单数量
    def get_order_len(self, openid):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """SELECT COUNT(o.orderno) FROM orders o WHERE o.open_id = \'%s\'""" % openid
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 查询相应商品
    def get_product(self, order):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """SELECT keyword FROM product WHERE orderno =\'%s\' """ % (order)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取全部记录列表
            results = cursor.fetchall()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 查找手机验证码
    def get_code(self, phone,cod):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句

        sql = """SELECT * FROM code WHERE phone = \'%s\' and code = \'%s\' """ % (phone,cod)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

        # 查找手机验证码
    def get_phone(self, phone):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句

        sql = """SELECT * FROM code WHERE phone = \'%s\' """ % (phone)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchone()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results





    # 后台查询
    # select  n.nickname '用户名',o.orderno '订单号', o.count '数量', p.keyword '商品'  from `name` n,product p,orders o where n.open_id = o.open_id and o.orderno = p.orderno;

    #select n.nickname '用户名',o.orderno '订单号', o.count '数量', (select GROUP_CONCAT(t.keyword) FROM product t WHERE t.orderno = o.orderno) '商品'  from `name` n, orders o where n.open_id = o.open_id ;
    def ad_get_order(self,page):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        page = page*10
        sql = """select n.phone '手机号',n.email '邮箱',o.orderno '订单号',o.time '时间', o.count '数量', (SELECT GROUP_CONCAT(t.keyword)FROM product t WHERE t.orderno = o.orderno) '商品',o.is_ok '已审核',n.user '微信号',o.note '备注'  FROM `name` n, orders o WHERE n.open_id = o.open_id ORDER BY  o.orderno DESC"""
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取全部记录列表
            results = cursor.fetchall()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 查询用户列表
    def ad_get_name(self):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """SELECT * FROM name"""
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取一条记录列表
            results = cursor.fetchall()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()
        return results

    # 更新审核
    def ad_updateorder(self, isok):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """UPDATE orders SET is_ok = '1' WHERE orderno = '%s'""" % isok
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

    # 更新审核
    def ad_updateorder_2(self, isok):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """UPDATE orders SET is_ok = '2' WHERE orderno = '%s'""" % isok
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

    # 更新订单备注
    def ad_updateorder_note(self, orderno,notes):
        # 打开数据库连接
        db = pymysql.connect(host='pbbf0v0d.2320.dnstoo.com', port=5511, user='topgus_f', passwd='Dear8717914',
                             db='topgus', charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = """UPDATE orders SET note = '%s' WHERE orderno = '%s'""" % (notes,orderno)
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        db.close()

