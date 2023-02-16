from settings import *

class Title:
    def __init__(self):
        self.win = display.get_surface()
        self.text = Text()

    def run(self,user):
        self.win.fill((100,120,255))
        self.text.txt("Platformer", 48, (0,0,0), (500, 250))
        self.text.txt("Your best time is "+str(self.get_score(user)), 32, (0,0,0), (500, 300))
        self.text.txt("press enter to start", 24, (0,0,0), (500,350))
        k = key.get_pressed()

        if k[K_RETURN]:
            return True
        else:
            return False
        
    def get_score(self, user):
        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        score = users[user][2]["Games"]["Game2"]["Highscore"]
        return score