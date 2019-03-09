from turtle import *
from random import *


# MIT LICENSE
# Copyright (c) 2016 Jeffrey Wong (contact@jeffreywong.ca)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


print("I am an awesome artist")

print("How many clouds do you want me to draw?")
numClouds = int(input())

print("How many fish do you want me to draw?")
numFish = int(input())

print("How many jellyfish do you want?")
numJellyfish = int(input())

# set the modes
setup(800,700)
speed(0)
colormode(255)
pensize(5)
penup()
bgcolor("#7FFFD4")

# draw clouds
pencolor("white")
fillcolor("white")
for i in range(numClouds):
    cloudX = randint(-400,400)
    cloudY = randint(150,250)
    goto(cloudX,cloudY)
    begin_fill()
    setheading(180)
    for k in range(11):
        forward(5)
        right(18)
    for j in range(2):
        setheading(90)
        for k in range(11):
            forward(5)
            right(18)
    setheading(0)
    for k in range(11):
        forward(5)
        right(18)
    
    end_fill() 

# draw the boat's sail
setheading(0)
goto(-75,200) # bottom of sail
pendown()
pencolor("black")
fillcolor("#00FF00")
begin_fill()
for i in range(3):
    forward(150)
    left(120)
end_fill()
# draw the boat pole
penup()
goto(0,200)
setheading(270)
pendown()
forward(50)

# draw the boat body
penup()
goto(-100,150)
setheading(0)
pendown()
begin_fill()
forward(200)
right(135)
forward(25)
right(45)
forward(165)
right(45)
forward(25)
end_fill()

# draw the waves and water
penup()
goto(-400,135)
pencolor("#0000FF")
fillcolor("#0000FF")
pendown()
begin_fill()
for i in range(13):
    setheading(270)
    for j in range(11):
        forward(10)
        left(18)
setheading(270)
forward(500)
right(90)
forward(900)
goto(-400,135)
end_fill()

# draw the fish
for i in range(numFish):
    penup()
    # set random location
    goto(randint(-350,350),randint(-150,0))
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    # set color
    pencolor(red, green, blue)
    fillcolor(red, green, blue)
    pendown()
    setheading(90)
    # fish body
    begin_fill()
    for j in range(36):
        forward(5)
        left(10)
    end_fill()    
    #fish tail

    begin_fill()
    setheading(45)
    for j in range(3):
        forward(20)
        right(120)
    end_fill()

# draw jelly fish
for i in range(numJellyfish):
    penup()
    x = randint(-350,350)
    y = randint(-150,0)
    goto(x,y)
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    # set color
    pencolor(red, green, blue)
    fillcolor(red, green, blue)
    pendown()

    # draw body
    begin_fill()
    setheading(90)
    for j in range(11):
        forward(10)
        right(18)
    end_fill()
    penup()
    # draw tentacles
    for j in range(3):
        goto(x,y)
        setheading(270)
        pendown()
        for k in range(5):
            forward(5)
            right(20)
            forward(5)
            left(40)
        penup()
        x = x + 30
    
print("Press enter to close")
input()
