from settings import *

class Portal(sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.win = display.get_surface()
        self.image = image.load("Game2_Portal.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect
    
    def update(self, offset):
        self.win.blit(self.image,(self.rect[0], self.rect[1]+offset))

        