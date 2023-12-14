import turtle

t = turtle.Turtle('turtle')
t.speed(0)

for i in range(40):
    t.circle(120)
    t.left(70)

turtle.exitonclick()
