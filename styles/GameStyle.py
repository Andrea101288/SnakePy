import turtle
import time
import random

class GameStyle:

    width=600
    height=600

    delay = 0.1
    # screen Creation 
    wn = turtle.Screen()
    # screen Title
    wn.title("Revisited Snake Game by Andrea Mancini ")
    # add background Color
    wn.bgcolor("green")
    # add background Image
    wn.bgpic(r"./pictures/background.gif")
    # Game field dimenntions setup
    wn.setup(width, height)
    # Turns turtle animation on/off and set delay for update drawings.
    wn.tracer(0)


    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"


    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)


    mypen = turtle.Turtle()
    mypen.color("white")

    segments = []    

    eating_sound = r"./sounds/pureskelu.mp3"
 
    score = 0

    game_over = False