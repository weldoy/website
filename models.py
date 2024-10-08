from flask_login import UserMixin
from datetime import datetime

from __init__ import db, manager


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)


@manager.user_loader
def load_user(id):
    return User.query.get(id)


class Cart (db.Model):

    __bind_key__ = 'goods'

    product_id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
