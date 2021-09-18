import turtle

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.goto(50,50)
    turtle.home()
    turtle.circle(25)
    turtle.circle(25)

def main_turtle():
    test_drive()
    input("Press any key to see status of turtle.....")

def turtle_state():
    a=turtle.isdown()
    b=turtle.heading()
    c=turtle.xcor(),turtle.ycor()
    print("Turtle Position:",a, "Turtle Orientation:",b, "Turtle Coordinates:",c)

main_turtle()
turtle_state()
