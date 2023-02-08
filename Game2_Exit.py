from pygame import *

class Exit(sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = image.load('Game2_Portal.png').convert_alpha()
        self.rect = self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect
    
    def leave(self, player):
        if self.hitbox.colliderect(player.hitbox):
            return True
        