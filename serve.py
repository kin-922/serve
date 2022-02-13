from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Masae　雅惠'

@app.route('/blog')
def blog():
    return 'My thoughts on blogs'