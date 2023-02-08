from pygame import *
init()

class player_name:
    def __init__(self, pos, groups, user):
        self.screen = display.get_surface()
        self.pos = pos
        user
        font1 = font.Font("PressStart2P-Regular.ttf",24)
        self.image = font1.render(user, True, (255,255,255))
        
    def draw(self):
        self.screen.blit(self.image,(self.pos[0] - self.image.get_width() // 2, self.pos[1] - self.image.get_height() // 2))
        
    def update(self):
        self.draw()