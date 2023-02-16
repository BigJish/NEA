from settings import *
from Game2_Title import *
from Game2_Player import *
from Game2_Platform import *
from Game2_Portal import *
from Game2_Game_Over import *

class Platformer:
    def __init__(self):
        self.win = display.get_surface()
        self.visible_sprites = sprite.Group()
        self.obsicle_sprites = sprite.Group()
        self.title = Title()
        self.text = Text()
        self.game_over = Game_over()
        self.player = Player(self.visible_sprites, (500,400), self.obsicle_sprites)
        self.screen = 1
        self.offset = 0
        self.score = 0
        self.startTime = 0
        self.setup()
    
    def setup(self):
        yVal = 460+r(40,100)
        xVal = r(0,900)
        Platform([self.visible_sprites, self.obsicle_sprites], (xVal,yVal))
        for level in range(1,20):
            yVal = r(70,100)
            nxVal = r(-80, 80)
            if 900 < xVal+nxVal or xVal+nxVal < 0:
                nxVal*=-1
            xVal += nxVal
            Platform([self.visible_sprites, self.obsicle_sprites], (xVal,460+yVal+(level*-100)))
        self.portal = Portal(self.visible_sprites, (xVal+20, 396+yVal+(level*-100)))
            
    def run(self, user):
        self.win.fill((60,60,60))
        if self.screen == 1:
            val = self.title.run(user)
            if val:
                self.screen = 2
                self.startTime = t()
        
        if self.screen == 2:
            self.score = t()-self.startTime
            self.win.fill((125,185,255))
            draw.rect(self.win, (155,118,83), (0,540+self.player.rect.h+self.offset, 1000, 200))
            for i in self.visible_sprites:
                i.update(self.offset)
            self.text.txt2("Time: "+str(round(self.score, 2)), 24, (0,0,0), (400,50))
            if self.player.rect.colliderect(self.portal.rect):
                self.screen = 3
            
            if self.player.rect.y + self.offset >= 150:
                self.offset += -2
            if self.player.rect.y + self.offset <= 450:
                self.offset += 2
        
        if self.screen == 3:
            self.game_over.display(self.score, user)

            if self.game_over.leave():
                return "exit"
            if self.game_over.retry():
                return "reset"