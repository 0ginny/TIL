from flask import Flask

app = Flask(__name__)

# __name__의 의미 : 작동되는 파일? 같은 느낌?
print(__name__)  # __main__
print(Flask.__name__)


@app.route('/')
def hello_world():
    # 렌더링을 하려면 html 한 것처럼 tag를 넣으면 됨
    # gif source : https://giphy.com/
    return '<h1>Hello, World!</h1>' \
           '<p>this is a paragraph</p>' \
           '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2d4YXllZHR6d21pZ3U2dWFydWE2NGllMm56MWU3YXk0eTRhZ2FhbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/t9aSNTJ4YSJFUW0dkB/giphy.gif">'

# 변수를 입력할 때는 <>안에 넣기
@app.route('/username/<name>/<int:age>')
def greet(name,age):
    return f'my name is {name} ,and {age} years old !!'


# window는 set으로 해야해.
# terminal 에 실행 (Command Prompt 로 실행)
# cd 100Days_of_Python_start_240515/day54_flask
# set FLASK_APP=flask_practice.py

# 두번째 방법
if __name__ == "__main__":
    # debug를 넣으면 수정하는 즉시 바로 반영이됨
    app.run(debug=True)
