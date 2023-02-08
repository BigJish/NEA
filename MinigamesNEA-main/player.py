from pygame import *
from sprite_sheet import SpriteSheet
from text import *

class Player(sprite.Sprite):
    def __init__(self, pos, groups, obsticles, user):
        super().__init__(groups)
        self.screen = display.get_surface()
        self.idle_img = image.load('Idle_Player1.png').convert_alpha()
        self.player_up = image.load('Walk_Up.png').convert_alpha()
        self.player_down = image.load('Walk_Down.png').convert_alpha()
        self.player_left = image.load('Walk_Left.png').convert_alpha()
        self.player_right = image.load('Walk_Right.png').convert_alpha()
        self.obsticles = obsticles
        sprite_sheet = SpriteSheet(self.player_down)
        self.image = sprite_sheet.get_image(0, 76, 100, 1, (0, 0, 0))
        self.rect = self.image.get_rect(topleft = pos)
        self.frames = []
        self.frame_count = 0
        self.hitbox = self.rect.inflate(-60, -70)
        self.direction = math.Vector2()
        self.speed = 4
        self.text = Text()
        self.user = user
 
    def inputs(self):
        k = key.get_pressed()

        if k[K_w]:
            self.direction.y = -1
            self.animation(self.player_up)
        elif k[K_s]:
            self.direction.y = 1
            self.animation(self.player_down)
        else:
            self.direction.y = 0
            self.idle()
            
        if k[K_a]:
            self.direction.x = -1
            self.animation(self.player_left)
        elif k[K_d]:
            self.direction.x = 1
            self.animation(self.player_right)
        else:
            self.direction.x = 0
            
        if self.direction.x == 0 and self.direction.y == 0:
            self.idle()
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        collision = False
        for i in self.obsticles:
            if i.hitbox.colliderect(self.hitbox):
                collision = True
                
        self.hitbox.x += self.direction.x*speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y*speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obsticles:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        
        if direction == "vertical":
            for sprite in self.obsticles:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                        
    
    def animation(self, sprite_sheet_image):
        if sprite_sheet_image == self.player_right or sprite_sheet_image == self.player_left:
            sprite_sheet = SpriteSheet(sprite_sheet_image)
            self.frames = []
            if self.frame_count//8 >= 8:
                self.frame_count = 0
            frame_num = self.frame_count//8
            for i in range(0,8):
                self.frames.append(sprite_sheet.get_image(i, 76, 100, 1, (0,0,0)))
            self.image = self.frames[frame_num]
            self.frame_count += 1
        elif sprite_sheet_image == self.player_up or sprite_sheet_image == self.player_down:
            sprite_sheet = SpriteSheet(sprite_sheet_image)
            self.frames = []
            if self.frame_count//5 >= 8:
                self.frame_count = 0
            frame_num = self.frame_count//5
            for i in range(0,8):
                self.frames.append(sprite_sheet.get_image(i, 76, 100, 1, (0,0,0)))
            self.image = self.frames[frame_num]
            self.frame_count += 1
        
    def idle(self):
        sprite_sheet = SpriteSheet(self.idle_img)
        self.frames = []
        if self.frame_count//60 >= 8:
            self.frame_count = 0
        frame_num = self.frame_count//60
        for i in range(0,8):
            self.frames.append(sprite_sheet.get_image(i, 76, 100, 1, (0,0,0)))
        self.image = self.frames[frame_num]
        self.frame_count += 1

    def update(self):
        self.inputs()
        self.move(self.speed)