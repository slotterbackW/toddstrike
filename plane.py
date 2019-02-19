import turtle
from bullet import *

class Plane:
    '''
    A wrapper around the turtle class used to represent the planes in the game
    '''
    def __init__(self, id, x, y, heading, speed, turn_speed, color):
        self.id = id

        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.setposition(x, y)
        self.turtle.setheading(heading)
        self.turtle.color(color)
        self.turtle.st()

        self.speed = speed
        self.turn_speed = turn_speed
        self.turn_right = False
        self.turn_left = False

        self.bullets = []

    def xcor(self):
        return self.turtle.xcor()

    def ycor(self):
        return self.turtle.ycor()

    def heading(self):
        return self.turtle.heading()

    def rotate_left(self):
        self.turn_left = True
        self.turn_right = False

    def rotate_right(self):
        self.turn_right = True
        self.turn_left = False

    def go_straight(self):
        self.turn_left = False
        self.turn_right = False

    def fly_forward(self):
        if self.turn_left == True:
            self.turtle.left(self.turn_speed)
        if self.turn_right == True:
            self.turtle.right(self.turn_speed)

        self.turtle.forward(self.speed)

    def setheading(self, heading):
        self.turtle.setheading(heading)

    def shoot_bullet(self):
        bullet = Bullet(self.xcor(), self.ycor(), self.heading(), 10)
        self.bullets.append(bullet)

    def get_bullets(self):
        return self.bullets
