from pygame import *
from text import *
from Game3_Game import *

class Maze:
    def __init__(self):
        self.screen = display.get_surface()
        self.text = Text()
        self.AmMaze = AmMaze()
        self.scrn = 1
        
    def run(self):
        if self.scrn == 1:
            self.screen.fill((60,60,60))
            self.text.txt("AmMaze", 32, (255,255,255), (500,250))
            self.text.txt("Press Enter Start", 32, (255,255,255), (500,350))
            
            k = key.get_pressed()
            
            if k[K_RETURN]:
                self.scrn = 2
                
        elif self.scrn == 2:
            if self.AmMaze.run() == True:
                self.text = Text()
                self.AmMaze = AmMaze()
                self.scrn = 1
                return True
