from turtle import *


def position(width, height):
    penup()
    goto(-width / 2, height / 2)
    pendown()

def Circle(radius):
    penup()
    goto(0, -radius)
    pendown()
    circle(radius, extent=None, steps=None)
    Screen().mainloop()

def Rectangle(width, height):
    penup()
    goto(-width / 2, height / 2)
    pendown()
    for i in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    Screen().mainloop()


def rectMaze(width, height):
    position(width, height)
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    tempWidth = width
    tempHeight = height
    widthSubtractor = int(width / 10)
    heightSubtractor = int(height / 10)
    for j in range(10):
        # penup()
        # goto(((j+1)/10)*(-width/2),((j+1)/10)*(height/2))
        # pendown()
        tempWidth -= widthSubtractor
        tempHeight -= heightSubtractor
        forward(tempWidth)
        right(90)
        forward(tempHeight)
        right(90)
    Screen().mainloop()

def rectMazeLeft(width, height):
    speed(10)
    left(180)
    i = 0
    j = 0
    while i < width and j < height:
        i += 10
        j += 10
        forward(i)
        left(90)
        forward(j)
        left(90)
    forward(width)
    Screen().mainloop()


if __name__ == "__main__":
    print("What shape do you want to make?")
    number = int(input("1. Circle    2. Rectangle    3. Rectangular Maze    4. Rectangular maze from the center:   "))
    width = 0
    height = 0
    radius = 0
    if number == 1:
        radius = int(input("Input Radius: "))
        Circle(radius)
    elif number == 2:
        width = int(input("Input Width: "))
        height = int(input("Input Height: "))
        Rectangle(width, height)
    elif number == 3:
        width = int(input("Input Width: "))
        height = int(input("Input Height: "))
        rectMaze(width, height)
    elif number == 4:
        width = int(input("Input Width: "))
        height = int(input("Input Height: "))
        rectMazeLeft(width, height)
