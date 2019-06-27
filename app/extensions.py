# -*-coding:utf-8-*-
#app 扩展文件，引入的类和实例化放到此处

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
import logging, os , sys
from Config import setting

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

# @LoginManager.user_loader
# def load_user(user_id):
#     from app.model import User
#     user = User.query.get(int(user_id))
#     return user



def get_logger():
    logger = logging.getLogger()
    if os.path.exists(setting.LOG_PATH):
        pass
    else:
        os.mkdir(setting.LOG_PATH)
    # 指定logger输出格式
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
    # 文件日志
    file_handler = logging.FileHandler("%s/%s" % (setting.LOG_PATH, setting.LOG_FILE))
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值
    # 为logger添加的日志处理器，可以自定义日志处理器让其输出到其他地方
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    # 指定日志的最低输出级别，默认为WARN级别
    logger.setLevel(logging.INFO)
    return logger