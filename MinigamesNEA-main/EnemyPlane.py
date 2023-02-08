from pygame import *
from sprite_sheet import *
from random import randint as r
from time import time as t

class Enemy(sprite.Sprite):
    def __init__(self,groups, rockets):
        super().__init__(groups)
        self.screen = display.get_surface()
        self.enemy_image = image.load("Enemy_Plane.png").convert_alpha()

        self.rect = self.enemy_image.get_rect(center = (1100,0))
        self.hitbox = self.rect
        self.x = r(600,900)
        self.y = r(0,500)
        self.rockets = rockets
        self.cooldown = 3
        self.time = t()
    
    def spawn(self,x,y):
        self.rect.y = y
        if self.rect.x >= x:
            self.rect.x -= 1
    
    def hit(self):
        for rocket in self.rockets:
            if rocket.hitbox.colliderect(self.hitbox):
                return True
            
    def shoot(self):
        if t() - self.time >= self.cooldown:
            self.time = t()
            return True
            
    def update(self):
        self.screen.blit(self.enemy_image,self.rect.topleft)
        self.spawn(self.x, self.y)