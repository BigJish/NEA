from pygame import *


class bg(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.screen = display.get_surface()
        self.image = image.load('Hallway_bgv2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect
    
    def upadte(self):
        self.screen.blit(self.image, self.rect.center)