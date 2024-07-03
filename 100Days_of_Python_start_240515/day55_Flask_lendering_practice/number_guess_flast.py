from flask import Flask
import random as rd

app = Flask(__name__)

target = 0

basic_img = '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2s5bXZ2dmtpeTNyZWJueTQ0M2huNGo4dTBmaHo5OG9jZmQ3ZG9sciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4T7e4DmcrP9du/giphy.gif">'
upper_img = '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjVlNnZtZmE3ejYwYXBzc3N5bzE2aW5laWU2MDFjZHI0dWNnMW11eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/P2hdI6VaKlFhxncQG9/giphy.gif">'
lower_img = '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjVlNnZtZmE3ejYwYXBzc3N5bzE2aW5laWU2MDFjZHI0dWNnMW11eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/P2hdI6VaKlFhxncQG9/giphy.gif">'
correct_img = '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjVlNnZtZmE3ejYwYXBzc3N5bzE2aW5laWU2MDFjZHI0dWNnMW11eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/P2hdI6VaKlFhxncQG9/giphy.gif">'

basic_style = 'style="color:red"'
upper_style = 'style="color:blue"'
lower_style = 'style="color:yellow"'
correct_style = 'style="color:green"'


@app.route('/')
def reset():
    global target
    target = rd.randint(1, 10)
    print(target)
    html = f'<h1 {basic_style}>Guess Number!</h1>' \
           f'{basic_img}'

    return html


@app.route('/guess/<int:num>')
def guess(num):
    print(target)
    print(num)

    if num < target:  # 미만
        html = f'<h1 {lower_style}>Guess upper number!</h1>' \
               f'{lower_img}'
    elif num > target:  # 초과
        html = f'<h1 {upper_style}>Guess lower number!</h1>' \
               f'{upper_img}'
    else:  # 정답
        html = f'<h1 {correct_style}>Collect!</h1>' \
               f'{correct_img}'

    return html

if __name__ == '__main__':
    app.run(debug=True)