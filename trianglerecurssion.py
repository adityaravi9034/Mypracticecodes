import turtle
MINIMUM_BRANCH = 5

def build_turtletree(t,length,decrease_by,angle):
 if length > MINIMUM_BRANCH:
  t.forward(length)
  new_length = length - decrease_by

  t.left(angle)
  build_turtletree(t,new_length,decrease_by,angle)

  t.right(angle *2 )
  build_turtletree(t,new_length,decrease_by,angle)

  t.left(angle)
  t.backward(length)

tree = turtle.Turtle()
turtle.hideturtle()
tree.setheading(15)
tree.color('orange')



build_turtletree(tree,50,8,15)
turtle.mainloop()

