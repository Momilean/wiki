# -*-coding:utf-8-*-
# @Time : 2019/6/21 上午7:16
# @Author : pyz
# @Project : wiki
# @File : __init__.py
# @Software: PyCharm


from flask import Blueprint
import os


# 创建该模块下的蓝图, 一般在视图的文件中。建议置于此初始化文件中
Admin = Blueprint('Admin', __name__, template_folder='../templates/admin')
# 导入蓝图视图
from app.admin import login
