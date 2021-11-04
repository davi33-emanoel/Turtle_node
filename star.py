import turtle
from turtle import *
wn = Screen()
wn.setup(1200, 680)
wn.bgcolor("black")
t = Turtle()
colors = ["white", "cyan"]

for i in range(150):
    t.pencolor(colors[i%len(colors)])
    t.fd(i)
    t.rt(120)
    t.fd(i)
    t.rt(180)
    t.fd(i)
    t.speed(0)
wn.mainloop()
