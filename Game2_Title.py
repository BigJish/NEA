from settings import *

class Title:
    def __init__(self):
        self.win = display.get_surface()
        self.text = Text()

    def run(self):
        self.win.fill((100,120,255))
        self.text.txt("Platformer", 48, (0,0,0), (500, 250))
        self.text.txt("press enter to start", 24, (0,0,0), (500,350))
        k = key.get_pressed()

        if k[K_RETURN]:
            return True
        else:
            return False