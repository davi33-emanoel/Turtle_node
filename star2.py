from turtle import *

wn =Screen()
wn.bgcolor('black')
wn.title('star2')
wn.setup(width=1200, height=750)
t= Turtle()
t.speed(0)
t.color('lightgreen')
while True:
    for i in range(140):
        t.pensize(i/50)
        t.fd(i)
        t.rt(90)
        t.fd(i)
        t.rt(80)
        t.fd(i+100)
        t.circle(30,67)
        reset()