from pygame import *
from text import *
from sprite_sheet import*



class Title_Screen:
    def __init__(self,user):
        self.user = user
        self.visible_sprites = sprite.Group()
        self.screen = display.get_surface()
        self.text = Text()
        self.next_page = False
        bg = image.load("Title_bg.jpg").convert_alpha()
        bg = SpriteSheet(bg)
        self.bg = bg.get_image(0, 1000, 600, 1, (0, 0, 0))
        
    def run(self):
        if self.next_page == True:
            return True
        else:
            self.display()
        
    def display(self):
        k = key.get_pressed()
        if k[K_RETURN]:
            self.next_page = True
        
        self.screen.fill((100,150,255))
        self.screen.blit(self.bg, (0,0))
        
        self.text.txt("Welcome!", 72, (0,0,0), (500, 180))
        self.text.txt(self.user, 56, (0,0,0), (500, 300))
        self.text.txt("Press Enter to start!", 32, (0,0,0), (500, 400))      