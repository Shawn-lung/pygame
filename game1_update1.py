import pygame
import random
import os


def updateRecord(score):
    currentRecord = getRecord()
    if currentRecord < score:
        print("writing record: ", score)
        with open("record.txt", "w") as file:
            file.write(str(score))


def getRecord():
    with open("record.txt", "r") as file:
        record = int(file.read())
    return record


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player1_img, (40, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT-100)
        self.hasCrown = False
        self.radius = 20
        self.speedr = 0
        self.speedl = 0
        self.speedd = 0
        self.speedu = 0

    def update(self):
        key_pressed = pygame.key.get_pressed()
        self.rect.centerx += self.speedr - self.speedl
        self.rect.centery += self.speedd - self.speedu
        if self.rect.centery < HEIGHT-100:
            self.speedd += 0.8
        if self.rect.centery >= HEIGHT-100:
            self.speedd = 0
            self.speedu = 0  # 刪掉這行會變跳跳
            self.rect.centery = HEIGHT-100
        if self.speedr != 0:
            self.speedr -= 0.5
        if self.speedl != 0:
            self.speedl -= 0.5
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            if self.speedr <= 7:
                self.speedr += 1
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            if self.speedl <= 7:
                self.speedl += 1
        if key_pressed[pygame.K_SPACE]:
            if self.rect.centery >= HEIGHT-100:
                self.speedu += 18
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.onTheGround():
            if self.hasCrown:
                self.image = pygame.transform.scale(
                    player1withcrown_img, (40, 45))
            else:
                self.image = pygame.transform.scale(player1_img, (40, 45))
        else:
            if self.hasCrown:
                self.image = pygame.transform.scale(
                    player2withcrown_img, (40, 45))
            else:
                self.image = pygame.transform.scale(player2_img, (40, 45))

    def onTheGround(self):
        if self.rect.centery == HEIGHT - 100:
            return True
        else:
            return False

    def setHasCrown(self, bool):
        self.hasCrown = bool


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Random pics
        rand = random.randrange(1, 3)
        if rand == 1:
            self.image = pygame.transform.scale(rock1_img, (40, 45))
        else:
            self.image = pygame.transform.scale(rock2_img, (40, 45))

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -40)
        self.speed_y = random.randrange(4, 7)
        self.speed_x = random.randrange(-3, 3)
        self.reflect = 0
        self.reflectpoint = random.randrange(240, 300)
        self.radius = 20

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()
        if self.rect.bottom > 520:
            self.speed_y = -self.speed_y
            if self.speed_x < 1 and self.speed_x > -1:
                self.speed_x += random.choice([2, -2])
            self.reflect += 1
        if self.reflect >= 1:
            if self.rect.top < self.reflectpoint:
                self.speed_y = -self.speed_y
        if self.onTheGround():
            self.image = pygame.transform.scale(rock3_img, (40, 45))

    def onTheGround(self):
        if self.rect.bottom >= 520:
            return True
        else:
            return False


class items(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(20, WIDTH - 20), 282)
        self.radius = 20


class Crown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(crown_img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(20, WIDTH - 20), 282)
        self.radius = 20


class Sword(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(sword_img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(20, WIDTH - 20), 282)
        self.radius = 20


def draw_text(surf, text: str, size: int, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface, text_rect)


def draw_init():
    draw_text(screen, 'press any bottom to start', 30, WIDTH/2, HEIGHT/2)
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
COLOR = (255, 255, 255)
WIDTH = 500
HEIGHT = 600
PCOLOR = (54, 48, 51)
RCOLOR = (102, 49, 12)
LCOLOR = (0, 0, 0)
RED = (255, 0, 0)
n = 0
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
true = True
show = True

player1_img = pygame.image.load(os.path.join("pics", "player1.png")).convert()
player2_img = pygame.image.load(os.path.join("pics", "player2.png")).convert()
player1withcrown_img = pygame.image.load(
    os.path.join("pics", "player1withcrown.png")).convert()
player2withcrown_img = pygame.image.load(
    os.path.join("pics", "player2withcrown.png")).convert()
rock1_img = pygame.image.load(os.path.join("pics", "rock1.png")).convert()
rock2_img = pygame.image.load(os.path.join("pics", "rock2.png")).convert()
rock3_img = pygame.image.load(os.path.join("pics", "rock3.png")).convert()
sword_img = pygame.image.load(os.path.join("pics", "sword.png")).convert()
crown_img = pygame.image.load(os.path.join("pics", "crown.png")).convert()


pygame.mixer.music.load(os.path.join("background.mp3"))
r = pygame.sprite.Group()
p = pygame.sprite.Group()
swords = pygame.sprite.Group()
crowns = pygame.sprite.Group()

player = Player()

p.add(player)
key_pressed = pygame.key.get_pressed()
pygame.mixer.music.play(-1)
while true:
    if show:
        close = draw_init()
        if close:
            break
        show = False
        swords = pygame.sprite.Group()
        crowns = pygame.sprite.Group()
        r = pygame.sprite.Group()
        p = pygame.sprite.Group()
        player = Player()
        p.add(player)
        b = pygame.time.get_ticks()//1000
        b = int(b)
    score = pygame.time.get_ticks()//1000-b
    if score >= 30:
        g = random.randrange(0, 23)
    else:
        g = random.randrange(0, 32)
    if g == 5:
        rock = Rock()
        r.add(rock)
    ran = random.randrange(0, 350)
    if ran == 3:
        sword = Sword()
        swords.add(sword)
    elif ran == 5:
        crown = Crown()
        crowns.add(crown)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            updateRecord(score)
            true = False
    p.update()
    r.update()
    a = pygame.sprite.groupcollide(
        p, r, False, True, pygame.sprite.collide_circle)
    ps = pygame.sprite.groupcollide(
        p, swords, False, True, pygame.sprite.collide_circle)
    pc = pygame.sprite.groupcollide(
        p, crowns, False, True, pygame.sprite.collide_circle)

    if a:
        if player.hasCrown:
            player.setHasCrown(False)
        else:
            show = True
            updateRecord(score)
    if ps:
        count = 0
        for sprite in r:
            count += 1
            r.remove(sprite)
            if count == 3:
                break
    if pc:
        player.setHasCrown(True)
    screen.fill(COLOR)
    p.draw(screen)
    swords.draw(screen)
    crowns.draw(screen)
    r.draw(screen)
    draw_text(screen, "Score: " + str(score), 30, WIDTH/2-90, 20)
    draw_text(screen, "Record: " + str(getRecord()), 30, WIDTH/2+60, 20)
    pygame.draw.line(screen, LCOLOR, (0, 520), (500, 520), 4)
    pygame.display.update()
pygame.quit()
