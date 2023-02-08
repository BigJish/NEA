from pygame import *
from sprite_sheet import *

class Player(sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.screen = display.get_surface()
        try:
            player_image = image.load(r"D:\Downloads\Thonny\Programs\Computer Science NEA\Jet.png").convert_alpha()
            

        except:
            player_image = image.load("Jet.png").convert_alpha()
            
            
        img = SpriteSheet(player_image)
        self.player_image = img.get_image(0, 602, 605, 0.15, (0, 0, 0))

        self.rect = self.player_image.get_rect(center = (pos))
        self.hitbox = self.rect
        self.rocket_count = 0
    
    def inputs(self):
        k = key.get_pressed()
        
        self.X_change = 0
        self.Y_change = 0

        if k[K_w]:
            self.Y_change += -3

        if k[K_s]:
            self.Y_change += 3

        if k[K_a]:
            self.X_change += -3

        if k[K_d]:
            self.X_change += 3
    
    def move(self):
        if self.rect.x+self.X_change <= 360 and self.rect.x+self.X_change >= 0:
            self.hitbox.x += self.X_change
        
        if self.rect.y+self.Y_change <= 600-self.rect.height and self.rect.y+self.Y_change >= 0:
            self.hitbox.y += self.Y_change

        self.rect.center = self.hitbox.center
        self.screen.blit(self.player_image,self.rect.topleft)
    
    def shoot(self):
        k = key.get_pressed()

        if k[K_SPACE] == False:
            return False
        

        if k[K_SPACE]:
            return True
        
    
    def update(self):
        self.shoot()
        self.inputs()
        self.move()