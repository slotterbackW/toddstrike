import turtle

class Bullet:

    def __init__(self, x, y, heading, speed):
        self.bullet = turtle.Turtle()
        self.bullet.ht()
        self.bullet.penup()
        self.bullet.setpos(x, y)
        self.bullet.setheading(heading)
        self.bullet.pendown()
        self.bullet.st()

        self.speed = speed

    def xcor(self):
        return self.bullet.xcor()

    def ycor(self):
        return self.bullet.ycor()

    def heading(self):
        return self.bullet.heading()

    def move(self):
        self.bullet.forward(self.speed)
