from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# aws에서 실행
if __name__ == '__main__':
    app.run('0.0.0.0',port=3001,debug=True)