import hashlib, time, json, random,requests,pymysql
from flask import request,session
import xml.etree.ElementTree as ET
import urllib.request as ul_re


class weixi:
    def main(self):
        if request.args.get('echostr'):
            return self.validation_token()
        else:
            return '错误'

    # 微信认证
    def validation(self):
        TOK = 'daqian'
        req = request.args
        signature = req.get('signature')
        timestamp = req.get('timestamp')
        nonce = req.get('nonce')
        # echostr = req.get('echostr')
        array = [str(TOK), str(timestamp), str(nonce)]
        array.sort()
        array = ''.join(array)
        data = hashlib.sha1(array.encode('utf-8'))
        data = data.hexdigest()
        if signature == data:
            return True
        return False

    # 返回验证码
    def validation_token(self):
        if self.validation():
            return '%s' % request.args.get('echostr')
        return '错误'

    # 返回消息
    def message(self):
        xmldata = request.get_data()
        xmldata = str(xmldata, encoding="utf-8")

        xml_rec = ET.fromstring(xmldata)

        self.log(xmldata)

        # 开发者微信号
        ToUserName = xml_rec.find('ToUserName').text
        # 开发者微信号
        fromUser = xml_rec.find('FromUserName').text
        # 消息类型
        MsgType = xml_rec.find('MsgType').text
        # 消息id，64位整型
        MsgId = xml_rec.find('MsgId').text

        # 文字
        if MsgType == 'text':
            # 文本消息内容
            Content = xml_rec.find('Content').text
            return self.MsgType_text(ToUserName, fromUser, Content, MsgId)
        # 图片
        elif MsgType == 'image':
            # 图片消息媒体id，可以调用多媒体文件下载接口拉取数据。
            MediaId = xml_rec.find('MediaId').text
            # 图片链接（由系统生成）
            PicUrl = xml_rec.find('PicUrl').text
            print(MediaId, PicUrl)
            return self.MsgType_image(ToUserName, fromUser, MediaId)
        # 语音
        elif MsgType == 'voice':
            MediaId = xml_rec.find('MediaId').text
            return self.MsgType_voice(ToUserName, fromUser, MediaId)
        # 视频
        elif MsgType == 'video':
            pass
        # 小视频
        elif MsgType == 'shortvideo':
            pass
        elif MsgType == 'location':
            pass
        elif MsgType == 'link':
            pass



    def log(self, logs):
        saveFile = open('log.xml', 'w')
        saveFile.write(logs)
        saveFile.close()  # 操作完文件后一定要记得关闭，释放内存资源

    # 回复文字
    def MsgType_text(self, ToUserName, fromUser, Content, MsgId):
        text = (json.loads(self.baidu_aip(Content)))
        text = text['result']['response']['action_list']
        # strings = text
        intran = random.randint(0, (len(text) - 1))
        strings = text[intran]['say']

        xm = """
        <xml>
        	<ToUserName><![CDATA[%s]]></ToUserName>
        	<FromUserName><![CDATA[%s]]></FromUserName>
        	<CreateTime>%s</CreateTime>
        	<MsgType><![CDATA[text]]></MsgType>
        	<Content><![CDATA[%s]]></Content>
        	<MsgId>%s</MsgId>
        </xml>
        """ % (fromUser, ToUserName, str(int(time.time())), strings, MsgId)
        return xm

    # 回复图片
    def MsgType_image(self, ToUserName, fromUser, MediaId):
        xm = """
            <xml>
                <ToUserName>< ![CDATA[%s] ]></ToUserName>
                <FromUserName>< ![CDATA[%s] ]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType>< ![CDATA[image] ]></MsgType>
                <Image>
                    <MediaId>< ![CDATA[%s] ]></MediaId>
                </Image>
            </xml>
        """ % (fromUser, ToUserName, str(int(time.time())), MediaId)
        print('-----------------' + xm + '--------------------')
        return xm

    # 回复语音
    def MsgType_voice(self, ToUserName, fromUser, MediaId):
        xm = """
            <xml>
                <ToUserName>< ![CDATA[%s] ]></ToUserName>
                <FromUserName>< ![CDATA[%s] ]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType>< ![CDATA[voice] ]></MsgType>
                <Voice>
                    <MediaId>< ![CDATA[%s] ]></MediaId>
                </Voice>
            </xml>
        """ % (fromUser, ToUserName, str(int(time.time())), MediaId)
        print('音频')
        return xm

    # 百度机器人
    def baidu_aip(self, txt):
        url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=24.1be6b60687f8aeeb7ddd11d0b9f9a892.2592000.1540176145.282335-10774392'
        post_data = {
            "bot_session": "",
            "log_id": "7758521",
            "request": {
                "bernard_level": 0,
                "client_session": "{\"client_results\":\"\", \"candidate_options\":[]}",
                "query": txt,
                "query_info": {
                    "asr_candidates": [],
                    "source": "KEYBOARD",
                    "type": "TEXT"
                },
                "updates": "",
                "user_id": "88888"
            },
            "bot_id": "5",
            "version": "2.0"
        }
        encoded_data = json.dumps(post_data).encode('utf-8')
        headers = {'Content-Type': 'application/json'}

        request = ul_re.Request(url, data=encoded_data, headers=headers)
        response = ul_re.urlopen(request)
        content = response.read()
        result = str(content, 'utf-8')
        # print(result)
        return result


class weixin:
    # 获取token
    def get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxe03a47dc1c18a735&secret=745f4f1daa376908d7294efd727962d7'
        data = requests.get(url)
        return json.loads(data.text)['access_token']

    # 修改菜单
    def caidan(self):
        wei = {
            "button": [
                {
                    "name": "菜单",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "搜索",
                            "url": "http://www.daqianwang.top/wei"
                        },
                        {
                            "type": "view",
                            "name": "赞一下我",
                            "url": "http://www.daqianwang.top/admin"
                        }
                    ]
                }
            ]
        }

        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % (self.get_token())
        headers = {'content-type': 'charset=utf8'}
        zhi = requests.post(url, data=wei, headers=headers)
        print(zhi.text)
        return zhi.text


    def get_user_info(self):
        xmldata = request.get_data()
        xmldata = str(xmldata, encoding="utf-8")

        xml_rec = ET.fromstring(xmldata)

        # 开发者微信号
        UserId = xml_rec.find('FromUserName').text

        token = self.get_token()
        url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN'%(token,UserId)
        data = requests.get(url)
        weidata = json.loads(data.text)

        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "123456", "weixin")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT id FROM name WHERE open_id = '%s'" %UserId
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
                    """ %(weidata['openid'],weidata['nickname'],weidata['sex'],weidata['headimgurl'])
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
