from pygame import *
init()

class Text:
    def __init__(self):
        self.screen = display.get_surface()
        
    def txt(self, text, fontsize, colour , pos):
        font1 = font.Font("PressStart2P-Regular.ttf",fontsize)
        text = font1.render(text, True, colour)
        self.screen.blit(text,(pos[0] - text.get_width() // 2, pos[1] - text.get_height() // 2))

    def txt2(self, text, fontsize, colour , pos):
        font1 = font.Font("PressStart2P-Regular.ttf",fontsize)
        text = font1.render(text, True, colour)
        self.screen.blit(text,pos)