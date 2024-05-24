import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLOURS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]


def init_tur():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing")


def no_racers():
    racers = 0
    while True:
        racers = input("Enter the no of racers from (2 to 10): ")
        if(racers.isdigit()):
            racers = int(racers)
            if(2 <= racers <= 10):
                return racers
            else:
                print("invalid... give a number from 2 to 10")
        else:
            print("invalid... give a number")


def create_tur(colour):
    turtles = [] 
    spacing = WIDTH // (len(colour) + 1)

    for i, colour in enumerate(colour):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()#no line till reaching start point
        racer.setpos((-WIDTH // 2) + (i + 1)*spacing, (-HEIGHT // 2) + 20)#by giving x,y we will set position
        racer.pendown()#lines ahould be after start pint reached
        turtles.append(racer)
    return turtles


def race(colour):
    turtles = create_tur(colour)

    while True:
        for turtle in turtles:
            dist = random.randrange(1,10)
            turtle.forward(dist)

            x, y = turtle.pos()
            if(y >= (HEIGHT//2) - 10):
                    return colour[turtles.index(turtle)] 


racers = no_racers()
init_tur()
random.shuffle(COLOURS)
colours = COLOURS[:racers]

winner = race(colours)
print(winner)






















# racer = turtle.Turtle() #assigning him the module
# racer.speed(1)
# racer.color("red")
# racer.shape("turtle")
# racer.forward(100)
# racer.left(90)
# racer.forward(100)
# racer.right(90)
# racer.backward(200)
# # time.sleep(20) it stops the turtle prompt for 20 sec


