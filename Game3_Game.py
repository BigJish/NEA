from pygame import *
from Maps import *
from Game3_Wall import *
from Game3_Player import *
from Game3_Exit import *

class AmMaze:
    def __init__(self):
        self.screen = display.get_surface()
        self.visible_sprites = Camera()
        self.obsticle_sprites = sprite.Group()
        self.setup()
        
    def setup(self):
        for i in range (0,4):
            for row_index, row in enumerate(maps[i]):
                for col_index, col in enumerate(row):
                    if i == 0:
                        x = col_index * 128
                        y = row_index * 128
                    if i == 1:
                        x = col_index * 128+1536
                        y = row_index * 128
                    if i == 2:
                        x = col_index * 128
                        y = row_index * 128+1536
                    if i == 3:
                        x = col_index * 128+1536
                        y = row_index * 128+1536
                    if col == "x":
                        Wall([self.visible_sprites, self.obsticle_sprites], (x,y))
                    if col == "p":
                        self.player = Player(self.visible_sprites, (x,y), self.obsticle_sprites)
                    if col =="e":
                        self.exit = Exit([self.visible_sprites], (x+32,y+32))
                   
    def Blackout(self):
        draw.rect(self.screen, (0,0,0),(0, -200, 1000, 1000), 200)
        draw.ellipse(self.screen, (0,0,0),(0, -200, 1000, 1000), 200)
        
    def run(self):
        self.screen.fill((60,60,60))
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        if self.exit.leave(self.player) == True:
            return True
        self.Blackout()
            
class Camera(sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)