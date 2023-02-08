from pygame import *
from text import *
import json
from time import time as t

class Portal(sprite.Sprite):
    def __init__(self, pos, groups, user, game):
        super().__init__(groups)
        self.screen = display.get_surface()
        
        self.unlocked_img = image.load('Unlocked_Portal.png').convert_alpha()
        self.locked_img = image.load('Locked_Portal.png').convert_alpha()
        
        self.image = self.locked_img 
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect
        self.hitbox = self.hitbox.inflate(80,0)
        
        self.star_img = image.load('Star.png').convert_alpha()
        self.empty_star_img = image.load('Empty_Star.png').convert_alpha()
        
        self.user = user
        self.text = Text()
        self.txt_hitbox = self.rect.inflate(0,20)
        self.game = game
        self.clicked = False
        self.click_cooldown = 2
        self.click_time = 0
        
        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        self.status = users[self.user][2]["Games"][self.game]["Status"]
    
    def enter(self, player):
        k = key.get_pressed()
        if player.hitbox.colliderect(self.txt_hitbox) and self.status == True:
            self.star_num()
            self.text.txt("Press E To Enter!", 32, (255,255,255), (500, 400))
            if k[K_e]:
                return True
            else:
                return False
            
        elif player.hitbox.colliderect(self.txt_hitbox) and self.status == False:
            self.text.txt("Press E To Unlock!", 32, (255,255,255), (500, 400))
            f = open("Users.txt","r")
            users = json.load(f)
            f.close()
            stars = users[self.user][1]["Total Stars"]
            if stars >= 2:
                if k[K_e]:
                    self.status = True
                    users[self.user][1]["Total Stars"] -= 2 
                    f = open("Users.txt","w")
                    json.dump(users, f)
                    f.close()
                    self.change_status()
                    
            elif stars < 2:
                if k[K_e]:
                    self.clicked = True
                    self.click_time = t()
                    
            if self.clicked == True:
                self.text.txt("You need "+str(2-stars)+" More Stars!", 32, (200,20,20), (500, 450))
                
            if t()- self.click_time >= self.click_cooldown:
                self.clicked = False
                
        else:
            return False
            
    
    def draw(self):
        if self.status == True:
            self.image = self.unlocked_img
        
    def star_num(self):
        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        stars = users[self.user][2]["Games"][self.game]["Stars"]
        if stars == 3:
            self.screen.blit(self.star_img, (405, 480))
            self.screen.blit(self.star_img, (470, 470))
            self.screen.blit(self.star_img, (535, 480))
            
        elif stars == 2:
            self.screen.blit(self.star_img, (405, 480))
            self.screen.blit(self.star_img, (470, 470))
            self.screen.blit(self.empty_star_img, (535, 480))
            
        elif stars == 1:
            self.screen.blit(self.star_img, (405, 480))
            self.screen.blit(self.empty_star_img, (470, 470))
            self.screen.blit(self.empty_star_img, (535, 480))
            
        elif stars == 0:
            self.screen.blit(self.empty_star_img, (405, 480))
            self.screen.blit(self.empty_star_img, (470, 470))
            self.screen.blit(self.empty_star_img, (535, 480))
        
    def change_status(self):
        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        users[self.user][2]["Games"][self.game]["Status"] = True
        self.status = users[self.user][2]["Games"][self.game]["Status"]
        f = open("Users.txt","w")
        json.dump(users, f)
        f.close()
        
    def update(self):
        self.draw()