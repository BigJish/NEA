from pygame import *

class Player(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.screen = display.get_surface()
        self.player_up = image.load('Test image.jpg').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)