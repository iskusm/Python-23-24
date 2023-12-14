from turtle import *

screen = Screen()
t = Turtle()

screen.setup(620, 620)
screen.bgcolor('black')

colors = ["red", "green", "blue", "yellow", "purple"]

t.pensize(4)
t.shape('turtle')
t.penup()
t.pencolor('red')

m = 0

for i in range(12):
    m += 1
    t.penup()
    t.setheading(-30*i + 60)
    t.fd(150)
    t.pendown()
    t.fd(25)
    t.penup()
    t.fd(20)
    t.write(str(m), align='center', font=('Arial',12,'normal'))
    if m == 12: m = 0
    t.home()

t.home()
t.setpos(0, -250)
t.pendown()
t.pensize(10)
t.pencolor('blue')
t.circle(250)
t.penup()
t.setpos(150, -270)
t.pendown()
t.pencolor('olive')
t.write('Turtle', font=('Arial',12,'normal'))
t.ht()
exitonclick()
