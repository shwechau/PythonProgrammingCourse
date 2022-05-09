import turtle
import print_me_first_gui
import Turtle_USA_Flag_sample

screen = turtle.getscreen()
screen.bgcolor("white")
turtle.goto(0,0)
turtle.bgpic("usa.png")
def draw_olympic_rings(x, y, color):
    turtle.speed(50)
    radius = 65
    width = 7
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pensize(width)
    turtle.pencolor(color)
    turtle.circle(radius)

def write_info():
    turtle.penup()
    width = 100
    turtle.pensize(width)
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.pencolor("blue")
    style = ('Ariel', 70, 'bold')
    turtle.write("USA\n", font= style, align='center')
    turtle.write("OLYMPIC TEAM", font= style, align='center')
    #turtle.write("OLYMPIC TEAM", font=style, align='center')
    turtle.hideturtle()

def write_name():
    width = 10
    turtle.penup()
    turtle.pensize()
    turtle.goto(300,-300)
    turtle.pendown()
    style = ('Ariel', 10, 'normal')
    infoDict = print_me_first_gui.print_me_time()
    turtle.write(infoDict[0], font = style)
    turtle.penup()
    turtle.goto(300, -315)
    turtle.pendown()
    turtle.write(infoDict[1], font = style)
    turtle.penup()
    turtle.goto(300, -330)
    turtle.pendown()
    turtle.write(infoDict[2], font = style)
    turtle.hideturtle()

Turtle_USA_Flag_sample.draw_US_flag()
draw_olympic_rings(-160,-300, "blue")
draw_olympic_rings(-80,-360, "orange")
draw_olympic_rings(0,-300, "black")
draw_olympic_rings(80,-360, "green")
draw_olympic_rings(160,-300, "red")
write_info()
print_me_first_gui.print_me_time()
screen.mainloop()
