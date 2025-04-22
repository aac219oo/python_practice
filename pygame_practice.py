import pygame as pg
import math
pg.init()

width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption("THIS IS TEST GAME")
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((187,252,255))
# pg.draw.rect(bg, (0,0,255),[70,70,500,60],4)
# pg.draw.rect(bg, (0,0,255),[70,70,500,60],0)
# pg.draw.circle(bg, (0,0,255),(100,255),50,4)
# pg.draw.ellipse(bg, (0,0,255),[70,70,500,60],4)
# pg.draw.arc(bg, (0,0,255),[70,70,500,60],5,1.5,4)
# pg.draw.line(bg, (0,0,255),(500,255),(550,400),4)
# 頭
pg.draw.circle(bg, (252,200,56),(320,240),100,0)

# 鼻
pg.draw.circle(bg, (255,0,0),(270,270),35,0)
pg.draw.circle(bg, (255,0,0),(370,270),35,0)
pg.draw.arc(bg, (0, 0, 0),[235, 235, 70, 70],math.pi+1.5, 1.6, 3)
pg.draw.arc(bg, (0, 0, 0),[335, 235, 70, 70],math.pi-1.6, -1.5, 3)
pg.draw.circle(bg, (255,0,0),(320,270),30,0)
pg.draw.circle(bg, (0,0,0),(320,270),30,3)
pg.draw.rect(bg, (255,255,255),[320,250,10,10],0)
pg.draw.rect(bg, (255,255,255),[370,250,10,10],0)
pg.draw.rect(bg, (255,255,255),[270,250,10,10],0)

# 嘴
pg.draw.arc(bg, (0, 0, 0),[275, 240, 90, 90],math.pi+0.6, -0.6, 3)

# 眼
pg.draw.ellipse(bg,(0, 0, 0),[280, 200, 25, 35],0)
pg.draw.ellipse(bg,(0, 0, 0),[330, 200, 25, 35],0)

# 眉
pg.draw.arc(bg, (0, 0, 0),[260, 175, 50, 60],0, math.pi, 3)
pg.draw.arc(bg, (0, 0, 0),[330, 175, 50, 60],0, math.pi, 3)

running = True
while running:
    screen.blit(bg, (0,0))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()