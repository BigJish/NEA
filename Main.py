from pygame import *
from settings import *
from title import *
from Game1 import *
from Game3 import *
from Game2 import *
from Game4 import *
from hallway import *


class Game:
    def __init__(self,user):
        init()
        self.user = user
        self.screen  = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.end = False
        self.title = Title_Screen(user)
        self.screen_num = 1
        self.game1 = Aerial()
        self.game2 = Platformer()
        self.game3 = Maze()
        self.game4 = game4()
        self.hallway = Hallway(user)
        self.clock = time.Clock()

    def run(self):
        while self.end == False:   
            for e in event.get():
                if e.type == QUIT:
                    self.end = True
                    
            if self.screen_num == 1:
                if self.title.run() == True:
                    self.screen_num = 2
            
            elif self.screen_num == 2:
                self.hallway.run()
                if self.hallway.minigame() == 1:
                    self.screen_num = 3
                    
                if self.hallway.minigame() == 2:
                    self.screen_num = 4
                    
                if self.hallway.minigame() == 3:
                    self.screen_num = 5
                    
                if self.hallway.minigame() == 4:
                    self.screen_num = 6
            
            elif self.screen_num == 3:
                if self.game1.run(self.user) == True:
                    self.screen_num = 2
                    
            elif self.screen_num == 4:
                val = self.game2.run(self.user)
                
                if  val == "exit":
                    self.game2 = Platformer()
                    self.screen_num = 2

                if val == "reset":
                    self.game2 = Platform()
                    
            elif self.screen_num == 5:
                if self.game3.run() == True:
                    self.screen_num = 2
                    
            elif self.screen_num == 6:
                if self.game4.run() == True:
                    self.screen_num = 2
                
            self.clock.tick(60)
            display.flip()
        
        quit()

if __name__ == '__main__':
    game = Game("Admin")
    game.run()