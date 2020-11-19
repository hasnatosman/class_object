import turtle

turtle.speed(15)


def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)


counter = 0
while counter < 72:
    turtle.color("#f00ed9")
    draw_square(25)
    turtle.right(5)
    counter += 1


counter = 0
while counter < 72:
    turtle.color("#d422c2")
    draw_square(50)
    turtle.right(5)
    counter += 1


counter = 0
while counter < 72:
    turtle.color("#b02aa2")
    draw_square(75)
    turtle.right(5)
    counter += 1


counter = 0
while counter < 72:
    turtle.color("#9c3691")
    draw_square(100)
    turtle.right(5)
    counter += 1


# def draw_circle():
#     turtle.color("green")
#     turtle.circle(100)
#     turtle.left(90)
#
#
# counter = 0
# while counter < 34:
#     draw_circle()
#     turtle.right(5)
#     counter += 1

turtle.exitonclick()
turtle.hideturtle()
