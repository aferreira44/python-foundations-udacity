import turtle

def draw_square(shape, color, speed):
    square = turtle.Turtle()
    square.shape(shape)
    square.color(color)
    square.speed(speed)

    for i in range(4):
        square.forward(100)
        square.right(90)

def draw_circle(shape, color, speed):
    circle = turtle.Pen()
    circle.shape(shape)
    circle.color(color)
    circle.speed(speed)
    circle.circle(100)

def draw_triangle(shape, color, speed):
    triangle = turtle.Pen()
    triangle.shape(shape)
    triangle.color(color)
    triangle.speed(speed)

    for i in range(3):
        triangle.forward(100)
        triangle.left(120)

window = turtle.Screen()
window.bgcolor("black")

draw_square("square", "white", 2)

draw_circle("circle", "yellow", 2)

draw_triangle("turtle", "orange", 2)

window.exitonclick()
