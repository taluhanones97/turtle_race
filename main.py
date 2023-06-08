from turtle import Turtle, Screen
import random


screen=Screen()
screen.setup(width=500,height=400)

tim=Turtle(shape="turtle")
tim.penup()
tim.goto(x=-220,y=120)
tim.color("red")

tom=Turtle(shape="turtle")
tom.penup()
tom.goto(x=-220,y=80)
tom.color("blue")

timmy=Turtle(shape="turtle")
timmy.penup()
timmy.goto(x=-220,y=40)
timmy.color("green")

timmo=Turtle(shape="turtle")
timmo.penup()
timmo.goto(x=-220,y=-40)
timmo.color("yellow")

tims=Turtle(shape="turtle")
tims.penup()
tims.goto(x=-220,y=-80)
tims.color("black")

timk=Turtle(shape="turtle")
timk.penup()
timk.goto(x=-220,y=-120)
timk.color("orange")

user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)



while tim.xcor()<261 and tim.xcor()<261 and timmy.xcor()<261 and timmo.xcor()<261 and tims.xcor()<261 and timk.xcor()<261:
     tim.forward(random.randint(0,10))
     if tim.xcor()>=250:
         if tim.color()[0]==user_bet:
             print("You won")
             break
     tom.forward(random.randint(0, 10))
     if tom.xcor()>=250:
         if tom.color()[0]==user_bet:
             print("You won")
             break
     timmy.forward(random.randint(0, 10))
     if timmy.xcor()>=250:
         if timmy.color()[0]==user_bet:
             print("You won")
             break
     timmo.forward(random.randint(0, 10))
     if timmo.xcor()>=250:
         if timmo.color()[0]==user_bet:
             print("You won")
             break
     tims.forward(random.randint(0, 10))
     if tims.xcor()>=250:
         if tims.color()[0]==user_bet:
             print("You won")
             break
     timk.forward(random.randint(0, 10))
     if timk.xcor()>=250:
         if timk.color()[0]==user_bet:
             print("You won")
             break
print(timk.color())
"""
def move_forwards():
    tim.forward(100)
def move_backwards():
    tim.back(100)
def counter_clockwise():
    tim.left(180)
def clockwise():
    tim.right(180)

def line():
    tim.right(60)
    tim.forward(150)
def circle():
    tim.circle(25)

def clear():

    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="l",fun=line)
screen.onkey(key="c",fun=circle)
screen.onkey(key="x",fun=clear)
screen.exitonclick()"""
screen.exitonclick()