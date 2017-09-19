import turtle

def striangle(depth,base):
   turtle.down()
   if depth == 0:
      turtle.fill(1)
      for i in 0,1,2:
         turtle.forward(base)
         turtle.left(120)
      turtle.fill(0)
   else:
      for i in 0,1,2:
         striangle(depth-1,base)
         turtle.up()
         turtle.forward(base*2**depth)
         turtle.left(120)
         turtle.down()

turtle.reset()
striangle(6,5)
