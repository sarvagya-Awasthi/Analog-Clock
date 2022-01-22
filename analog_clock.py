#Simple analog clock
#turtle module helps us to create a GUI
import time
import turtle
screen=turtle.Screen()
screen.bgcolor("red")
screen.setup(width=800,height=800)
screen.title("Analog clock")
#initialise a pen to draw
pen=turtle.Turtle()
pen.color("black")
pen.speed(6)
pen.write("the time is",move=True,align='left',font=('Arial',14,'bold'))
pen.pensize(6)
def draw_clock(hrs,min,sec,pen): 
    #draw the clock structure
    pen.penup()
    pen.goto(0,210)
    pen.setheading(180)     #it takes angle as an argument to move the pen
    pen.color("white")
    pen.pendown()
    pen.circle(210)
    #draw the hands of the clock
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    for j in range(12):
        pen.forward(190)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.goto(0,0)
        pen.right(30)
    #Draw the hour hands
    pen.penup()
    pen.goto(0,0)
    pen.color("yellow")
    pen.setheading(90)
    angle=(hrs/12)*360
    pen.right(angle)
    pen.pendown()
    pen.forward(180)

    #Draw the minutes hands
    pen.penup()
    pen.goto(0,0)
    pen.color("lightblue")
    pen.setheading(90)
    angle=(min/60)*360
    pen.right(angle)
    pen.pendown()
    pen.forward(180)

    #Draw the seconds hand
    pen.penup()
    pen.goto(0,0)
    pen.color("green")
    pen.setheading(90)
    angle=(sec/60)*360
    pen.right(angle)
    pen.pendown()
    pen.forward(50)
while True:
    hrs=int(time.strftime("%H"))
    min=int(time.strftime("%M"))
    sec=int(time.strftime("%S"))

    draw_clock(hrs,min,sec,pen)
    screen.update()
    pen.clear()
    time.sleep(10)
screen.exitonclick()
screen.mainloop()