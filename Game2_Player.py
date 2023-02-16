from settings import *

class Player(sprite.Sprite):
    def __init__(self, groups, pos, obsticles):
        super().__init__(groups)
        self.win = display.get_surface()

        self.idle_img = image.load('Idle_Player1.png').convert_alpha()
        self.player_left = image.load('Walk_Left.png').convert_alpha()
        self.player_right = image.load('Walk_Right.png').convert_alpha()

        sprite_sheet = SpriteSheet(self.idle_img)
        self.idle = []
        for i in range(0,8):
            self.idle.append(sprite_sheet.get_image(i, 76, 100, 0.55, (0,0,0)))
        self.image = sprite_sheet.get_image(0, 76, 100, 0.55, (0, 0, 0))

        sprite_sheet = SpriteSheet(self.player_left)
        self.left = []
        for i in range(0,8):
            self.left.append(sprite_sheet.get_image(i, 76, 100, 0.55, (0,0,0)))
        
        sprite_sheet = SpriteSheet(self.player_right)
        self.right = []
        for i in range(0,8):
            self.right.append(sprite_sheet.get_image(i, 76, 100, 0.55, (0,0,0)))

        self.frame_count = 0
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect
        self.direction = math.Vector2()

        self.speed = 3
        self.grav = 0.5
        self.jump = False
        self.obsticles = obsticles
    
    def input(self):

        k = key.get_pressed()

        if k[K_a]:
            self.direction.x = -self.speed
            self.animation(self.left, 60)

        elif k[K_d]:
            self.direction.x = self.speed
            self.animation(self.right, 60)

        else:
            self.direction.x = 0
            self.animation(self.idle, 8)
        
        if self.jump == False:
            if k[K_SPACE]:
                self.direction.y = -12
                self.jump = True
    
    def move(self, offset):
        if  self.rect.y + self.direction.y < 540 and self.direction.y <= 10:
            self.direction.y += self.grav

        if self.rect.y + self.direction.y >= 540:
            self.rect.y = 540
            self.direction.y = 0
            self.jump = False

        self.hitbox.x += self.direction.x
        self.collision("horizontal")
        self.hitbox.y += self.direction.y
        self.collision("vertical")
        self.rect.center = self.hitbox.center
        self.win.blit(self.image, (self.rect.x, self.rect.y+offset))
    
    def animation(self, sprite_sheet, delay):
        if self.frame_count//delay >= 8:
            self.frame_count = 0
        frame_num = self.frame_count//delay
        self.image = sprite_sheet[frame_num]
        self.frame_count += 1
    
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
                        self.jump = False
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                        self.direction.y = 0

    def update(self, offset):
        self.input()
        self.move(offset)