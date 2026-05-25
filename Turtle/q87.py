import turtle
scr= turtle.Screen()
scr.title("Olympics Symbol")
 
t= turtle.Turtle()
t.color("Blue")
t.circle(50)

t.penup()
t.setposition(-120,0)
t.pendown()
t.color("red")
t.circle(50)

t.penup()
t.setposition(60,60)
t.pendown()

t.color("Black")
t.circle(50)

t.penup()
t.setposition(-60,60)
t.pendown()

t.color("Yellow")
t.circle(50)

t.penup()
t.setposition(-180,60)
t.pendown()

t.color("Pink")
t.circle(50)



turtle.exitonclick()