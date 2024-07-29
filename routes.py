from flask import render_template, url_for, redirect, url_for
from __init__ import app


@app.route('/')
def hello():
    return f"""
    <link rel="stylesheet" href="{ url_for('static', filename='style.css') }">
    <h1>test</h1>
    Ссылка на <a href="{url_for('index')}">index</a> страницу<br>
    <p></p>
    Ссылка на <a href="{url_for('base')}">base</a> страницу<br>
    <p></p>
    Ссылка на <a href="{url_for('order')}">order</a> страницу<br>
    """


@app.route('/index')
def index():
     return render_template('index.html')


@app.route('/tshirts')
def tshirts():
    return render_template('t-shirts.html')


@app.route('/pants')
def pants():
    return render_template('pants.html')


@app.route('/hoodies')
def hoodies():
    return render_template('hoodies.html')


@app.route('/underwear')
def underwear():
    return render_template('underwear.html')


@app.route('/proof_of_tshirt')
def proof_of_tshirt():
    return render_template('proof_of_tshirt.html')


@app.route('/proof_of_pants')
def proof_of_pants():
    return render_template('proof_of_pants.html')


@app.route('/proof_of_hoodies')
def proof_of_hoodies():
    return render_template('proof_of_hoodies.html')


@app.route('/proof_of_underwear')
def proof_of_underwear():
    return render_template('proof_of_underwear.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/order')
def order():
    return render_template('order.html')
