import turtle
import time
import random
import easygui

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

    # Snake Head creation
    head = turtle.Turtle()
    # set head initial speed
    head.speed(0)
    # set head shape
    head.shape("square")
    # set head color
    head.color("black")
    # Sets the current pen state to penup, not drawing it
    head.penup()
    # initialize the head ih 0,0 coordinates
    head.goto(0,0)
    # Intialize the movement to stop
    head.direction = "stop"

    # Snake Food creation
    food = turtle.Turtle()
    # Initialize food speed to 0
    food.speed(0)
    # set food Shape
    food.shape("circle")
    # set food color
    food.color("red")
    # set the food to penUp, not drawing it
    food.penup()
    # set iniitial coordinates for food
    food.goto(0,100)

    # define segments array to add everytime we get food
    segments = []    

    #eating soundtrack
    eating_sound = r"./sounds/pureskelu.mp3"

    # set initial score 
    score = 0

    # variable gameOver initialized to False
    game_over = False