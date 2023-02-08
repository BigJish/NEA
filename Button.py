from pygame import *
from text import*

class button:
    def __init__(self, pos, width, height , colour1, t, colour2, font_size):
        self.screen = display.get_surface()
        self.colour1 = colour1
        self.colour2 = colour2
        self.bg_colour = colour1
        self.text_colour = colour2
        self.font_size = font_size
        self.t = t
        self.text = Text()
        self.rect = Rect(pos[0], pos[1], width, height)
    
    def draw(self):
        draw.rect(self.screen, self.bg_colour, self.rect)
        self.text.txt(self.t,self.font_size, self.text_colour, self.rect.center)
    
    def collide(self):
        mpos = mouse.get_pos()
        if self.rect.collidepoint(mpos[0],mpos[1]):
            self.text_colour = self.colour1
            self.bg_colour = self.colour2
            if mouse.get_pressed()[0]:
                return True
        else :
            temp = self.text_colour
            self.text_colour = self.colour2
            self.bg_colour = self.colour1
    
    def update(self):
        if self.collide() == True:
            return True
        self.draw()
        