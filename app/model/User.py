# -*-coding:utf-8-*-

from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User (db.Model, UserMixin):
#实例化USER模型
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(30))
    about = db.Column(db.Text(128))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def vaildata_password(self, password):
        return check_password_hash(self.password_hash, password)


    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(25), unique=True, nullable=False)
    # email = db.Column(db.String(100), unique=True, nullable=False)
    # password = db.Column(db.String(100), unique=True, nullable=False)
