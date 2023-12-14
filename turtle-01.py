import turtle

t = turtle.Turtle()
t.shape('turtle')

t.pencolor('red')

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(50, 60)
t.pendown()

t.circle(70)



