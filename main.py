from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return f"""
    <h1>test</h1>
    Ссылка на <a href="{url_for('index')}">index</a> страницу<br>
    """


@app.route('/index')
def index():
     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
