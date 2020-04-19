import turtle
import time
import random
import easygui

width=600
height=600

delay = 0.1
# screen Creation 
wn = turtle.Screen()
# screen Title
wn.title("Revisited Snake Game by Andrea Mancini ")
# add background Color
wn.bgcolor("green")
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

# variable gameOver initialized to False
gameOver = False

# Move funcions
def go_up():
    # set the direction to up
    head.direction = "up"

def go_down():
    # set the direction to down
    head.direction = "down"

def go_left():
    # set the direction to left
    head.direction = "left"

def go_right():
    # set the direction to right
    head.direction = "right"

def move():

    if head.direction == "up":
        # get head y coordinate
        y = head.ycor()
        # increase head y coordinates of 20 pxls
        head.sety(y + 20)

    if head.direction == "down":
        # get head y coordinate
        y = head.ycor()
        # decrease head y coordinates of 20 pxls
        head.sety(y - 20)

    if head.direction == "left":
        # get head x coordinate
        x = head.xcor()
        # increase head x coordinates of 20 pxls
        head.setx(x + 20)

    if head.direction == "right":
        # get head x coordinate
        x = head.xcor()
        # decrease head x coordinates of 20 pxls
        head.setx(x - 20)

# Keyboard bindings
wn.listen()
# if press w call go_up funcion
wn.onkeypress(go_up, "w")
# if press s call go_down funcion
wn.onkeypress(go_down, "s")
# if press d call go_left funcion
wn.onkeypress(go_left, "d")
# if press a call go_right funcion
wn.onkeypress(go_right, "a")

def play():
    # TurtleScreen update
    wn.update()

    #check for a collision with the food, so if collides move the food to other random coordinates
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment to the snake
        # segment creation
        new_segment = turtle.Turtle()
        # sei initial speed
        new_segment.speed(0)
        # set segment shape
        new_segment.shape("square")
        # set segment color
        new_segment.color("grey")
        # set initial penup method
        new_segment.penup()
        # add new segment to the snake 
        segments.append(new_segment)    

    # Move the end Segment in first in reverse order
    for index in range(len(segments)-1, 0, -1):        
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        # get head x, y
        x = head.xcor()
        y = head.ycor()
        # move segment 0 in head
        segments[0].goto(x,y)

    # get position 
    w, h = head.position()

    # check if the snake is going out of the screen
    # if went out to the right side, let it appear to the left one
    if not -width / 2 < w:
        head.goto(w+width, h)
     # if went out to the left side, let it appear to the right one    
    elif not w < width / 2:
        head.goto(w-width, h)
    # if went out to the top side, let it appear to the bottom
    elif not -height / 2 < h:
        head.goto(w,h+height)
     # if went out to the bottom, let it appear to the upper side
    elif not h < height / 2:
        head.goto(w,h-height)

    # for segment in segments:
    #     if head.distance(segment) < 20: 
    #         yn = easygui.ynbox('game over!', 'Try again?', ('yes', 'no'))
    #         if yn == 'yes':
    #             gameOver = False
    #             break
    #         else:
    #             quit()

    # Calling move funcion
    move()
    time.sleep(delay)   

# Main game loop
if __name__ == "__main__":

    while gameOver is False:
        play()
        
    wn.mainloop()