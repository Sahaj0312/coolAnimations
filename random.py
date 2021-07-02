from turtle import *
import turtle

bg = turtle.Screen()
bg.bgcolor("black")

speed(0)
color("white")
shape("turtle")

def coolAnimation(levels,inc,c):

    colors = ["black", "white"]

    if (levels == 0):
        return "done"

    forward(inc)
    right(55)
    circle(inc)
    forward(inc)
    circle(inc)
    left(90)
    forward(inc)
    circle(inc)
    color(colors[c])
    coolAnimation(levels-1,inc+0.5,levels % 2)

    
coolAnimation(200,5,0)

mainloop()



