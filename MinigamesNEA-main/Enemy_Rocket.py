from pygame import *
from sprite_sheet import *

class enemy_rocket(sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups) 
        self.screen = display.get_surface() 
        
        self.rocket_image = image.load("Enemy_Rocket.png").convert_alpha()
        
        self.rect = self.rocket_image.get_rect(center = (pos))
        self.screen.blit(self.rocket_image,self.rect.topleft)
        self.hitbox = self.rect.inflate(-30, -30)
        
    
    def move(self):
        self.X_change = -10
        self.hitbox.x += self.X_change
        self.rect.center = self.hitbox.center
        self.screen.blit(self.rocket_image,self.rect.topleft)
    
    def collide(self, player):
        if self.hitbox.colliderect(player.hitbox):
            return True
    
        
    def off_screen(self):
        if self.rect.x <= 0:
            return True
    
    
    def update(self):
        self.move()