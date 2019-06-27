# -*-coding:utf-8-*-
# @Time : 2019/6/21 上午7:45
# @Author : pyz
# @Project : wiki
# @File : __init__.py
# @Software: PyCharm


from flask import Flask
from app.admin.login import Admin
from app.extensions import db, login_manager, csrf, bootstrap, get_logger

def create_app(config_name):
    app = Flask(__name__)  #app是Flask的实例，接收包或者模块的名字作为参数，但一般都是传递__name__
    app.config.from_pyfile('../Config/setting.py') # 推荐object对象方式
    register_blue(app)

    login_manager.init_app(app) #在extension实例化类 在ini_app方法初始化
    db.init_app(app)
    bootstrap.init_app(app)

    app.config['HOST']
    print(app.config['HOST'])
    logger = get_logger()
    logger.debug("msg")
    return app

#该函数下 标记注册蓝图，并引入试图创建的文件
def register_blue(app):
    app.register_blueprint(Admin, url_prefix='/admin')
    # app.register_blueprint(route_auth, url_prefix="/auth")

