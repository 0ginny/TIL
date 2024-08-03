from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # 만약 import 가 필요한 함수를 써야할 경우
    random_number = random.randint(1,10)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template('jinja_index.html',num = random_number,
                           today = today)


if __name__ == '__main__':
    app.run(debug=True)