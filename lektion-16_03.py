import turtle

def polygon(horn, lengd):
    for h in range(horn):
        turtle.fd(lengd)
        turtle.lt(int(360/horn))

def flytta_till(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.pensize(3)

flytta_till(-50, -230)

polygon(30, 50)
turtle.home()

turtle.exitonclick()
