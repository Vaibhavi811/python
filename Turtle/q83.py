import turtle
scr= turtle.Screen()
scr.title("HELLO")
scr.bgcolor("Pink")
t= turtle.Turtle()

def square(l=100):
    for i in range(4):
        t.forward(l)
        t.right(90)
        l= l+5


square(10)
square(30)
square(50)
turtle.done()