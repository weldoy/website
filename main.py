from flask import Flask
from flask import render_template
from flask import url_for
import smtplib

app = Flask(__name__)


@app.route('/')
def hello():
    return f"""
    <link rel="stylesheet" href="static/style.css">
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


# <------------------------------->

def send_email(message):
    sender = "your email"
    password = "your password"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, f"Subject: NEW EMAIL FOR SENDER\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    message = input("Text your message: ")
    print(send_email(message=message))

# <------------------------------->

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/order')
def order():
    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)
