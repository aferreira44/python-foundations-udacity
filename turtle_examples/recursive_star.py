#"Recursive Star"
import turtle
def star(turtle, n,r):
 """ draw a star of n rays of length d"""
 for k in range(0,n):
    turtle.pendown()
    turtle.forward(r)
    turtle.penup()
    turtle.backward(r)
    turtle.left(360/n)
 
def recursive_star(turtle, n, r, depth, f):
 """At each point of the star, draw another smaller star,
 and so on, up to given depth. Rescale the stars by a factor f
 at each generation."""
 
 if depth == 0:
    star(turtle, n, f*4)
 else:
    for k in range(0,n):
        turtle.pendown()
        turtle.forward(r)
        recursive_star(turtle, n, f*r, depth - 1,f)
        turtle.penup()
        turtle.backward(r)
        turtle.left(360/n)
 
fred = turtle.Turtle()
fred.speed("fastest")
recursive_star(fred, 5 , 150, 4, 0.4)
 
import turtle
import random
fred = turtle.Turtle()
 
fred.speed(10)
 
colors=['lavender', 'pink', 'blue', 'midnight blue', 'lime']
 
def flower(x,y,r,g,b):
    fred.setposition(x,y)
    fred.pendown()
    fred.color('green')
    fred.setheading(270)
    fred.fd(200)
 
    fred.setposition(x,y)
 
    fred.color(random.choice(colors))
    for i in range(12):
        fred.circle(20)
        fred.left(30)
 
 
for i in range(100):
    fred.penup()
    flower(random.randint(-200,200), random.randint(-200,0),random.randint(0,255),
    random.randint(0,255),random.randint(0,255))
