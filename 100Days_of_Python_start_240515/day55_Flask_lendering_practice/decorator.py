from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def decorated_func():
        return f'<b>{func()}</b>'
    return decorated_func

def make_emphasis(func):
    def decorated_func():
        return f'<em>{func()}</em>'
    return decorated_func

def make_underlined(func):
    def decorated_func():
        return f'<u>{func()}</u>'
    return decorated_func

@app.route('/')
def home():
    return "Hello World"

@app.route('/hello')
@make_bold
@make_underlined
@make_emphasis
def hello():
    return "hello"

# arg kwarg 이용
class User:
    def __init__(self,name):
        self.name = name
        self.logged = False

def is_authenticated(func):
    def wrapper(*args,**kwargs):
        if args[0].logged == True:
            func(args[0])
    return wrapper


@app.route('/set/<name>')
def setting(name):
    global user
    user = User(name)
    user.logged = True


@app.route('/post')
@is_authenticated
def post(user):
    return f"This is {user.name}'s new blog post"



if __name__ == '__main__':
    app.run(debug=True)