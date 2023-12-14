import turtle
import random

turtle.speed(0)

def star():
    for i in range(5):
        turtle.fd(50)
        turtle.left(72)

turtle.bgcolor("black")
turtle.pencolor("yellow")

for i in range(20):
    turtle.penup()
    turtle.goto(random.randint(-200, 200),
                random.randint(-200, 200))
    turtle.pendown()
    star()
    
turtle.exitonclick()
