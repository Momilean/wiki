# -*-coding:utf-8-*-
# @Time : 2019/6/21 上午7:50
# @Author : pyz
# @Project : wiki
# @File : form.py
# @Software: PyCharm
#表单文件，给该模块提供from


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError,  \
    PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from app.model.User import User


class BaseForm(FlaskForm):
    LANGUAGES = ['zh']

class LoginFrom (BaseForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('password', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login in')

class RegistFrom(BaseForm):
    # username = StringField('Username', validators=[DataRequired(), Length(4, 20)])
    username = StringField('用户名', validators=[DataRequired(), Length(5, 20),
                                                   Regexp('^[a-zA-Z0-9]*$',
                                                          message='Contain Only aA-zZ and 0-9')])
    # password = PasswordField('密 码', validators=[DataRequired('密码不能为空'), Length(8, 128, message="长度不足"), EqualTo('passwords')])
    # passwords = PasswordField('密 码', validators=[DataRequired('密码不一致')])
    password = PasswordField('密码', validators=[
        DataRequired(),Length(8, 128, message="长度不足"), EqualTo('password2', message='密码不一致')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    name = StringField('昵 称', validators=[DataRequired(), Length(4, 18)])
    submit = SubmitField()



    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('昵称已存在')