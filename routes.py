from flask import render_template, request, redirect, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user

from __init__ import app, db
from models import User


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/tshirts', methods=['GET'])
def tshirts():
    return render_template('t-shirts.html')


@app.route('/pants', methods=['GET'])
def pants():
    return render_template('pants.html')


@app.route('/hoodies', methods=['GET'])
def hoodies():
    return render_template('hoodies.html')


@app.route('/underwear', methods=['GET'])
def underwear():
    return render_template('underwear.html')


@app.route('/proof_of_tshirt', methods=['GET'])
def proof_of_tshirt():
    return render_template('proof_of_tshirt.html')


@app.route('/proof_of_pants', methods=['GET'])
def proof_of_pants():
    return render_template('proof_of_pants.html')


@app.route('/proof_of_hoodies', methods=['GET'])
def proof_of_hoodies():
    return render_template('proof_of_hoodies.html')


@app.route('/proof_of_underwear', methods=['GET'])
def proof_of_underwear():
    return render_template('proof_of_underwear.html')


@app.route('/base', methods=['GET'])
def base():
    return render_template('base.html')


@app.route('/order', methods=['GET'])
@login_required
def order():
    return render_template('order.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
        
            next_page = request.args.get('next', 1)

            return redirect(next_page)
        else:
            flash('Неправильный логин или пароль')
    else:
        flash('Пожалуйста заполните поля авторизации')

    return render_template('login.html')


@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=["GET", "POST"])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == "POST":
        if not (login or password or password2):
            flash('Пожалуйста заполните поля')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))

    return render_template('register.html')


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login') + '?next=' + request.url)
    
    return response


@app.route('/personal', methods=['GET'])
def personal():
    return render_template('personal_cab.html')
