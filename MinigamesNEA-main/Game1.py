from pygame import *
from PlayerPlane import *
from rocket import *
from time import time as t
from EnemyPlane import *
from text import *
from Boom import *
from Enemy_Rocket import *
from Game1_Game_Over import *
from Game1_Title import *


class Aerial:
    def __init__(self):
        self.screen = display.get_surface()
        
        self.visible_sprites = sprite.Group()
        self.enemy_sprites = sprite.Group()
        self.rocket_sprites = sprite.Group()
        self.obstcale_sprites = sprite.Group()
        self.enemy_rocket_sprites = sprite.Group()
        
        self.bg_img = image.load('Game1_bg.jpg').convert_alpha()
        
        self.collisions = []
        self.explosions = []
        
        self.text = Text()
        self.GameOver = game_over()
        self.title = game1_title()
        
        self.score = 0
        self.rocket_cooldown = 99999
        self.enemy_cooldown = 0
        self.difficulty_factor = 0.95
        self.cooldown = 2
        self.dead = False
        self.key_held = False
        
        self.scrn_num = 1
        
        self.setup()
        
    def setup(self):
        self.player = Player((200,300),self.visible_sprites)
    
    def run(self, user):
        if self.scrn_num == 1:
            if self.title.run(user) == True:
                self.scrn_num = 2
            
        if self.scrn_num == 2:
            if self.dead == False:
                self.screen.blit(self.bg_img,(0,0))
                self.text.txt(str(self.score), 128,(0,0,0), (150, 300))
                if self.player.shoot() == True:
                    if self.key_held == False:
                        if t() - self.rocket_cooldown >= 0.5:
                            self.rocket_cooldown = t()
                            self.key_held = True
                            Rocket(self.player.rect.center, [self.visible_sprites, self.rocket_sprites, self.obstcale_sprites], self.enemy_sprites)
               
                for i in self.enemy_sprites:
                    if i.shoot() == True:
                        enemy_rocket((i.rect.x, i.rect.y+25), [self.visible_sprites, self.enemy_rocket_sprites])
                    
                if t() - self.enemy_cooldown >= self.cooldown:
                    self.enemy_cooldown = t()
                    self.cooldown *= self.difficulty_factor
                    Enemy([self.visible_sprites, self.enemy_sprites, self.obstcale_sprites], self.rocket_sprites)
                    
                
                for i in self.obstcale_sprites:
                    if i.hit() == True:
                        self.visible_sprites.remove(i)
                        self.obstcale_sprites.remove(i)
                        self.collisions.append(i)
                        
                        
                for i in self.collisions:
                    for j in self.enemy_sprites:
                        if j == i:
                            self.enemy_sprites.remove(i)
                            self.score += 1
                            self.explosions.append(Pow(i.rect.center, self.visible_sprites))
                    for j in self.rocket_sprites:
                        if j == i:
                            self.rocket_sprites.remove(i)
                            
                            
                for i in self.rocket_sprites:
                    if i.off_screen() == True:
                        self.visible_sprites.remove(i)
                        self.obstcale_sprites.remove(i)
                        self.rocket_sprites.remove(i)
                
                for i in self.explosions:
                    if i.timer() == True:
                        self.visible_sprites.remove(i)
                        
                for i in self.enemy_rocket_sprites:
                    if i.collide(self.player) == True:
                        self.visible_sprites.remove(self.player)
                        self.explosions.append(Pow(self.player.rect.center, self.visible_sprites))
                        self.dead = True
                        
                for i in self.visible_sprites:
                    i.update()

                if self.player.shoot() == False:
                    self.key_held = False
                    
            if self.dead == True:
                self.GameOver.display(self.score, user)
                
                if self.GameOver.retry() == True:
                    self.visible_sprites = sprite.Group()
                    self.enemy_sprites = sprite.Group()
                    self.rocket_sprites = sprite.Group()
                    self.obstcale_sprites = sprite.Group()
                    self.enemy_rocket_sprites = sprite.Group()
                    self.screen = display.get_surface()
                    self.key_held = False
                    self.text = Text()
                    self.GameOver = game_over()
                    self.score = 0
                    self.rocket_cooldown = 99999
                    self.setup()
                    self.collisions = []
                    self.explosions = []
                    self.enemy_cooldown = 0
                    self.cooldown = 2
                    self.dead = False
                    self.scrn_num = 1
                    
                if self.GameOver.leave() == True:
                    self.visible_sprites = sprite.Group()
                    self.enemy_sprites = sprite.Group()
                    self.rocket_sprites = sprite.Group()
                    self.obstcale_sprites = sprite.Group()
                    self.enemy_rocket_sprites = sprite.Group()
                    self.screen = display.get_surface()
                    self.key_held = False
                    self.text = Text()
                    self.GameOver = game_over()
                    self.score = 0
                    self.rocket_cooldown = 99999
                    self.setup()
                    self.collisions = []
                    self.explosions = []
                    self.enemy_cooldown = 0
                    self.cooldown = 2
                    self.dead = False
                    self.scrn_num = 1
                    
                    return True
                else:
                    return False