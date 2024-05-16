from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return f"""
    <link rel="stylesheet" href="static/style.css">
    <h1>test</h1>
    Ссылка на <a href="{url_for('index')}">index</a> страницу<br>
    """


@app.route('/index')
def index():
     return render_template('index.html')


@app.route('/t-shorts')
def tshorts():
    return render_template('t-shorts.html')


@app.route('/pants')
def pants():
    return render_template('pants.html')


@app.route('/hoodies')
def hoodies():
    return render_template('hoodies.html')


@app.route('/underwear')
def underwear():
    return render_template('underwear.html')


if __name__ == '__main__':
    app.run(debug=True)
