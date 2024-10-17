from flask import render_template, request, redirect, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from __init__ import app, db
from models import User, Cart, Trade


@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')


@app.route('/tshirts', methods=['GET', "POST"])
def tshirts():
    goods = Cart.query.order_by(Cart.date.desc()).all()
    return render_template('collections/t-shirts.html', goods=goods)


@app.route('/pants', methods=["GET", "POST"])
def pants():
    goods = Cart.query.order_by(Cart.date.desc()).all()
    return render_template('collections/pants.html', goods=goods)


@app.route('/hoodies', methods=["GET", "POST"])
def hoodies():
    goods = Cart.query.order_by(Cart.date.desc()).all()
    return render_template('collections/hoodies.html', goods=goods)


@app.route('/underwear', methods=["GET", "POST"])
def underwear():
    goods = Cart.query.order_by(Cart.date.desc()).all()
    return render_template('collections/underwear.html', goods=goods)



@app.route('/base', methods=["GET", "POST"])
def base():

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:
    
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
    email = request.form.get('email')

    login_old = User.query.order_by(User.login).all()
    login_list = []
    for el in login_old:
        login_list.append(el.login)

    email_old = User.query.order_by(User.email).all()
    email_list = []
    for el in email_old:
        email_list.append(el.email)

    if request.method == "POST":
        if not (login or password or password2 or email):
            flash('Пожалуйста заполните поля')
        elif password != password2:
            flash('Пароли не совпадают')
        elif login in login_list:
            flash('Такой логин уже существует!')
        elif email in email_list:
            flash('Такая почта уже существует!')
        else:

            password = password.replace(' ', '')
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login.replace(' ', ''), password=hash_pwd, email=email.replace(' ', ''))
            db.session.add(new_user)
            db.session.commit()

            if new_user.id == 1:
                new_user.admin = True
                db.session.commit()
            else:
                pass

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


@app.route('/addinggoods', methods=["GET", "POST"])
@login_required
def addinggoods():

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        collection = request.form.get('collection')
        product_price = request.form.get('product_price')
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
                new_goods = Cart(product=goodsname.capitalize(), 
                                 collection=collection.lower().replace(' ', ''),
                                 product_price=product_price.replace(' ', ''))
                db.session.add(new_goods)
                db.session.commit()

                return redirect(url_for('addinggoods'))
        return render_template('cabinet/addinggoods.html')


@app.route('/basepage', methods=["GET", "POST"])
@login_required
def basepage():
    goods = Cart.query.order_by(Cart.date.desc()).all()

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        return render_template('cabinet/basepage.html', goods=goods)


@app.route('/basepage/<int:id>/complete')
@login_required
def complete_task(id):
    goods = Cart.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        try:
            db.session.delete(goods)
            db.session.commit()
            flash('Товар удален!')
            return redirect('/basepage')
        except:
            return 'Произошла ошибка при удалении товара'


@app.route('/1')
def error1():
    return redirect('/')


@app.route('/users', methods=["GET", "POST"])
@login_required
def users():
    users = User.query.order_by(User.login).all()

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        return render_template('cabinet/users.html', users=users)


@app.route('/users/<int:id>/delete')
@login_required
def delete_user(id):
    users = User.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        try:
            db.session.delete(users)
            db.session.commit()
            flash('Пользователь удален!')
            return redirect('/users')
        except:
            return 'Произошла ошибка при удалении пользователя'


@app.route('/users/<int:id>/edit', methods=["GET", "POST"])
@login_required
def edituser(id):
    user = User.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        return render_template('date_edit/edituser.html', user=user)


@app.route('/users/<int:id>/edit/login', methods=["GET", "POST"])
@login_required
def editlogin(id):
    user = User.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        return render_template('date_edit/editlogin.html', user=user)
    


