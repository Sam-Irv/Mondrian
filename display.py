from turtle import Turtle, Screen
import turtle
import yaml


def display_puzzle_yaml(yaml_path):
    with open(yaml_path) as f:
        puzzle = yaml.safe_load(f)

    screen = Screen()
    turtle.setup(700, 700)
    screen.setworldcoordinates(0, 0, 6, 6)
    me = Turtle(visible=False)
    me.speed("fastest")
    me.hideturtle()

    def filled_rectangle(t, x, y, width, height, colour):
        t.penup()
        t.fillcolor(colour)
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.setheading(90)
        for _ in range(2):
            t.forward(height)
            t.right(90)
            t.forward(width)
            t.right(90)
        t.end_fill()
        t.penup()

    filled_rectangle(me, 1, 1, **puzzle["board"])

    filled_rectangle(me, **puzzle["pieces"][0])
    for piece in puzzle["pieces"]:
        filled_rectangle(me, **piece)

    screen.exitonclick()


if __name__ == "__main__":
    display_puzzle_yaml("puzzle_setup.yaml")
