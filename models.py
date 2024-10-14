from flask_login import UserMixin
from datetime import datetime
from hashlib import md5

from __init__ import db, manager


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'


@manager.user_loader
def load_user(id):
    return User.query.get(id)


class Cart (db.Model):

    __bind_key__ = 'goods'

    product_id = db.Column(db.Integer, primary_key=True)
    collection = db.Column(db.String(64), nullable=False)
    product = db.Column(db.String(64), nullable=False)
    product_price = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())


class Trade (db.Model):

    __bind_key__ = 'trade'

    trade_id = db.Column(db.Integer, primary_key=True)
    trade_prod_id = db.Column(db.String(64), nullable=False)
    trade_prod_name = db.Column(db.String(64), nullable=False)
    trade_prod_price = db.Column(db.String(64), nullable=False)
    trade_prod_size = db.Column(db.String(64), nullable=False)
    trade_user_id = db.Column(db.String(64), nullable=False)
    trade_user_email = db.Column(db.String(64), nullable=False)
    trade_date = db.Column(db.DateTime, default=datetime.now())
