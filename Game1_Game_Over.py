from pygame import *
from text import *
import json

class game_over:
    def __init__(self):
        self.screen = display.get_surface()
        self.star_img = image.load('Star.png').convert_alpha()
        self.empty_star_img = image.load('Empty_Star.png').convert_alpha()
        self.text = Text()
        self.star_num = 0
    
    def display(self, score, user):
        self.screen.fill((20,20,20))
        self.text.txt("Game Over!", 72, (255,255,255), (500,150))
        self.stars(score)
        self.text.txt("Your Score was "+str(score), 48, (255,255,255), (500,350))
        self.text.txt("Press r To Play Agian", 32, (255,255,255), (500,450))
        self.text.txt("Press enter To Quit", 32, (255,255,255), (500,550))
        
        self.update_score(score, user)
        self.update_stars(user)
        
    def stars(self, score):
        if score >= 40:
            self.screen.blit(self.star_img, (220, 210))
            self.screen.blit(self.star_img, (470, 210))
            self.screen.blit(self.star_img, (720, 210))
            self.star_num = 3
            
        elif score >= 20:
            self.screen.blit(self.star_img, (220, 210))
            self.screen.blit(self.star_img, (470, 210))
            self.screen.blit(self.empty_star_img, (720, 210))
            self.star_num = 2
            
        elif score >= 10:
            self.screen.blit(self.star_img, (220, 210))
            self.screen.blit(self.empty_star_img, (470, 210))
            self.screen.blit(self.empty_star_img, (740, 210))
            self.star_num = 1
            
        elif score < 10:
            self.screen.blit(self.empty_star_img, (220, 210))
            self.screen.blit(self.empty_star_img, (470, 210))
            self.screen.blit(self.empty_star_img, (720, 210))
        
    def retry(self):
        k = key.get_pressed()
        if k[K_r]:
            return True
        else:
            return False
    
    def leave(self):
        k = key.get_pressed()
        if k[K_RETURN]:
            return True
        else:
            return False
        
    def update_stars(self, user):
        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        stars = users[user][2]["Games"]["Game1"]["Stars"]
        
        if self.star_num > stars:
            users[user][2]["Games"]["Game1"]["Stars"] = self.star_num
            users[user][1]["Total Stars"] += self.star_num - stars
            
        f = open("Users.txt","w")
        json.dump(users, f)
        f.close()
        
    def update_score(self, new_score, user):
        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        score = users[user][2]["Games"]["Game1"]["Highscore"]
        
        if new_score > score:
            users[user][2]["Games"]["Game1"]["Highscore"] = new_score
            
        f = open("Users.txt","w")
        json.dump(users, f)
        f.close()