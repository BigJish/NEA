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
        for level in range (1,20):
            atLevel = r(1, 4)
            for i in range(0, atLevel):
                yVal = r(20,100)
                Platform([self.visible_sprites, self.obsicle_sprites], (r(0,900),yVal+420+(level*-80)))
            
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
                self.offset += -1
            if self.player.rect.y + self.offset <= 450:
                self.offset += 1