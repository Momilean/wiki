# -*-coding:utf-8-*-
# @Time : 2019/6/21 上午7:41
# @Author : pyz
# @Project : wiki
# @File : setting.py
# @Software: PyCharm

import os

#配置文件
DEBUG = True

#log
LOG_PATH = 'logs'
LOG_FILE = 'message'
HOST = '127' #测试配置

# 密钥 随机字符串
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:123456@127.0.0.1/wiki"
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/wiki'
SQLALCHEMY_TRACK_MODIFICATIONS = False