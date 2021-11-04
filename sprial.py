import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

while True:
    for colours in ["red","magenta","blue","cyan","green","yellow","white"] :
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()