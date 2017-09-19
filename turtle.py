import turtle

def draw_square(turtle):
    for i in range(4):
        turtle.forward(75)
        turtle.right(90)

def draw_circle(turtle):
    turtle.circle(100)

def draw_triangle(turtle):
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    #Draws a square
    square = turtle.Turtle()
    square.color("white")
    square.speed(25)
    for i in range(36):
        draw_square(square)
        square.right(10)

    #Draws a circle
    #circle = turtle.Turtle()
    #circle.shape("circle")
    #circle.color("yellow")
    #circle.speed(2)
    #draw_circle(circle)

    #Draws a triangle
    #triangle = turtle.Turtle()
    #triangle.shape("turtle")
    #triangle.color("orange")
    #triangle.speed(2)
    #draw_triangle(triangle)

    window.exitonclick()

draw_art()
