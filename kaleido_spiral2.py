import turtle

from itertools import cycle
colors = cycle(['orange', 'pink', 'green', 'yellow', 'purple', 'blue'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+8, angle+1,shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(20)
draw_circle(30,0,1)