@app.route('/users/<int:id>/edit/login/complete', methods=["GET", "POST"])
@login_required
def editcomplete(id):
    user = User.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        newlogin = request.form.get('newlogin')
        oldlogin = User.query.order_by(User.login).all()
        login_list = []
        for el in oldlogin:
            login_list.append(el.login)

        if request.method == "POST":
            if not (newlogin):
                pass
            elif newlogin in login_list:
                pass
            else:
                db.session.query(User).filter(User.login == user.login).update({User.login : newlogin.replace(' ', '')})
                db.session.commit()
        flash('Логин изменен!')
        return redirect(url_for('users'))


@app.route('/users/<int:id>/edit/email', methods=["GET", "POST"])
@login_required
def editemail(id):
    user = User.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        return render_template('date_edit/editemail.html', user=user)
    


@app.route('/users/<int:id>/edit/email/complete', methods=["GET", "POST"])
@login_required
def editemailcomplete(id):
    user = User.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        newemail = request.form.get('newemail')
        oldemail = User.query.order_by(User.email).all()
        email_list = []
        for el in oldemail:
            email_list.append(el.email)

        if request.method == "POST":
            if not (newemail):
                pass
            elif newemail in email_list:
                pass
            else:
                db.session.query(User).filter(User.email == user.email).update({User.email : newemail.replace(' ', '')})
                db.session.commit()
        flash('Почта изменена!')
        return redirect(url_for('users'))


@app.route('/users/<int:id>/edit/status', methods=["GET", "POST"])
@login_required
def editstatus(id):
    user = User.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        return render_template('date_edit/editstatus.html', user=user)
    


@app.route('/users/<int:id>/edit/status/complete', methods=["GET", "POST"])
@login_required
def editstatuscomplete(id):
    user = User.query.get_or_404(id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        newstatus = request.form.get('newstatus')

        if request.method == "POST":
            if (newstatus.replace(' ', '') == 'True' 
                or newstatus.replace(' ', '') == '1'):
                user.admin = True
                db.session.commit()
            elif (newstatus.replace(' ', '') == 'False' 
                or newstatus.replace(' ', '') == '0'):
                user.admin = False
                db.session.commit()
            else:
                pass
        flash('Статус изменен!')
        return redirect(url_for('users'))


@app.route('/trades', methods=["GET", "POST"])
@login_required
def trades():

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        trade = Trade.query.order_by(Trade.trade_date.desc()).all()
        
        return render_template('cabinet/trades.html', trade=trade)


@app.route('/trades/<int:trade_id>/delete')
@login_required
def delete_trade(trade_id):
    trade = Trade.query.get_or_404(trade_id)

    if current_user.admin == False:
        return 'Sorry, you have not special access for that page'
    else:

        try:
            db.session.delete(trade)
            db.session.commit()
            flash('Заказ удален!')
            return redirect('/trades')
        except:
            return 'Произошла ошибка при удалении заказа'


@app.route('/<int:product_id>/proof', methods=["GET", "POST"])
def proof(product_id):
    product = Cart.query.get_or_404(product_id)

    return render_template('proof.html', product=product)


@app.route('/<int:product_id>/proof/success', methods=["GET", "POST"])
@login_required
def proof_success(product_id):
    product = Cart.query.get_or_404(product_id)

    product_price = product.product_price
    product_size = request.form.get('size')
    user_id = current_user.id
    user_email = current_user.email

    if request.method == "POST":
        new_trade = Trade(trade_prod_id=product_id, trade_prod_name=product.product, 
                          trade_prod_price=product_price, trade_prod_size=product_size,
                          trade_user_id=user_id, trade_user_email=user_email)

        db.session.add(new_trade)
        db.session.commit()
        flash('Заказ создан!')

        if product.collection == 'футболка':
            return redirect(url_for('tshirts'))
        elif product.collection == 'штаны':
            return redirect(url_for('pants'))
        elif product.collection == 'кофта':
            return redirect(url_for('hoodies'))
        elif product.collection == 'белье':
            return redirect(url_for('underwear'))
    return redirect(url_for('index'))
