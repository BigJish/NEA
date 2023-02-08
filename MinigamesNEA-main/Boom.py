from pygame import *
from sprite_sheet import *
from time import time

class Pow(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.screen = display.get_surface()
        Explode = image.load("explosion.png").convert_alpha()
        img = SpriteSheet(Explode)
        self.explosion = img.get_image(0, 600, 498, 0.3, (0, 0, 0))
        self.rect = self.explosion.get_rect(center = pos)
        self.n = 0
        self.t = time()
    
    def draw(self):
        self.screen.blit(self.explosion, self.rect)
    
    def timer(self):
        if time() - self.t >= 1:
            return True
        
    def update(self):
        self.draw()