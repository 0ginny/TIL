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

@app.route('/hello')
@make_bold
@make_underlined
@make_emphasis
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)