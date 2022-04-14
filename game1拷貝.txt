import pygame
import random
import os
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img,(40,45))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2 , HEIGHT-100)
        self.radius = 20
    def update(self):
        key_pressed =  pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            self.rect.x += 6
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self.rect.x -= 6
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH   
        if self.rect.left < 0:
            self.rect.left = 0         
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(rock_img,(40,45))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150,-40)
        self.speed_y = random.randrange(4,7)
        self.speed_x = random.randrange(-3,3)
        self.reflect = 0
        self.reflectpoint = random.randrange(240,300)
        self.radius = 20

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()               
        if self.rect.bottom > 520  :
            self.speed_y = -self.speed_y
            if self.speed_x < 1 and self.speed_x > -1:
                self.speed_x += random.choice([2,-2]) 
            self.reflect += 1
        if self.reflect >= 1:
            if self.rect.top < self.reflectpoint:
                self.speed_y = -self.speed_y
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface= font.render(text , True , RED)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface , text_rect)

def draw_init():
    draw_text(screen, 'press any bottom to start' , 30 , WIDTH/2 , HEIGHT/2)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                waiting = False
                return False       



font_name = pygame.font.match_font('arial')

FPS = 60
COLOR = (255,255,255)
WIDTH = 500
HEIGHT = 600
PCOLOR = (54,48,51)
RCOLOR = (102,49,12)
LCOLOR = (0,0,0)
RED = (255,0,0)
n=0
pygame.init()
pygame.mixer.init( )
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
true = True
show = True
player_img=pygame.image.load(os.path.join("pics", "player.png")).convert()
rock_img = pygame.image.load(os.path.join("pics", "rock.png")).convert()
pygame.mixer.music.load(os.path.join("background.mp3"))
r=pygame.sprite.Group()
p=pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
p.add(player)
key_pressed =  pygame.key.get_pressed()
pygame.mixer.music.play(-1)
while true:
        if show:
            close = draw_init()
            if close:
                break
            show=False
            r=pygame.sprite.Group()
            p=pygame.sprite.Group()
            all_sprites = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            p.add(player)
            b=pygame.time.get_ticks()//1000
            b=int(b)
        score=pygame.time.get_ticks()//1000-b 
        if score >= 30:            
            g=random.randrange(0,23)
        else:
            g=random.randrange(0,32)    
        if g == 5:
            rock=Rock()
            all_sprites.add(rock)
            r.add(rock)
        clock.tick(FPS)     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                true=False
        all_sprites.update()
        a=pygame.sprite.groupcollide(p, r , False ,False ,pygame.sprite.collide_circle)            
        if a:
            show = True
        screen.fill(COLOR)
        all_sprites.draw(screen)
        draw_text(screen ,str(score),30,WIDTH/2,20 )
        pygame.draw.line(screen,LCOLOR,(0,520),(500,520),4)
        pygame.display.update()
pygame.quit()        
                
