from turtle import *

shape("turtle")
pencolor("blue")

def kvadrat():
    for i in range(4):
        forward(100)
        left(90)

kvadrat()

penup()
goto(-100, 100)
pendown()

kvadrat()
