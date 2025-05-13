import pygame as pg
import math
import random
pg.init()

font = pg.font.SysFont(None, 20)

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
ball2_coord_text = font.render('', True, (255, 255, 255))
x2, y2 = rect2.topleft
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

ball_click = pg.Surface((70,70), pg.SRCALPHA)
ball_click.fill((255,255,255,0))
pg.draw.circle(ball_click, (255,255,255), (35,35),35,0)
rect_click = ball_click.get_rect()
rect_click.center = (random.randint(100,250), random.randint(150,250))
x_click, y_click = rect_click.topleft
direction_click = random.randint(20,70)
radian_click = math.radians(direction_click)
dx_click = 1 * math.cos(radian_click)
dy_click = -1 * math.sin(radian_click)

# 更新 ball2 顯示的文字
def update_ball2_text(x, y):
    global ball2_coord_text
    ball2_coord_text = font.render(f'({int(x)}, {int(y)})', True, (255, 255, 255))

update_ball2_text(x2, y2)

clock = pg.time.Clock()

running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if (dx_click == 0 and dy_click == 0):
                dx_click = tempX
                dy_click = tempY
            else:
                tempX = dx_click
                tempY = dy_click
                dx_click, dy_click = 0, 0
    
    x += speed
    rect.center = (x,y)
    if(rect.left <= 0 or rect.right >= screen.get_width()):
        speed *= -1

    x2 += dx
    y2 += dy
    rect2.center = (x2,y2)
    if(rect2.left <= 0 or rect2.right >= screen.get_width()):
        dx *= -1
        update_ball2_text(x2, y2)
    elif(rect2.top <= -1 or rect2.bottom >= screen.get_height()-1):
        dy *= -1
        update_ball2_text(x2, y2)
    
    y3 += speed3
    rect3.center = (x3,y3)
    if(rect3.top <= -1 or rect3.bottom >= screen.get_height()-1):
        speed3 *= -1

    x_click += dx_click
    y_click += dy_click
    rect_click.center = (x_click,y_click)
    if(rect_click.left <= 0 or rect_click.right >= screen.get_width()):
        dx_click *= -1
    elif(rect_click.top <= -1 or rect_click.bottom >= screen.get_height()-1):
        dy_click *= -1

    screen.blit(bg, (0,0))
    screen.blit(ball, rect.topleft)
    screen.blit(ball2, rect2.topleft)
    screen.blit(ball3, rect3.topleft)
    screen.blit(ball2_coord_text, (0, 0))
    screen.blit(ball_click, rect_click.topleft)

    pg.display.update()
pg.quit()