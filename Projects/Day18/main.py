from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")


def turle_move():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


for _ in range(4):
    turle_move()

screen = Screen()
screen.exitonclick()
