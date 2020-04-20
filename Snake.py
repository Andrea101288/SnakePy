import os
import platform
import turtle
import time
import random
import playsound
import easygui
from settings.GameSetting import GameSetting as settings
from styles.GameStyle import GameStyle as style

Game = settings()
styles = style()

# Keyboard bindings
styles.wn.listen()
# if press w call go_up funcion
styles.wn.onkeypress(Game.go_up, "w")
# if press s call go_down funcion
styles.wn.onkeypress(Game.go_down, "s")
# if press d call go_left funcion
styles.wn.onkeypress(Game.go_left, "d")
# if press a call go_right funcion
styles.wn.onkeypress(Game.go_right, "a")

def play():

    # TurtleScreen update
    styles.wn.update()

    #check for a collision with the food, so if collides move the food to other random coordinates
    if styles.head.distance(styles.food) < 20:
        if platform.system() == 'Windows':
           playsound.playsound(styles.eating_sound, 0)
        else:
            os.system("afplay "+styles.eating_sound+"&")
        
        styles.score += 1
        print(styles.score)
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        styles.food.goto(x, y)

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
        styles.segments.append(new_segment)    

    # Move the end Segment in first in reverse order
    for index in range(len(styles.segments)-1, 0, -1):        
        x = styles.segments[index - 1].xcor()
        y = styles.segments[index - 1].ycor()
        styles.segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(styles.segments) > 0:
        # get head x, y
        x = styles.head.xcor()
        y = styles.head.ycor()
        # move segment 0 in head
        styles.segments[0].goto(x,y)

    # get position 
    w, h = styles.head.position()

    # check if the snake is going out of the screen
    # if went out to the right side, let it appear to the left one
    if not -styles.width / 2 < w:
        styles.head.goto(w+styles.width, h)
     # if went out to the left side, let it appear to the right one    
    elif not w < styles.width / 2:
        styles.head.goto(w-styles.width, h)
    # if went out to the top side, let it appear to the bottom
    elif not -styles.height / 2 < h:
        styles.head.goto(w,h+styles.height)
     # if went out to the bottom, let it appear to the upper side
    elif not h < styles.height / 2:
        styles.head.goto(w,h-styles.height)


    # for segment in styles.segments:
    #     if styles.head.distance(segment) < 20: 
    #         yn = easygui.ynbox('game over!', 'Try again?', ('yes', 'no'))
    #         if yn == 'yes':
    #             gameOver = False
    #             break
    #         else:
    #             quit()

    # Calling move funcion
    Game.move()
    time.sleep(styles.delay)   

# Main game loop
if __name__ == "__main__":

    while styles.game_over is False:
        play()
        
    styles.wn.mainloop()