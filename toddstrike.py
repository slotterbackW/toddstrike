import turtle

SPEED = 2
ROTATE_SPEED = 2
BULLET_SPEED = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

p1_right = False
p1_left = False

p2_right = False
p2_left = False

def p1_rotate_right():
    global p1_left
    global p1_right
    p1_right = True
    p1_left = False

def p1_rotate_left():
    global p1_left
    global p1_right
    p1_left = True
    p1_right = False

def p1_reset():
    global p1_left
    global p1_right
    p1_left = False
    p1_right = False

def p2_rotate_right():
    global p2_left
    global p2_right
    p2_right = True
    p2_left = False

def p2_rotate_left():
    global p2_left
    global p2_right
    p2_left = True
    p2_right = False

def p2_reset():
    global p2_left
    global p2_right
    p2_left = False
    p2_right = False

def move_forward(players):
    if p1_left == True:
        players[0].left(ROTATE_SPEED)
    if p1_right == True:
        players[0].right(ROTATE_SPEED)

    if p2_left == True:
        players[1].left(ROTATE_SPEED)
    if p2_right == True:
        players[1].right(ROTATE_SPEED)

    for player in players:
        player.forward(SPEED)

def isHit(player, bullet):
    px = player.xcor()
    py = player.ycor()
    bx = bullet.xcor()
    by = bullet.ycor()
    if abs(px - bx) < 5 and abs(py - by) < 5:
        return True
    else:
        return False


def bullets_hit(players, bullets):
    for bullet in bullets:
        if isHit(players[0], bullet) or isHit(players[1], bullet):
            return True
    return False


def move_bullets(bullets):
    for i, bullet in reversed(list(enumerate(bullets))):
        # if bullets are off screen, delete them
        if (bullet.xcor() > SCREEN_WIDTH / 2  or bullet.xcor() < -SCREEN_WIDTH / 2
            or bullet.ycor() > SCREEN_HEIGHT / 2 or bullet.ycor() < -SCREEN_HEIGHT / 2):
            bullets.pop(i)
        # otherwise move bullet
        else:
            bullet.forward(BULLET_SPEED)

def shoot_bullet(player, bullets):
    bullet = turtle.Turtle()
    bullet.ht()
    bullet.penup()
    bullet.setpos(player.xcor(), player.ycor())
    bullet.setheading(player.heading())
    bullet.forward(10)
    bullet.pendown()
    bullet.st()
    bullets.append(bullet)

def bind_keys(screen, p1, p2, bullets):
    # Player 1
    screen.onkey(lambda: p1_rotate_right(), 'Right')
    screen.onkey(lambda: p1_rotate_left(), 'Left')
    screen.onkey(lambda: p1_reset(), 'Up')
    screen.onkey(lambda: shoot_bullet(p1, bullets), 'm')
    # Player 2
    screen.onkey(lambda: p2_rotate_right(), 'd')
    screen.onkey(lambda: p2_rotate_left(), 'a')
    screen.onkey(lambda: p2_reset(), 'w')
    screen.onkey(lambda: shoot_bullet(p2, bullets), 's')

def main():
    wn = turtle.Screen()
    wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=None, starty=None)
    p1 = turtle.Turtle()
    p2 = turtle.Turtle()
    turtle.delay(0)
    players = [p1, p2]
    bullets = []
    bind_keys(wn, p1, p2, bullets)
    wn.listen()
    while not bullets_hit(players, bullets):
        turtle.tracer(0,0)
        move_forward(players)
        move_bullets(bullets)
        turtle.update()
    print("Game over!")
    wn.mainloop()

main()
