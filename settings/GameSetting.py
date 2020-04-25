import turtle
import time
import random
from styles.GameStyle import GameStyle as style

class GameSetting:

    gameStyle = style()   

    # Move funcions
    def go_up(self):
        self.gameStyle.head.direction = "up"

    def go_down(self):
        self.gameStyle.head.direction = "down"

    def go_left(self):
        self.gameStyle.head.direction = "left"

    def go_right(self):
        self.gameStyle.head.direction = "right"

    def move(self):

         # get head coordinates and increase it of 20 pxls
        if self.gameStyle.head.direction == "up":
           
            y = self.gameStyle.head.ycor()
            self.gameStyle.head.sety(y + 20)
            
        if self.gameStyle.head.direction == "down":          
            y = self.gameStyle.head.ycor()          
            self.gameStyle.head.sety(y - 20)

        if self.gameStyle.head.direction == "left":
         
            x = self.gameStyle.head.xcor()
           
            self.gameStyle.head.setx(x + 20)

        if self.gameStyle.head.direction == "right":          
            x = self.gameStyle.head.xcor()          
            self.gameStyle.head.setx(x - 20)