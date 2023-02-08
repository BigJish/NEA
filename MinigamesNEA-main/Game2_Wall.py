from pygame import *

class Wall(sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = image.load('Game2_Wall.png').convert_alpha()
        self.rect = self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect