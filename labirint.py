# Разработай свою игру в этом файле!
from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
black = (200,255,0)
bullets = sprite.Group()
monsters = sprite.Group()

x_speed = 0
y_speed = 0
class GameSprite(sprite.Sprite):
    def __init__ (self,picture,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,picture,w,h,x,y,x_speed,y_speed):
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self,barries,False)
        if self.x_speed > 0:
            for p in platforms_touched:
               self.rect.right = min (self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left,p.rect.right)
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self,barries,False)
        if self.y_speed > 0:
            for p in platforms_touched:
                   self.rect.bottom = min (self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top,p.rect.bottom)
    def fire(self):
        bullet_0 = bullet('bullet.png',30,30, self.rect.right, self.rect.centery, 4)
        bullets.add(bullet_0)
class Enemy(GameSprite):
    def __init__(self,picture,w,h,x,y,speed,x1,x2):
        super().__init__(picture,w,h,x,y)
        self.speed = speed
        self.x1 = x1
        self.x2 =x2
    def update(self):
        if self.rect.x <= self.x1:
            self.direction = "right"
        if self.rect.x >= self.x2 - 85:
            self.direction ="left"
        if self.direction == "left":
            self.rect.x -= self.speed   
        else:
            self.rect.x += self.speed
class bullet (GameSprite):
    def __init__(self,picture,w,h,x,y,speed):
        super().__init__(picture,w,h,x,y)
        self.speed = speed
    def update (self):
        self.rect.x += self.speed
        if self.rect.x > win_width:
            self.kill()

        

        
run = True
finish = False
wall_1 = GameSprite('plitka-stena.jpg',80,20,165,250)
wall_2 = GameSprite('plitka-stena.jpg',20,300,165 ,250)
wall_3 = GameSprite('plitka-stena.jpg', 20,380,370 ,0)
wall_4 = GameSprite('plitka-stena.jpg', 110,20,280 ,380)
wall_5 = GameSprite('plitka-stena.jpg', 20,150,470 ,100)
wall_7 = GameSprite('plitka-stena.jpg', 100,20,390 ,90)
wall_6 = GameSprite('plitka-stena.jpg', 20,150,470 ,350)
player = Player ('free-icon-ghost-8534244.png',65,65,40,20,x_speed,y_speed)
final = GameSprite('win.png', 65, 65, 405, 15)

monster = Enemy('monster.png', 65,65, 480, 100,2,500, 700)
monster_2 = Enemy('monster.png', 65,65, 40, 400,3,40, 420)
monsters.add(monster)
monsters.add(monster_2)

win = transform.scale(image.load('images.png'),(700,500))
lose = transform.scale(image.load('lose.png'),(700,500))
barries = sprite.Group()
barries.add(wall_1)
barries.add(wall_2)
barries.add(wall_3)
barries.add(wall_4)
barries.add(wall_5)
barries.add(wall_6)
barries.add(wall_7)
while run:
    if finish != True:
        window.fill(black)
        barries.draw(window)
        sprite.groupcollide(bullets, barries, True, False)
        sprite.groupcollide(bullets, monsters,True,True)

        player.reset()
        player.update()
        bullets.draw(window)
        bullets.update()
        monsters.update()
        monsters.draw(window)
        final.reset()
        time.delay(50)
        if sprite.spritecollide(player, monsters,True):
            finish = True
            window.blit(lose,(0,0))
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win,(0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
            if e.key == K_w:
                player.y_speed = -4
            if e.key == K_s:
                player.y_speed = 4
            if e.key == K_a:
                player.x_speed = -4
            if e.key == K_d:
                player.x_speed = 4
        elif e.type == KEYUP:
            if e.key == K_w:
                player.y_speed = 0
            if e.key == K_s:
                player.y_speed = 0
            if e.key == K_a:
                player.x_speed = 0
            if e.key == K_d:
                player.x_speed = 0

        

    display.update()

