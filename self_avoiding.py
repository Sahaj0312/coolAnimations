# import package
from os import error
import turtle
import random

#global variables
directions = ["left", "right", "up", "down"]

state = "right" #The turtle by default faces right

xmovement = 0 #how much the turtle has moved on the x-axis
ymovement = 0 #how much the turtle has moved on the y-axis
yCoor = 0 #y-coordinate of turtle at any given point in the execution
xCoor = 0 #x-coordinate of turtle at any given point in the execution
moves = [] #list of moves(states)
revMoves = [] #list of moves in reverse for backtracking
visitedCoor = [(0,0)] #list of coordinated visited

#function to ensure that program does not run indefinetly and restrict movement of turtle
def isValid(xmovement,ymovement):
    return (xmovement <= 900 and ymovement <= 900 )

#function to setup turtle and background
def setup():
    bg = turtle.Screen()
    bg.bgcolor("yellow")
    bg.title("Self-Avoiding walk")
    # turtle.hideturtle()s
    turtle.speed(0)

#function that backtracks on the turtles path once it's stuck
def goBack():
    turtle.pencolor("yellow")
    turtle.pensize(3)
    revCoords = reversed(visitedCoor)
    for coord in revCoords:
        turtle.goto(coord)

            

#recursive solution
def main(xmovement,ymovement,xCoor,yCoor,state):
    try:
        print(f"X movement: {xmovement} and Y movement: {ymovement}")
        direction = random.choice(directions)
        print(direction)

        if (isValid(xmovement,ymovement)):
            if (direction == "up" and ((xCoor,yCoor+10) not in visitedCoor)):
                if (state == "up"):
                    turtle.forward(10)
                elif (state == "down"):
                    turtle.left(180)
                    turtle.forward(10)
                elif (state == "right"):
                    turtle.left(90)
                    turtle.forward(10)
                elif (state == "left"):
                    turtle.right(90)
                    turtle.forward(10)
                state = "up"
                ymovement += 10
                yCoor += 10
                visitedCoor.append((xCoor,yCoor))
                moves.append(state)
                main(xmovement,ymovement,xCoor,yCoor,state)
            elif (direction == "down" and ((xCoor,yCoor-10) not in visitedCoor)):
                if (state == "down"):
                    turtle.forward(10)
                elif (state == "up"):
                    turtle.left(180)
                    turtle.forward(10)
                elif (state == "right"):
                    turtle.right(90)
                    turtle.forward(10)
                elif (state == "left"):
                    turtle.left(90)
                    turtle.forward(10)
                state = "down"
                ymovement += 10
                yCoor -= 10
                visitedCoor.append((xCoor,yCoor))
                moves.append(state)
                main(xmovement,ymovement,xCoor,yCoor,state)
            elif (direction == "left" and ((xCoor-10,yCoor) not in visitedCoor)):
                if (state == "left"):
                    turtle.forward(10)
                elif (state == "up"):
                    turtle.left(90)
                    turtle.forward(10)
                elif (state == "right"):
                    turtle.right(180)
                    turtle.forward(10)
                elif (state == "down"):
                    turtle.right(90)
                    turtle.forward(10)
                state = "left"
                xmovement += 10
                xCoor -= 10
                visitedCoor.append((xCoor,yCoor))
                moves.append(state)
                main(xmovement,ymovement,xCoor,yCoor,state)
            elif (direction == "right" and ((xCoor+10,yCoor) not in visitedCoor)):
                if (state == "right"):
                    turtle.forward(10)
                elif (state == "up"):
                    turtle.right(90)
                    turtle.forward(10)
                elif (state == "left"):
                    turtle.right(180)
                    turtle.forward(10)
                elif (state == "down"):
                    turtle.left(90)
                    turtle.forward(10)
                state = "right"
                xmovement += 10   
                xCoor += 10
                visitedCoor.append((xCoor,yCoor))
                moves.append(state)
                main(xmovement,ymovement,xCoor,yCoor,state)
            else:
                main(xmovement,ymovement,xCoor,yCoor,state)
        else:
            print("Out of movess")
    except RecursionError:
        print("stuck, gotta goBack")
        goBack()
        print(moves)
        #print(visitedCoor)
        

setup()
main(xmovement,ymovement,xCoor,yCoor,state)


print("DONE")

        
turtle.mainloop()