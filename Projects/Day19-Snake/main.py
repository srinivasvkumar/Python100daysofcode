from turtle import Screen, Turtle
import time

screen=Screen()

screen.bgcolor("black")
screen.title("My snake game")
screen.screensize(680,500)
screen.tracer(0)

starting_positions=[(0,0),(-20,0),(-40,0)]

segments=[]

for position in starting_positions:
    new_segment=Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)




game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()


    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num - 1].xcor()
        new_y=segments[seg_num - 0].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)




screen.exitonclick()