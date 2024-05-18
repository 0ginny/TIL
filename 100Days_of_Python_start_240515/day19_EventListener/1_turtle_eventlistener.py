from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# 입력 준비
screen.listen()

# 입력 이벤트
def move_forwards():
    tim.forward(10)

# 입력 이벤트 바인딩
# 만약 함수를 전달할 때 () 를 쓰면, 함수를 실행하는 거야. 전달 할 때는 ()를 빼고 전달해야해.
# higher order function
screen.onkey(key= 'space',fun = move_forwards)

screen.exitonclick()