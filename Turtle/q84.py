# making star using turtle
import turtle
scr= turtle.Screen()
scr.title("Star")
scr.bgcolor("Pink")
t= turtle.Turtle()
t.color("red")
t.speed(3)

for i in range(5):
    t.forward(80)
    t.right(144)

t.penup()
t.goto(100,100)
t.pendown()

for i in range(10):
    t.circle(22)
    t.left(45)

t.penup()
t.goto(-150,-150)
t.pendown()

def circle(r=20):
    for i in range(1):
        t.circle(r)
        t.circle(-r)
        # r= r+5

circle(20)
# circle(30)
# circle(40)


turtle.exitonclick()