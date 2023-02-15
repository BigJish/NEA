from settings import *

class Platform(sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.win = display.get_surface()
        self.rect = Rect(pos[0], pos[1], 100,20)
        self.hitbox = self.rect
    
    def update(self, offset):
        draw.rect(self.win,(255,100,50), (self.rect.x, self.rect.y+offset, self.rect.w, self.rect.h))
