import turtle
import time
import random
import easygui
from styles.GameStyle import GameStyle as style

class GameSetting:

    gameStyle = style()   

    # Move funcions
    def go_up(self):
        # set the direction to up
        self.gameStyle.head.direction = "up"

    def go_down(self):
        # set the direction to down
        self.gameStyle.head.direction = "down"

    def go_left(self):
        # set the direction to left
        self.gameStyle.head.direction = "left"

    def go_right(self):
        # set the direction to right
        self.gameStyle.head.direction = "right"

    def move(self):

        if self.gameStyle.head.direction == "up":
            # get head y coordinate
            y = self.gameStyle.head.ycor()
            # increase head y coordinates of 20 pxls
            self.gameStyle.head.sety(y + 20)
            
        if self.gameStyle.head.direction == "down":
            # get head y coordinate
            y = self.gameStyle.head.ycor()
            # decrease head y coordinates of 20 pxls
            self.gameStyle.head.sety(y - 20)

        if self.gameStyle.head.direction == "left":
            # get head x coordinate
            x = self.gameStyle.head.xcor()
            # increase head x coordinates of 20 pxls
            self.gameStyle.head.setx(x + 20)

        if self.gameStyle.head.direction == "right":
            # get head x coordinate
            x = self.gameStyle.head.xcor()
            # decrease head x coordinates of 20 pxls
            self.gameStyle.head.setx(x - 20)