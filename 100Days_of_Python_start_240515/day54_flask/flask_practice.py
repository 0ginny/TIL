from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# window는 set으로 해야해.
# terminal 에 실행 (Command Prompt 로 실행)
# cd 100Days_of_Python_start_240515/day54_flask
# set FLASK_APP=flask_practice.py