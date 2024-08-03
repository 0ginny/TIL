from flask import Flask, render_template
import random
import datetime
import requests as rq



app = Flask(__name__)

@app.route('/')
def home():
    # 만약 import 가 필요한 함수를 써야할 경우
    random_number = random.randint(1,10)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template('jinja_index.html',num = random_number,
                           today = today)

@app.route('/guess/<name>')
def guess(name):
    age_api = rq.get(f"https://api.agify.io?name={name}")
    gender_api = rq.get(f"https://api.genderize.io?name={name}")
    age = age_api.json()["age"]
    gender = gender_api.json()["gender"]
    return f"<h1>Hey {name},</h1>" \
           f"<h2>I think you are {gender},</h2>" \
           f"<h3>And maybe {age} years old."



if __name__ == '__main__':
    app.run(debug=True)