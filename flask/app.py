from flask import Flask, url_for
from  markupsafe import escape

app = Flask(__name__)

@app.route('/home')
def said_hi():
    return '<h3>test</h3>'
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'
@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'


if __name__ == '__main__' :
    app.run()