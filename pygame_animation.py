import pygame as pg
import math
import random
pg.init()

width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption("THIS IS ANIMATION")
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((0,0,0))

ball = pg.Surface((70,70), pg.SRCALPHA)
ball.fill((255,255,255,0))
pg.draw.circle(ball, (0,0,255), (35,35),35,0)
rect = ball.get_rect()
rect.center = (320,240)
x, y = rect.topleft
speed = 1

ball2 = pg.Surface((70,70), pg.SRCALPHA)
ball2.fill((255,255,255,0))
pg.draw.circle(ball2, (0,255,0), (35,35),35,0)
rect2 = ball2.get_rect()
rect2.center = (random.randint(100,250), random.randint(150,250))

x2, y2 = rect.topleft
direction = random.randint(20,70)
radian = math.radians(direction)
dx = 1 * math.cos(radian)
dy = -1 * math.sin(radian)

ball3 = pg.Surface((70,70), pg.SRCALPHA)
ball3.fill((255,255,255,0))
pg.draw.circle(ball3, (255,0,0), (35,35),35,0)
rect3 = ball3.get_rect()
rect3.center = (320,240)
x3, y3 = rect3.topleft
speed3 = 1

clock = pg.time.Clock()

running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    x += speed
    rect.center = (x,y)
    if(rect.left <= 0 or rect.right >= screen.get_width()):
        speed *= -1

    x2 += dx
    y2 += dy
    rect2.center = (x2,y2)
    if(rect2.left <= 0 or rect2.right >= screen.get_width()):
        dx *= -1
    elif(rect2.top <= -1 or rect2.bottom >= screen.get_height()-1):
        dy *= -1
    
    y3 += speed3
    rect3.center = (x3,y3)
    if(rect3.top <= -1 or rect3.bottom >= screen.get_height()-1):
        speed3 *= -1

    screen.blit(bg, (0,0))
    screen.blit(ball, rect.topleft)
    screen.blit(ball2, rect2.topleft)
    screen.blit(ball3, rect3.topleft)
    pg.display.update()
pg.quit()