# -*-coding:utf-8-*-
# @Time : 2019/6/27 上午7:24
# @Author : pyz
# @Project : wiki
# @File : login.py
# @Software: PyCharm
# 后台登录 退出 注册文件

from app.admin import Admin
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, logout_user, login_user
from app.admin.form import RegistFrom, LoginFrom
from app.extensions import db, get_logger
from app.model.User import User


logger = get_logger()

#Admin蓝图装饰器  以Admin.route注册的函数都会自带/admin，所以该试图函数的url是/admin/函数名
@Admin.route('/login', methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginFrom()
    if form.validate_on_submit():
        try:
            form.validate_on_submit()
        except Exception as e:
            print(e)
            users = User.query.filter_by(email=form.email.data).first()
            if users is not None and users.verify_password(form.password.data):
                login_user(users, form.remember_me.data)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                return redirect(next)
            flash(u'无效的凭证' )
            logger.debug("login")

    return render_template('login.html', form=form)

@Admin.route('/register', methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('.login'))
    form = RegistFrom()
    # if form.validate_on_submit():
    #     username = User.query.filter_by(username=form.username.data.lower()).first()
    #     if username is not None and User.vaildata_password(form.password.data)
    #         if
    if request.method == 'POST' and  form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        name  = form.name.data
        user = User(username=username, password_hash=password, name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash(u'Thanks for registering', 'info')
        return redirect(url_for('.login'))
        logger.debug('db user id is %s, detail is %s' % (user.username, user))
    return render_template('admin/register.html', form=form )
