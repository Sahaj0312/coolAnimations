from turtle import *
import turtle

bg = turtle.Screen()
bg.bgcolor("black")

speed(0)
color("white")

left(90)


def tree(size, levels, angle):
	if levels == 0:
		return 

	forward(size)
	right(angle)

	tree(size * 0.8, levels - 1, angle)

	left(angle * 2)

	tree(size * 0.8, levels - 1, angle)

	right(angle)
	backward(size)



    
color("red")
tree(70,7,30)
right(90)
color("green")
tree(70,7,30)
right(90)
color("yellow")
tree(70,7,30)
right(90)
color("blue")
tree(70,7,30)
right(90)



mainloop()