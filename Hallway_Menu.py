from pygame import *
from Button import *

class menu:
    def __init__(self):
        self.screen = display.get_surface()
        self.b1 = button((375,150), 250, 50, (120,120,120), "Resume", (0,0,0), 24)
        self.b2 = button((375,300), 250, 50, (120,120,120), "Logout", (0,0,0), 24)
        self.b3 = button((375,450), 250, 50, (120,120,120), "Quit", (0,0,0), 24)
    def draw(self):
        if  self.b1.update() == True:
            return 1
        elif  self.b2.update() == True:
            return 2
        elif  self.b3.update() == True:
            return 3
        