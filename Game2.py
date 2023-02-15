from settings import *
from Game2_Title import *
from Game2_Player import *
from Game2_Platform import *

class Platformer:
    def __init__(self):
        self.win = display.get_surface()
        self.visible_sprites = sprite.Group()
        self.obsicle_sprites = sprite.Group()
        self.title = Title()
        self.player = Player(self.visible_sprites, (500,400), self.obsicle_sprites)
        self.screen = 1
        self.offset = 0
        self.setup()
    
    def setup(self):
        yVal = 460+r(40,100)
        xVal = r(0,900)
        Platform([self.visible_sprites, self.obsicle_sprites], (xVal,yVal))
        for level in range(1,20):
            yVal = r(70,100)
            xVal = xVal+r(-80, 80)
            Platform([self.visible_sprites, self.obsicle_sprites], (xVal,460+yVal+(level*-100)))
            
    def run(self):
        self.win.fill((60,60,60))
        if self.screen == 1:
            val = self.title.run()
            if val:
                self.screen = 2
        
        if self.screen == 2:
            self.win.fill((125,185,255))
            for i in self.visible_sprites:
                i.update(self.offset)
            
            if self.player.rect.y + self.offset >= 150:
                self.offset += -2
            if self.player.rect.y + self.offset <= 450:
                self.offset += 2