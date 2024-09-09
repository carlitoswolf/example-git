#Backend de login

from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/login')
def login():
    return 'Login'

@app.route('/register')
def register():
    return 'Register'

if __name__ == '__main__':
    app.run()

@app.route('/login/<username>') # type: ignore
def login(username):
    return 'Hello, {}!'.format(username)   

