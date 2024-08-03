from flask import Flask, render_template
import requests as rq

app = Flask(__name__)

@app.route('/')
def home():
    global blog_data
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_data = rq.get(blog_url).json()
    return render_template("index.html",blog_data = blog_data)

@app.route('/post/<blog_id>')
def post(blog_id):
    global blog_data

    for post in blog_data:
        if post['id'] == int(blog_id):
            break
    return render_template('post.html',post = post)

if __name__ == "__main__":
    app.run(debug=True)
