from flask import render_template, request, redirect, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from __init__ import app, db
from models import User, Cart


@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')


@app.route('/tshirts', methods=['GET', "POST"])
def tshirts():
    return render_template('t-shirts.html')


@app.route('/pants', methods=["GET", "POST"])
def pants():
    return render_template('pants.html')


@app.route('/hoodies', methods=["GET", "POST"])
def hoodies():
    return render_template('hoodies.html')


@app.route('/underwear', methods=["GET", "POST"])
def underwear():
    return render_template('underwear.html')


@app.route('/proof_of_tshirt', methods=["GET", "POST"])
def proof_of_tshirt():
    return render_template('proof_of_tshirt.html')


@app.route('/proof_of_pants', methods=["GET", "POST"])
def proof_of_pants():
    return render_template('proof_of_pants.html')


@app.route('/proof_of_hoodies', methods=["GET", "POST"])
def proof_of_hoodies():
    return render_template('proof_of_hoodies.html')


@app.route('/proof_of_underwear', methods=["GET", "POST"])
def proof_of_underwear():
    return render_template('proof_of_underwear.html')


@app.route('/base', methods=["GET", "POST"])
def base():
    return render_template('base.html')


@app.route('/order', methods=["GET", "POST"])
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
    login_old = User.query.order_by(User.login).all()
    login_list = []
    for el in login_old:
        login_list.append(el.login)

    if request.method == "POST":
        if not (login or password or password2):
            flash('Пожалуйста заполните поля')
        elif password != password2:
            flash('Пароли не совпадают')
        elif login in login_list:
            flash('Такой логин уже существует!')
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


@app.route('/personal', methods=["GET", "POST"])
@login_required
def personal():
    now_user = current_user
    return render_template('personal_cab.html', current_user=now_user)


@app.route('/admin', methods=["GET", "POST"])
@login_required
def admin():
    goodsname = request.form.get('goodsname')
    goodsold = Cart.query.order_by(Cart.product).all()
    goods_list = []
    for el in goodsold:
        goods_list.append(el.product)

    if request.method == "POST":
        if not (goodsname):
            flash('Пожалуйста заполните поля')
        elif goodsname in goods_list:
            flash('Такой товар уже существует!')
        else:
            flash('Товар добавлен в базу данных')
            new_goods = Cart(product=goodsname)
            db.session.add(new_goods)
            db.session.commit()

            return redirect(url_for('admin'))
    return render_template('admin.html')


@app.route('/basepage', methods=["GET", "POST"])
@login_required
def basepage():
    goods = Cart.query.order_by(Cart.date.desc()).all()
    return render_template('basepage.html', goods=goods)


@app.route('/basepage/<int:id>/complete')
def complete_task(id):
    goods = Cart.query.get_or_404(id)

    try:
        db.session.delete(goods)
        db.session.commit()
        return redirect('/basepage')
    except:
        'Произошла ошибка при удалении товара'


@app.route('/1')
def error1():
    return redirect('/')
