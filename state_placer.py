from turtle import Turtle


class State_placer(Turtle):
    counter = 0

    def __init__(self, x, y, statename):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setx(x)
        self.sety(y)
        self.write(statename, False, align="center")
        State_placer.counter += 1
