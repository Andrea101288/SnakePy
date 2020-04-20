import os
import platform
import turtle
import time
import random
import playsound
import easygui
from GameSetting import GameSetting as settings
from GameStyle import GameStyle as style

Game = settings()
GameStyle = style()

# Keyboard bindings
GameStyle.wn.listen()
# if press w call go_up funcion
GameStyle.wn.onkeypress(Game.go_up, "w")
# if press s call go_down funcion
GameStyle.wn.onkeypress(Game.go_down, "s")
# if press d call go_left funcion
GameStyle.wn.onkeypress(Game.go_left, "d")
# if press a call go_right funcion
GameStyle.wn.onkeypress(Game.go_right, "a")

def play():

    # TurtleScreen update
    GameStyle.wn.update()

    #check for a collision with the food, so if collides move the food to other random coordinates
    if GameStyle.head.distance(GameStyle.food) < 20:
        if platform.system() == 'Windows':
           playsound.playsound(GameStyle.eating_sound, 0)
        else:
            os.system("afplay "+GameStyle.eating_sound+"&")
        
        GameStyle.score += 1
        print(GameStyle.score)
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        GameStyle.food.goto(x, y)

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
        GameStyle.segments.append(new_segment)    

    # Move the end Segment in first in reverse order
    for index in range(len(GameStyle.segments)-1, 0, -1):        
        x = GameStyle.segments[index - 1].xcor()
        y = GameStyle.segments[index - 1].ycor()
        GameStyle.segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(GameStyle.segments) > 0:
        # get head x, y
        x = GameStyle.head.xcor()
        y = GameStyle.head.ycor()
        # move segment 0 in head
        GameStyle.segments[0].goto(x,y)

    # get position 
    w, h = GameStyle.head.position()

    # check if the snake is going out of the screen
    # if went out to the right side, let it appear to the left one
    if not -GameStyle.width / 2 < w:
        GameStyle.head.goto(w+GameStyle.width, h)
     # if went out to the left side, let it appear to the right one    
    elif not w < GameStyle.width / 2:
        GameStyle.head.goto(w-GameStyle.width, h)
    # if went out to the top side, let it appear to the bottom
    elif not -GameStyle.height / 2 < h:
        GameStyle.head.goto(w,h+GameStyle.height)
     # if went out to the bottom, let it appear to the upper side
    elif not h < GameStyle.height / 2:
        GameStyle.head.goto(w,h-GameStyle.height)


    # for segment in GameStyle.segments:
    #     if GameStyle.head.distance(segment) < 20: 
    #         yn = easygui.ynbox('game over!', 'Try again?', ('yes', 'no'))
    #         if yn == 'yes':
    #             gameOver = False
    #             break
    #         else:
    #             quit()

    # Calling move funcion
    Game.move()
    time.sleep(GameStyle.delay)   

# Main game loop
if __name__ == "__main__":

    while GameStyle.game_over is False:
        play()
        
    GameStyle.wn.mainloop()