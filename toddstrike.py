import turtle
from plane import *

# Constants
SPEED = 2
ROTATE_SPEED = 2
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def move_planes(planes):
    for plane in planes:
        plane.fly_forward()


def in_range(x1, y1, x2, y2):
    '''
    returns whether or not (x1, y1) is within 5 units of (x2, y2)
    '''
    return abs(x1 - x2) < 5 and abs(y1 - y2) < 5

def is_plane_hit(plane, bullets):
    '''
    Checks if the given plane has been hit by (is within range of) any of the given
    bullets
    '''
    for bullet in bullets:
        if in_range(bullet.xcor(), bullet.ycor(), plane.xcor(), plane.ycor()):
            return True
    return False

def game_over(planes):
    '''
    Returns true if any plane has been hit by a bullet or is off-screen,
    false otherwise
    '''
    p1 = planes[0]
    p2 = planes[1]

    return (is_plane_hit(p2, p1.get_bullets()) or is_plane_hit(p1, p2.get_bullets())
        or is_off_screen(p1) or is_off_screen(p2))


def is_off_screen(turtle):
    '''
    Returns true if the given turtle is off the screen
    '''
    tx = turtle.xcor()
    ty = turtle.ycor()

    return (tx > SCREEN_WIDTH / 2  or tx < -SCREEN_WIDTH / 2
        or ty > SCREEN_HEIGHT / 2 or ty < -SCREEN_HEIGHT / 2)

def move_bullets(planes):
    '''
    Advances all bullets forward, and removes those that have flown off-screen
    '''
    for plane in planes:
        for i, bullet in reversed(list(enumerate(plane.get_bullets()))):
            if is_off_screen(bullet):
                plane.get_bullets().pop(i)
            else:
                bullet.move()

def setup_screen():
    '''
    Sets up the game window using the SCREEN_WIDTH and SCREEN_HEIGHT variable
    '''
    wn = turtle.Screen()
    wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=None, starty=None)
    # Remove re-render delay
    turtle.delay(0)
    return wn

def update_screen(planes):
    move_bullets(planes)
    move_planes(planes)

def bind_keys(screen, p1, p2, bullets):
    # Player 1 keys
    screen.onkey(lambda: p1.rotate_right(), 'Right')
    screen.onkey(lambda: p1.rotate_left(), 'Left')
    screen.onkey(lambda: p1.go_straight(), 'Up')
    screen.onkey(lambda: p1.shoot_bullet(), 'm')
    # Player 2 keys
    screen.onkey(lambda: p2.rotate_right(), 'd')
    screen.onkey(lambda: p2.rotate_left(), 'a')
    screen.onkey(lambda: p2.go_straight(), 'w')
    screen.onkey(lambda: p2.shoot_bullet(), 's')

def main():
    # Create game screen
    wn = setup_screen()
    # Setup model
    # id, x, y, heading, speed, turn_speed
    p1 = Plane(1, 0, 0, 0, 1, 2)
    p2 = Plane(2, 0, 0, 180, 1, 2)
    planes = [p1, p2]
    bullets = []

    bind_keys(wn, p1, p2, bullets)
    wn.listen()

    while not game_over(planes):
        # Wait to update view until all turtle updates have finished
        turtle.tracer(0,0)
        update_screen(planes)
        # Now update view
        turtle.update()
    print("Game over!")
    wn.mainloop()

main()
