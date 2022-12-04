from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
# ask the screen object to start listening to an event
screen.listen()

def move_forwards():
    tim.forward(20)
    print(tim.position())
def move_backwards():
    tim.backward(20)
    print(tim.position())
# Challenge 0: bind a funtion (to trigger) to a key stroke (for our purpose)
# for example, set focus on the onkey function and bind it to a key turtle.onkey(fun, key)
screen.onkey(fun=move_backwards, key='Left')
screen.onkey(fun=move_forwards, key='Right')

# Challenge 2: Write code to make the turtle move forwards for'w', backwards for key 's',

def move_circ_clock():
    r = -30 # draws clockwise if radius is negative. anticlockwise if radius is positive
    e = 90 # extent. 90 = draw quarter circle. 180 = semicircle etc
    s = 10 # = 10 steps
    tim.circle(r, e , s)
    print(tim.position())


def move_circ_anticlock():
    r = 30 # draws clockwise if radius is negative. anticlockwise if radius is positive
    e = 90 # extent. 90 = draw quarter circle. 180 = semicircle etc
    s = 10 # = 10 steps
    tim.circle(r, e , s)
    print(tim.position())

def go_home():
    tim.penup()
    tim.goto(0, 0)
    print(tim.position())
    tim.pendown()
#  counter-clockwise for 'a', and clockwise for 'd'
tim.left(45 )
screen.onkey(fun=move_forwards, key='w')
screen.onkey(key='s', fun=move_backwards)
screen.onkey(fun=move_circ_clock, key='a')
screen.onkey(fun=move_circ_anticlock, key='d')
screen.onkey(key='Escape', fun=screen.bye)
screen.onkey(key='c', fun=screen.clear)
screen.onkey(key='Home', fun=go_home)






screen.exitonclick()
