import turtle as t
from turtle import Screen


tim=t.Turtle()


for _ in range(20):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

screen = Screen()
screen.exitonclick()

