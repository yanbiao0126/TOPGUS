from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length,Regexp,EqualTo


class addname_form(Form):
    user = StringField('微信号', validators=[DataRequired('请输入内容')])
    email = StringField('邮箱',validators=[DataRequired('请输入内容'),Email('邮箱格式有误')])
    phone = StringField('手机号',validators=[DataRequired('请输入手机号码'),Regexp("1[3578]\d{9}", message="手机格式不正确")])
    code = StringField('验证码',validators=[Length(6,6,message='验证码错误')])
    pwsd = PasswordField('密码', validators=[DataRequired('请输入内容'), Length(6,16,message='请输入 6-16 位')])
    ispwd = PasswordField('确认密码', validators=[EqualTo('pwsd',message='两次密码必须一致')])
    submit = SubmitField('提交')


class login_form(Form):
    phone = StringField('手机号', validators=[DataRequired('请输入手机号码'), Regexp("1[3578]\d{9}", message="手机格式不正确")])
    pwsd = PasswordField('密码', validators=[DataRequired('请输入内容'), Length(6, 16, message='请输入 6-16 位')])
    submit = SubmitField('提交')