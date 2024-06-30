from flask import Flask

app = Flask(__name__)

# __name__의 의미 : 작동되는 파일? 같은 느낌?
print(__name__) # __main__
print(Flask.__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 변수를 입력할 때는 <>안에 넣기
@app.route('/username/<name>')
def greet(name):
    return f'Hello {name}!!'

# window는 set으로 해야해.
# terminal 에 실행 (Command Prompt 로 실행)
# cd 100Days_of_Python_start_240515/day54_flask
# set FLASK_APP=flask_practice.py

# 두번째 방법
if __name__ == "__main__":
    # debug를 넣으면 수정하는 즉시 바로 반영이됨
    app.run(debug=True)