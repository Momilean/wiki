# -*-coding:utf-8-*-
# @Time : 2019/6/21 上午7:14
# @Author : pyz
# @Project : wiki
# @File : common.py
# @Software: PyCharm



from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from Config import setting

#公共
print(setting.SECRET_KEY)
user = '1'
name = 'hello'
print(setting.LOG_PATH)
def generate_token(user, name, expire_in=None, **kwargs):
    s = Serializer(setting.SECRET_KEY, expires_in = expire_in)
    data = {'id': user,'name':name}
    data.update(**kwargs)
    return s.dumps(data)

# def generate_token(user, operation, expire_in=None, **kwargs):
#     s = Serializer(current_app.config['SECRET_KEY'], expire_in)
#
#     data = {'id': user.id, 'operation': operation}
#     data.update(**kwargs)
#     return s.dumps(data)