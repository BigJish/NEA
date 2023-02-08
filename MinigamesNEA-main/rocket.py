from pygame import *

class Rocket(sprite.Sprite):
    def __init__(self, pos, groups, enemies):
        super().__init__(groups)

        self.screen = display.get_surface()

        self.rocket_image = image.load("Player_Rocket.png").convert_alpha()
            
        self.rect = self.rocket_image.get_rect(center = (pos))
        self.screen.blit(self.rocket_image,self.rect.topleft)
        self.hitbox = self.rect.inflate(-30, -30)
        self.enemies = enemies

        
    
    def move(self):
        self.X_change = 20
        self.hitbox.x += self.X_change
        self.rect.center = self.hitbox.center
        self.screen.blit(self.rocket_image,self.rect.topleft)
    
    def hit(self):
        for enemy in self.enemies:
            if enemy.hitbox.colliderect(self.hitbox):
                return True
    
    def off_screen(self):
        if self.rect.x >= 1000:
            return True
    
    
    def update(self):
        self.move()
    

    