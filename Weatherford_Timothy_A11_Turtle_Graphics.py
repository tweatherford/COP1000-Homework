'''
Assignment #11 - Turtle Graphics
Programmed By: Timothy Weatherford
Added functions, plus makes the turtle do a Christmas spirited infinite loop.
'''
#imports the turtle library
import turtle;

#Setup the function
def setup():
    turtle.showturtle();

#Writes text on command
def writeText():
    turtle.write("Welcome to COP1000 ");
    turtle.color("purple")

#For rectangles
def longFwd():
    turtle.forward(100)

#For rectangles and squares
def shortFwd():
    turtle.forward(50)

def right():
    turtle.right(90)

def left():
    turtle.left(90)

#Makes the turtle do a rectangle pattern
def rectangle():
    longFwd()
    right()
    shortFwd()
    right()
    longFwd()
    right()
    shortFwd()

#Makes the spirited and infinite square pattern.
def square():
    left()
    shortFwd()
    right()
    turtle.color("red")
    shortFwd()
    right()
    shortFwd()
    turtle.color("green")
    right()
    shortFwd()
    square()
    
#Calls the setup, then writes text, and begins the turtle dance!
def turtleMovements():
    setup()
    writeText()
    rectangle()
    square()

#Sets the initial loop in motion
turtleMovements()

# End Program
