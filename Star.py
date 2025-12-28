import turtle
turtle.Screen().bgcolor("darkblue")
board= turtle.Turtle()
board.pencolor("yellow")
# Upper triangle of Star
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# Lower triangle of Star
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()