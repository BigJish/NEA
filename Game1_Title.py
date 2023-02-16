from settings import *

class game1_title:
    def __init__(self):
        self.screen = display.get_surface()
        self.bg_img = image.load('Game1_bg.jpg').convert_alpha()
        self.text = Text()
        
    def run(self, user):
        self.screen.blit(self.bg_img,(0,0))
        self.text.txt("Sky Raiders!", 64, (0,0,0), (500, 180))
        self.text.txt("Your highscore is "+str(self.get_score(user)), 32, (0,0,0), (500, 300))
        self.text.txt("Press enter to start", 36, (0,0,0), (500, 420))
        k = key.get_pressed()
        if k[K_RETURN]:
            return True
        
    def get_score(self, user):
        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        score = users[user][2]["Games"]["Game1"]["Highscore"]
        return score