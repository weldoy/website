from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'krfiyg3wiyti43uiwhyfgsdih334'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///profiles.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SQLALCHEMY_BINDS'] = {
    'goods': 'sqlite:///goods.db'
}

db = SQLAlchemy(app)
manager = LoginManager(app)
manager.login_view = 'login'
manager.login_message_category = 'info'

with app.app_context():
    db.create_all()


@app.before_request
def create_tables():
     db.create_all()


import routes
