import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
turtle.pencolor('blue')


def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius = radius-4


def drawdesign():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)


drawdesign()
turtle.done()
