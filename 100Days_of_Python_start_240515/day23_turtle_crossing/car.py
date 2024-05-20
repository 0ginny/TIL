import turtle as t
import random as rd

CAR_SHAPE = 'square'
COLORS = ['red','blue','yellow','green','purple','orange','navy','gray']
CAR_SPEED = 0.1
MOVE_DISTATNCE = 10
NUM_CARS = 10
HEADING = 180

STRETCH_LEN = 2
STRETCH_WID = 1

X_MIN_RANGE = 0 #250
X_MAX_RANGE = 250
Y_MIN_RANGE = -200
Y_MAX_RANGE = 200

# class Car(t.Turtle):
#     def __init__(self):
#         super().__init__()
#
#

class Cars():
    def __init__(self):
        self.cars = []
        for _ in range(NUM_CARS):
            self.create_car()
        self.car_speed = CAR_SPEED

    def create_car(self):
        car = t.Turtle()
        car.shape(CAR_SHAPE)
        car.color(rd.choice(COLORS))
        car.turtlesize(stretch_len=STRETCH_LEN,stretch_wid=STRETCH_WID)
        car.penup()
        pos_x = rd.randint(X_MIN_RANGE,X_MAX_RANGE)
        pos_y = rd.randint(Y_MIN_RANGE,Y_MAX_RANGE)
        car.goto(pos_x,pos_y)
        car.setheading(HEADING)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.fd(MOVE_DISTATNCE)

