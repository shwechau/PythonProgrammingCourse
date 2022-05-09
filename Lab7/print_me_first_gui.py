import os.path
import sys
from datetime import datetime
import  turtle

def print_me_time():
    name = "Shweta Chauhan"
    program = os.path.basename((sys.argv[0]))
    currentTime = datetime.now()
    timestamp_str = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    turtle.pensize()
    position(300, -300)
    write("Name")
    position(380,-300)
    write(": " + name)
    position(300, -320)
    write("Program")
    position(380, -320)
    write(": " + program)
    position(300, -340)
    write("Time")
    position(380, -340)
    write(": " + timestamp_str)

def position(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def write(info):
    style = ('Ariel', 10, 'normal')
    turtle.write(info, font = style)





