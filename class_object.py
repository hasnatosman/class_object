import turtle

tom = turtle.Turtle()
tom.speed(50)


def draw_circle():
    tom.left(90)


counter = 0
while counter < 72:
    tom.color("red")
    tom.circle(140)
    draw_circle()
    tom.right(5)
    counter += 1

counter = 0
while counter < 72:
    tom.color("black")
    tom.circle(120)
    draw_circle()
    tom.right(5)
    counter += 1

counter = 0
while counter < 72:
    tom.color("yellow")
    tom.circle(100)
    draw_circle()
    tom.right(5)
    counter += 1

counter = 0
while counter < 72:
    tom.color("green")
    tom.circle(80)
    draw_circle()
    tom.right(5)
    counter += 1

counter = 0
while counter < 72:
    tom.color("indigo")
    tom.circle(60)
    draw_circle()
    tom.right(5)
    counter += 1
counter = 0
while counter < 72:
    tom.color("blue")
    tom.circle(40)
    draw_circle()
    tom.right(5)
    counter += 1
counter = 0
while counter < 72:
    tom.color("violet")
    tom.circle(20)
    draw_circle()
    tom.right(5)
    counter += 1

turtle.exitonclick()
turtle.hideturtle()
