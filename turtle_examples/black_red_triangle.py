# "A black and red triangle"
import turtle
turtle.pen(fillcolor="black", pencolor="red", pensize=10)
turtle.fill(True)
for _ in range(3):
  turtle.forward(100)
  turtle.left(120)
turtle.fill(False)
