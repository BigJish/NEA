from pygame import *
from text import *

class game4:
    def __init__(self):
        self.screen = display.get_surface()
        self.text = Text()
        
    def run(self):
        self.screen.fill((60,60,60))
        self.text.txt("Game Isn't Made!", 32, (255,255,255), (500,250))
        self.text.txt("Press Enter To Go Away", 32, (255,255,255), (500,350))
        
        k = key.get_pressed()
        
        if k[K_RETURN]:
            return True