import turtle as t

bob = t.Turtle()
t.bgcolor('black')

bob.pencolor('yellow')

# ---------------------------
def polygon(horn, length):
    angle = 360 / horn
    for i in range(horn):
        bob.fd(length)
        bob.left(angle)
# ---------------------------

horn = 10
length = 120

polygon(horn, length)

t.exitonclick()
